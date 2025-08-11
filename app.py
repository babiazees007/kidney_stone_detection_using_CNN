# app.py
from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
import pandas as pd
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)

model = load_model("kidney_stone_detection_cnn_model.h5")
UPLOAD_FOLDER = 'static/uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load dataset statistics
def load_dataset_stats():
    try:
        df = pd.read_csv("kidneyData.csv")
        stats = {
            'total_images': len(df),
            'class_distribution': df['Class'].value_counts().to_dict(),
            'class_percentages': (df['Class'].value_counts() / len(df) * 100).round(1).to_dict(),
            'dataset_info': {
                'normal_count': len(df[df['Class'] == 'Normal']),
                'stone_count': len(df[df['Class'] == 'Stone']),
                'cyst_count': len(df[df['Class'] == 'Cyst']),
                'tumor_count': len(df[df['Class'] == 'Tumor'])
            }
        }
        return stats
    except Exception as e:
        print(f"Error loading dataset stats: {e}")
        return None

dataset_stats = load_dataset_stats()

@app.route('/')
def index():
    return render_template('home.html', dataset_stats=dataset_stats)

@app.route('/statistics')
def statistics():
    return render_template('statistics.html', dataset_stats=dataset_stats)

@app.route('/api/dataset-stats')
def api_dataset_stats():
    return jsonify(dataset_stats)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        img = image.load_img(filepath, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        prediction_proba = prediction[0]
        
        # Get prediction confidence
        confidence = float(np.max(prediction_proba)) * 100
        predicted_class = np.argmax(prediction)
        result = 'Normal Image' if predicted_class == 0 else 'Stone Image'
        
        # Enhanced prediction data
        prediction_data = {
            'result': result,
            'confidence': round(confidence, 2),
            'probabilities': {
                'normal': round(float(prediction_proba[0]) * 100, 2),
                'stone': round(float(prediction_proba[1]) * 100, 2) if len(prediction_proba) > 1 else 0
            },
            'predicted_class': int(predicted_class)
        }

        return render_template('result.html', 
                             prediction=result, 
                             image_filename=filename,
                             prediction_data=prediction_data,
                             dataset_stats=dataset_stats)

if __name__ == '__main__':
    app.run(debug=True)
