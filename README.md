# Image Captioning with Vision Encoder-Decoder

This project demonstrates an **image captioning** system that leverages a pre-trained vision encoder-decoder model to generate descriptive captions for images. It combines the power of computer vision and natural language processing using Hugging Face's `nlpconnect/vit-gpt2-image-captioning` model.

## Overview

Image captioning is the task of automatically generating natural language descriptions for given images. This repository uses:
- **Hugging Face Transformers** to load a pre-trained vision encoder-decoder model.
- **ViTFeatureExtractor** to preprocess images appropriately.
- **PyTorch** as the deep learning framework.

The project is designed for quick experimentation and demonstration, and it runs on GPU if available.

## Features

- **Pre-trained Model:** Uses `nlpconnect/vit-gpt2-image-captioning` for generating captions.
- **Easy-to-Use:** Simple function `generate_caption(image_path)` to produce captions.
- **Flexible:** Easily extendable for different image datasets or additional processing.

