# ----------------------------------------------
# IMPORT REQUIRED LIBRARIES
# ----------------------------------------------
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import tensorflow as tf
import numpy as np  
import cv2
import os
import sqlite3
import re  #for validation

# ----------------------------------------------
#DATABASE CONNECTION FUCNTION
# ----------------------------------------------
def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# ----------------------------------------------
# INITIALIZE FLASK APP
# ----------------------------------------------
app = Flask(__name__)
app.secret_key = "secret_key_123"  #required for session tracking

#Enable CORS with credentials
CORS(app,supports_credentials=True)

#----------------------------------------------
# HOME ROUTE
#---------------------------------------------- 
@app.route("/", methods=["GET"])
def home():
    return "Breast Cancer Detection API (TFLite) is running."

#----------------------------------------------
# VALIDATION FUCNTION
#----------------------------------------------
#Check email format
def is_valid_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email) is not None
#Check password rules
def is_valid_password(password):
    return (
         len(password) >= 8 and
         re.search(r"[0-9]", password) and
         re.search(r"[!@#$%^&*]", password)
    )

#----------------------------------------------
# REGISTER ROUTE
#----------------------------------------------
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    #------------------ VALIDATION-------------------
    if not name:
        return jsonify({"error": "Name is required"}), 400
    if not email or not is_valid_email(email):
        return jsonify(
            {"error": "Invalid email format"} ), 400
    if not password or not is_valid_password(password):
        return jsonify(
            {"error": "Password must be at least 8 characters long, include a number & special character"}), 400  
    
    #------------------DATABASE CHECK-------------------
    conn = get_db()
    existing_doctor = conn.execute(
        "SELECT * FROM doctors WHERE email = ?", (email,)
    ).fetchone()

    if existing_doctor:
        conn.close()
        return jsonify({"error": "Already registered"}), 400
    
    #Insert new doctor into database
    #Hash the password before storing
    hashed_password = generate_password_hash(password)
    conn.execute(
        "INSERT INTO doctors (name, email, password) VALUES (?, ?, ?)", 
        (name.strip(), email.strip(), hashed_password)
    )
    conn.commit()
    conn.close()

    return jsonify({"success": "Doctor registered successfully"})
#----------------------------------------------
# LOGIN ROUTE
#----------------------------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    #------------------ VALIDATION-------------------
    if not email or not is_valid_email(email):
        return jsonify(
            {"error": "Invalid email format"}
            ), 400
    if not password:
        return jsonify(
            {"error": "Password is required"}
            ), 400  
    
    #------------------DATABASE CHECK-------------------

    conn = get_db()
    doctor = conn.execute(
        "SELECT * FROM doctors WHERE email = ?", 
        (email.strip(),)
    ).fetchone()

    if doctor and check_password_hash(doctor["password"], password):
        #Store doctor info in session 
        session["doctor_id"] = doctor["id"]
        session["doctor_name"] = doctor["name"]

        return jsonify({
            "success": True, 
            "doctor_id": doctor["id"], 
            "name": doctor["name"]
        })
    else:
        return jsonify({"error": "Invalid email or password"}), 401
    
#----------------------------------------------
# LOGOUT ROUTE
#----------------------------------------------
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"})

# ----------------------------------------------
# LOAD TFLITE MODEL
# ----------------------------------------------
interpreter = tf.lite.Interpreter(
    model_path="ai/breast_cancer_cnn.tflite"
)
interpreter.allocate_tensors()

# Get input & output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# ----------------------------------------------
# CLASS LABELS
# ----------------------------------------------
class_names = ["Normal", "Benign", "Malignant"]

# ----------------------------------------------
# IMAGE PREPROCESSING FUNCTION
# ----------------------------------------------
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))

    image = image.astype(np.float32) / 255.0
    image = np.expand_dims(image, axis=0)

    return image
# ----------------------------------------------
# UPLOAD FOLDER
# ----------------------------------------------
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):   
    os.makedirs(UPLOAD_FOLDER)

