from PIL import Image
import torchvision.transforms as transforms

def transform_image(image):
    # Convert to grayscale if the image is not already in grayscale
    if image.mode != 'L':
        image = image.convert('L')  # 'L' mode is grayscale in PIL
    
    # Normalize pixel values to be between 0 and 1
    image = image.resize((28, 28))  # Resize the image to 28x28 pixels
    image = transforms.ToTensor()(image)  # Convert image to tensor
    image = image.unsqueeze(0)  # Add a batch dimension (1, 1, 28, 28)
    image = transforms.Normalize((0.5,), (0.5,))(image)  # Normalize pixel values
    return image