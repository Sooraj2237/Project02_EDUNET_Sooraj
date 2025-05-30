# Crop Disease Detection

## Introduction

In this project I used `Azure Custom Vision` to create an AI Model that can view images of the Tomato Leaves and give confidence score. 

Then I made the `crop-disease-detection.py` to check the working of the model using AZURE API.

I have also deployed it as a chatbot interface using `Lovable AI` and thus please visit - https://crop-disease-detector-sooraj.lovable.app

## Features

- Detects diseases in tomato leaves using AI.
- Utilizes Azure Custom Vision for image classification.
- Provides confidence scores for predictions.
- Easy-to-use Python script for model inference.

## Getting Started

### Prerequisites

- Python 3.x
- Azure account with Custom Vision resources
- Required Python packages (see `requirements.txt`)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/Project02_EDUNET_Sooraj.git
    cd Project02_EDUNET_Sooraj
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Set your Azure Custom Vision API credentials in `crop-disease-detection.py`.
2. Run the script with an image:
    ```bash
    python crop-disease-detection.py --image path/to/tomato_leaf.jpg
    ```

## Project Structure

```
.
├── DataSet
    ├── Tomato Early Blight
    ├── Tomato Late Blight
    ├── Tomato Septoria Leaf Spot
    ├── Tomato Leaf Mold
    └── Tomato Healthy
├── crop-disease-detection.py
├── requirements.txt
└── README.md
```

## License

This project is licensed under the MIT License.