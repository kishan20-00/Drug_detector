from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import json
import cv2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the pre-trained model
MODEL_PATH = 'weed_classification_model.h5'
model = load_model(MODEL_PATH)

# Load the class labels (weed varieties)
with open('class_labels.json', 'r') as f:
    class_labels = json.load(f)

# Image size expected by the model
IMG_SIZE = (128, 128)

# Preprocessing function to prepare the image for the model
def preprocess_image(image_path, target_size):
    img = cv2.imread(image_path)
    if img is not None:
        img = cv2.resize(img, target_size)
        img = img.astype('float32') / 255.0  # Normalize
        img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No image file found'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        # Save the uploaded image to a temporary directory
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)
        
        # Preprocess the image for the model
        img = preprocess_image(filepath, IMG_SIZE)
        
        # Make prediction
        predictions = model.predict(img)
        predicted_class_idx = np.argmax(predictions)
        predicted_class = class_labels[predicted_class_idx]  # Get class name from index
        
        # Delete the saved file
        os.remove(filepath)
        
        return jsonify({'predicted_class': predicted_class})
    
    return jsonify({'error': 'Invalid request'}), 400

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')  # Create uploads directory if it doesn't exist
    app.run(debug=True)
