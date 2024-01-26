from PIL import Image
from model import Shufflenet_V2_X2_0

import streamlit as st

import torch
from torchvision import transforms
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


@st.cache
def load_model(model_path):
    model_best = torch.load(model_path, map_location="cpu")
    model =Shufflenet_V2_X2_0()
    model.load_state_dict(model_best)
    model.to(device)
    return model

@st.cache
def load_metadata(metadata_path):
    metadata = torch.load(metadata_path)
    transform = transforms.Compose([
        transforms.Resize(metadata.img_resize),
        transforms.CenterCrop(metadata.img_crop_size),
        transforms.ToTensor()
    ])
    classes = metadata.classes
    return transform, classes


def predict_img(img_file):
    model = load_model("F:\Jupyter Notebook Python\deep_learning-master\deep_learning-master\Skin Cancer Classification\content\output\model_best.pth")
    transform, classes = load_metadata("F:\Jupyter Notebook Python\deep_learning-master\deep_learning-master\Skin Cancer Classification\content\output\configs.pth")

    img = Image.open(img_file)
    img = transform(img).unsqueeze(0)
    with torch.no_grad():
        output = model(img)
        pred_id = output.argmax(dim=1)
        pred = classes[pred_id]
    return pred