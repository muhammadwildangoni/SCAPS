from PIL import Image

import torch
from torchvision import datasets, transforms, models

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model = torch.load("model_best.pth", map_location="cpu").to(device)
metadata = torch.load("configs.pth")
model.eval()

def predict(image_path):
    transform = transforms.Compose([
    transforms.Resize(metadata["img_resize"]),
    transforms.CenterCrop(metadata["img_crop_size"]),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])   
    with torch.no_grad():
        img = Image.open(image_path).convert("RGB")   
        img_trans = transform(img).unsqueeze(0).to(device)
        output = model(img_trans)
        pred_id = output.argmax(1)
        pred = metadata['classes'][pred_id]
    print(pred)
    return pred