# ----------------------------------------------
# PREDICTION ROUTE -SESSION BASED
# ----------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():

    print("PREDICT ROUTE HIT")
    #Check if doctor is logged in
    doctor_id = session.get("doctor_id")
    if not doctor_id:
        return jsonify({"error": "Unauthorized - Please log in"}), 401
    
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    file = request.files["image"]
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    #----------------------------------------------
    #GET PATIENT DETAILS FROM FRONTEND
    #---------------------------------------------- 
    first_name = request.form.get("firstName")
    last_name = request.form.get("lastName")
    date_of_birth = request.form.get("dateOfBirth")
    history = request.form.get("history")

    #----------------------------------------------
    #PREPROCESS IMAGE
    #----------------------------------------------
    image = preprocess_image(file_path)

    # Run model
    interpreter.set_tensor(input_details[0]["index"], image)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]["index"])

    output = np.array(output)
    #----------------------------------------------
    #GET PREDICTION & CONFIDENCE
    #----------------------------------------------
    try:
        predicted_index = int(np.argmax(output))
        predicted_class = class_names[predicted_index]
        confidence = float(output[0][predicted_index]) 


    except:
        predicted_class = "Unknown"
        confidence = 0.0

    # Save prediction to database
    conn = get_db()
    conn.execute("""
    INSERT INTO patients 
    (doctor_id, first_name, last_name, date_of_birth, history, prediction, confidence) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        doctor_id,
        first_name,
        last_name,
        date_of_birth,
        history,
        predicted_class,
        confidence
    ))

    #----------------------------------------------
    #DOCTORE RECCOMENDATION 
    #----------------------------------------------
    referral_suggestions = []

    #Get diagnosis id
    diagnosis_row = conn.execute(
        "SELECT id FROM diagnosis WHERE type = ?", (predicted_class,)
    ).fetchone()
    
    diagnosis_id = None
    if diagnosis_row:
        diagnosis_id = diagnosis_row["id"]

        #Get recomended doctors
        doctors = conn.execute("""
        SELECT d.id, d.name, d.specialization, d.rating, d.hospital_affiliation, d.location,d.availability, 
        d.years_of_experience,d.cases_handled, dd.priority_level
        FROM doctors d
        JOIN doctor_diagnosis dd ON d.id = dd.doctor_id
        WHERE dd.diagnosis_id = ?
        ORDER BY dd.priority_level DESC, d.rating DESC
        """, (diagnosis_id,)).fetchall()

        referral_suggestions = [dict(doctor) for doctor in doctors]

    conn.commit()
    conn.close()

    return jsonify({
    "prediction": predicted_class,
    "confidence": confidence,
    "referral_suggestions": referral_suggestions
    })

# ----------------------------------------------
# GET PATIENTS -ONLY FOR THE LOGGED IN DOCTOR
#-----------------------------------------------
@app.route("/patients", methods=["GET"])
def get_patients():

    doctor_id = session.get("doctor_id")
    if not doctor_id:
        return jsonify({"error": "Unauthorized - Please log in"}), 401
    
    conn = get_db()
    patients = conn.execute(
        "SELECT * FROM patients WHERE doctor_id = ?", (doctor_id,)).fetchall()
    conn.close()

    return jsonify([dict(patient) for patient in patients])

# ----------------------------------------------
#DELETE PATIENT RECORD 
#-----------------------------------------------
@app.route("/patients/<int:patient_id>", methods=["DELETE"])
def delete_patient(patient_id):
    conn = get_db()

    conn.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Patient record deleted successfully"})

# ----------------------------------------------
#Update patient record
#-----------------------------------------------
@app.route("/patients/<int:patient_id>", methods=["PUT"])
def update_patient(patient_id):
    data = request.get_json()

    conn = get_db()
    conn.execute("""
        UPDATE patients
        SET first_name = ?, last_name = ?, date_of_birth = ?, history = ?
        WHERE id = ?
    """, (
        data.get("first_name"),
        data.get("last_name"),
        data.get("date_of_birth"),
        data.get("history"),
        patient_id
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Patient record updated successfully"})
# ----------------------------------------------
# RUN FLASK APP
# ----------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
