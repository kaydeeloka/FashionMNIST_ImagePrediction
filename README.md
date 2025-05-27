# FASHION MNIST FLASK APPLICATION

# Directory Structure
/your_app/
├ app.py # Flask application entry point
 ├ static/
 │ ├ css/
           └ style.css
 │ ├ data/
           └ Fmnist_dataset.ipynb # Jupyter notebook for downloading and processing the dataset
 │ └ js/
           └ mnist.js
 ├ templates/
 │ └ index.html # HTML template for the UI
 ├ models/
 │  └ F_mnist_model.pth # Pre-trained model file
 └ modules/
 └ data_processing.py # Image processing logic
 └ model.py


## Installation
1. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv (if already have can use your own venv)

2. **Change the user preference for the PowerShell script execution policy**
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process 
   
3. **Activate venv**
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Install Jupyter (If Not Installed)**:
    ```bash
    pip install jupyter
    ```

6. **Download the Fashion MNIST dataset and save images **:
   -Navigate to the static\data folder and open fmnist_dataset.ipynb 
   -Run the fmnist_dataset.ipynb notebook code 1 and 4 to download the dataset and save a few example images. The Fmnist_images folder will contain subfolders for each class, and inside each subfolder, 3 images corresponding to that class will be saved. This is necessary for testing the app.
   -Once the F_mnist_dataset.ipynb file is open, you can run the notebook step by step. To run a cell, click on it and press Shift + Enter.    

## Usage

1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Access the application**:
    - `http://127.0.0.1:5000` will directly go to the main web browser.

3. **Image Upload**:
    - Users can upload an image of fashion items (such as T-shirts, trousers, or shoes) via the index.html page.
    - You can used the save images inside the Fmnist_images folder to test the website.
    - Once the image is uploaded and processed, the predicted class label is displayed on the page.

## Error Handling

- No file uploaded: If no file is selected during the image upload, the app will return an error message.
- Invalid file type: Only image files are accepted. If a non-image file is uploaded, an error will be shown.
- Prediction errors: If an error occurs during the prediction process (e.g., model loading issue), the app will return a failure message with an error description.



