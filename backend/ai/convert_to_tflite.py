import tensorflow as tf

# Load the Keras model
model = tf.keras.models.load_model("saved_model/breast_cancer_cnn.keras")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_types = [tf.float16]

tflite_model = converter.convert()

with open("breast_cancer_cnn.tflite", "wb") as f:
    f.write(tflite_model)

print("TFLite model created successfully!")
