import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
import torchvision.transforms as transforms


# 이미지 전처리 함수
def transform_image(image):
   
    image = image.resize((28, 28))  
    image = transforms.ToTensor()(image)  
    image = image.unsqueeze(0)  
    return image

# 모델 정의
class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        
        # Convolutional layers
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1) 
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        
        # Fully connected layers
        self.fc1 = nn.Linear(64 * 7 * 7, 128) 
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10) 

    def forward(self, x):
        x = F.relu(self.conv1(x))  
        x = F.max_pool2d(x, 2) 
        
        x = F.relu(self.conv2(x))  
        x = F.max_pool2d(x, 2)  
        
        x = x.view(-1, 64 * 7 * 7)  
        
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        
        return x

# 모델 불러오기 함수
def load_model(model_path):
    model = ConvNet()  # Create the model instance
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu'), weights_only=True))  # Load only the weights
    model.eval()  # Set the model to evaluation mode
    return model

def predict(file):
    model = load_model('models/F_mnist_model.pth')
    if file:
        # 이미지를 전처리하고 모델로 예측
        img = Image.open(file)
        processed_img = transform_image(img)
        
        # 예측
        prediction = model(processed_img)
        result = torch.argmax(prediction, dim=1).item()
    
    return result
