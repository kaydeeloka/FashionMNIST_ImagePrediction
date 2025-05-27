from flask import Flask, request, jsonify, render_template
from modules.model import load_model  # Import the model load function
from modules.data_processing import transform_image  # Import the image processing function
import torch
from PIL import Image

app = Flask(__name__)

# Load the model once when the app starts
model = load_model('models/F_mnist_model.pth')  # Load the saved model

@app.route('/')
def index():
    return render_template('index.html')  # Return the index.html template

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not file.content_type.startswith('image'):
        return jsonify({'error': 'Invalid file type. Please upload an image.'}), 400
    
    if file:
        try:
            # Open the image and process it
            img = Image.open(file)
            processed_img = transform_image(img)  # Process the image for prediction
            
            # Prediction using the model
            with torch.no_grad():  # No need to compute gradients during inference
                prediction = model(processed_img)
                result = torch.argmax(prediction, dim=1).item()  # Get the predicted class index
            
            # Define the class labels for Fashion MNIST
            class_labels = [
                'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal',
                'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
            ]
            
            # Map the predicted index to the corresponding class label
            predicted_label = class_labels[result]
            
            # Return the prediction result with a success message
            return jsonify({'message': 'Prediction successful', 'prediction': predicted_label})
    
        except Exception as e:
            # Return the error message with a failure status code
            return jsonify({'message': 'Prediction failed', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)