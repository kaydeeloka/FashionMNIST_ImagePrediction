document.getElementById('fileInput').addEventListener('change', function() {
    // Check if a file is selected
    var fileInput = document.getElementById('fileInput').files[0];
    if (fileInput) {
        // Change the <h2> text
        document.querySelector('h2').innerText = 'Image is uploaded!';
    } else {
        document.querySelector('h2').innerText = 'Please upload an image';
    }
});

document.getElementById('uploadButton').addEventListener('click', function() {
    var fileInput = document.getElementById('fileInput').files[0];
    if (!fileInput) {
        alert('Please select a file!');
        return;
    }

    var formData = new FormData();
    formData.append('file', fileInput);

    // Image preview
    var reader = new FileReader();
    reader.onload = function(e) {
        var uploadedImage = document.getElementById('uploadedImage');
        uploadedImage.src = e.target.result;
        uploadedImage.style.display = 'block'; // Show image
        uploadedImage.style.width = '400px'; // Set width
        uploadedImage.style.height = '400px'; // Set height
    };
    reader.readAsDataURL(fileInput); // Read the file as data URL

    // Display uploading message
    document.getElementById('result').innerText = 'Processing image...';

    // Make the POST request to Flask backend
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.prediction !== undefined) {
            document.getElementById('result').innerText = 'Prediction : ' + data.prediction;
        } else {
            document.getElementById('result').innerText = 'Error : ' + (data.error || 'Unknown error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error occurred during prediction.';
    });
});
