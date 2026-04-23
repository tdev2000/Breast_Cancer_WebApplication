import tensorflow as tf

# Load trained Keras model
model = tf.keras.models.load_model("saved_model/breast_cancer_cnn.keras")

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# (Optional but recommended)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

tflite_model = converter.convert()

# Save file
with open("ai/breast_cancer_cnn.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ TFLite model created successfully!")