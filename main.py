import torch
import torchvision.models as models
from markdown_it.rules_inline import image

resnet = models.resnet18(pretrained=True)
resnet.eval()

from torchvision import transforms
from PIL import Image

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),

])
img = Image.open("C:\\Users\\direo\Downloads\\archive(3)\\mammals\\african_elephant\\african_elephant-0258.jpg")
img = transform(img).unsqueeze(0)

from transformers import VisionEncoderDecoderModel, AutoTokenizer

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")


def generate_caption(image_path):
    image = Image.open(image_path)
    inputs = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model.generate(inputs)

    caption = tokenizer.decode(output[0], skip_special_tokens=True)
    return caption


print(generate_caption("sample.jpg"))
