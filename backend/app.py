#IMPORT REQUIRED LIBRARIES
#----------------------------------------------

from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
import os

#----------------------------------------------
#INITIALIZE FLASK APP
#----------------------------------------------

app = Flask(__name__)

#----------------------------------------------
#Folder to save uploaded images
#----------------------------------------------

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Create upload folder if it,s not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

#----------------------------------------------
#LOAD PRE-TRAINED MODEL
#----------------------------------------------
model = tf.keras.models.load_model("ai/saved_model/breast_cancer_cnn.keras")

#----------------------------------------------
#Class labels
#----------------------------------------------
class_names = ["Normal", "Benign", "Malignant"]

#----------------------------------------------
#mage preprocessing function using OpenCv
#----------------------------------------------

def preprocess_image(image_path):

    #Read image using OpenCv
    image = cv2.imread(image_path)
    
    #Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #Resize image to 224x224
    image_resized= cv2.resize(image_rgb, (224, 224))

    #Convert to grayscale for thresholding
    gray = cv2.cvtColor(image_resized, cv2.COLOR_RGB2GRAY)

    #Apply thresholding
    _, threshholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    #Thresholded back to RGB
    threshholded_rgb = cv2.cvtColor(threshholded, cv2.COLOR_GRAY2RGB)

    #Normalize image values to [0,1]
    image_normalized = threshholded_rgb / 255.0

    #Expand dimensions to match model input
    image_final = np.expand_dims(image_normalized, axis=0)
    return image_final

#----------------------------------------------
#Prediction Route
#----------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    #Check if image is uploaded
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})
    
    file = request.files["image"]

    #Save uploaded image
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    #Preprocess image and make prediction
    preprocess_image = preprocess_image(file_path)
    predictions = model.predict(preprocess_image)

    #Get predicted class and confidence
    predicted_index = np.argmax(predictions)
    predicted_class = class_names[predicted_index]
    confidence = float(np.max(predictions)) * 100

    #Send rsult to frontend
    return jsonify({
        "prediction": predicted_class,
        "confidence": round(confidence , 2)
    })

#----------------------------------------------
#Run the Flask app
#----------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)