import torch
from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer

# Load the pre-trained model, feature extractor, and tokenizer
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

# Set device to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()


def generate_caption(image_path):
    # Open and ensure the image is in RGB mode
    image = Image.open(image_path)
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Use the Hugging Face feature extractor to process the image
    inputs = feature_extractor(images=image, return_tensors="pt")
    pixel_values = inputs.pixel_values.to(device)

    # Generate output IDs and decode to text
    with torch.no_grad():
        output_ids = model.generate(pixel_values)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return caption


# Make sure "sample.jpg" exists in your working directory, or change the path accordingly.
print(generate_caption("C:\\Users\\direo\\Downloads\\archive(3)\mammals\\african_elephant\\african_elephant-0328.jpg"))
