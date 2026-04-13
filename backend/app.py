# ----------------------------------------------
# IMPORT REQUIRED LIBRARIES
# ----------------------------------------------
from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import cv2
import os
import sqlite3

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
CORS(
    app,
    resources={r"/predict": {"origins": "*"}},
    supports_credentials=False
)

@app.route("/", methods=["GET"])
def home():
    return "Breast Cancer Detection API (TFLite) is running."

# ----------------------------------------------
# UPLOAD FOLDER
# ----------------------------------------------
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

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

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    thresholded = cv2.cvtColor(thresholded, cv2.COLOR_GRAY2RGB)

    image = thresholded.astype(np.float32) / 255.0
    image = np.expand_dims(image, axis=0)

    return image

# ----------------------------------------------
# PREDICTION ROUTE
# ----------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    # Preprocess image
    image = preprocess_image(file_path)

    # Run inference
    interpreter.set_tensor(input_details[0]["index"], image)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]["index"])

    predicted_index = int(np.argmax(output))
    predicted_class = class_names[predicted_index]
    confidence = float(output[0][predicted_index])

    return jsonify({
        "prediction": predicted_class,
        "confidence": confidence 
    })

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    conn = get_db()
    doctor = conn.execute("SELECT * FROM doctors WHERE email = ? AND password = ?", 
                          (email, password)).fetchone()
    conn.close()

    if doctor:
        return jsonify({
            "success": "Login successful", 
            "doctor_id": doctor["id"], 
            "name": doctor["name"]})
    else:
        return jsonify({"success": "False"}), 401
# ----------------------------------------------
# RUN FLASK APP
# ----------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
