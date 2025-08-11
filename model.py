# model.py

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf

# Load your trained model
model = load_model('kidney_stone_detection_cnn_model.h5')  # Update the path if needed

# Define class labels
class_labels = ['Normal', 'Stone']

def predict_image(img_path):
    # Load the image with the correct target size as per model input
    img = image.load_img(img_path, target_size=(224, 224))  # Matches model input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Shape becomes (1, 224, 224, 3)
    img_array /= 255.0  # Normalize the image

    # Predict using the model
    prediction = model.predict(img_array)

    # Get class label and confidence
    class_index = np.argmax(prediction[0])
    confidence = round(float(prediction[0][class_index]) * 100, 2)
    result = class_labels[class_index]

    return result, confidence
