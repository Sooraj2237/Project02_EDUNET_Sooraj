import os
from dotenv import load_dotenv
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

load_dotenv()

# Get credentials from environment variables
PREDICTION_KEY = os.getenv("PREDICTION_KEY")
PREDICTION_ENDPOINT = os.getenv("PREDICTION_ENDPOINT")
PROJECT_ID = os.getenv("PROJECT_ID")
PUBLISHED_NAME = os.getenv("PUBLISHED_NAME")

def predict_image_from_file(image_path):
    """
    Predict image classification from a local file
    """
    # Validate that environment variables are loaded
    if not all([PREDICTION_KEY, PREDICTION_ENDPOINT, PROJECT_ID, PUBLISHED_NAME]):
        print("Error: Missing environment variables. Please check your .env file.")
        return None, None
    
    # Create prediction client
    credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
    predictor = CustomVisionPredictionClient(PREDICTION_ENDPOINT, credentials)
    
    try:
        # Open and read the image file
        with open(image_path, "rb") as image_contents:
            results = predictor.classify_image(
                PROJECT_ID, 
                PUBLISHED_NAME, 
                image_contents.read()
            )
        
        # Display results
        print(f"\nPrediction results for: {image_path}")
        print("-" * 50)
        
        for prediction in results.predictions:
            print(f"Disease: {prediction.tag_name}")
            print(f"Confidence: {prediction.probability * 100:.2f}%")
            print("-" * 30)
            
        # Get the top prediction
        top_prediction = max(results.predictions, key=lambda x: x.probability)
        return top_prediction.tag_name, top_prediction.probability
        
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found!")
        return None, None
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return None, None

def predict_image_from_url(image_url):
    """
    Predict image classification from a URL
    """
    # Validate that environment variables are loaded
    if not all([PREDICTION_KEY, PREDICTION_ENDPOINT, PROJECT_ID, PUBLISHED_NAME]):
        print("Error: Missing environment variables. Please check your .env file.")
        return None, None
    
    # Create prediction client
    credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
    predictor = CustomVisionPredictionClient(PREDICTION_ENDPOINT, credentials)
    
    try:
        results = predictor.classify_image_url(
            PROJECT_ID, 
            PUBLISHED_NAME, 
            url=image_url
        )
        
        # Display results
        print(f"\nPrediction results for URL: {image_url}")
        print("-" * 50)
        
        for prediction in results.predictions:
            print(f"Disease: {prediction.tag_name}")
            print(f"Confidence: {prediction.probability * 100:.2f}%")
            print("-" * 30)
            
        # Get the top prediction
        top_prediction = max(results.predictions, key=lambda x: x.probability)
        return top_prediction.tag_name, top_prediction.probability
        
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return None, None

def main():
    print("🌱 Crop Disease Detection using Custom Vision")
    print("=" * 50)
    
    # Check if environment variables are loaded
    if not all([PREDICTION_KEY, PREDICTION_ENDPOINT, PROJECT_ID, PUBLISHED_NAME]):
        print("\n❌ Error: Environment variables not found!")
        print("Please ensure you have a .env file with the following variables:")
        print("- PREDICTION_KEY")
        print("- PREDICTION_ENDPOINT")
        print("- PROJECT_ID")
        print("- PUBLISHED_NAME")
        return
    
    while True:
        print("\nChoose an option:")
        print("1. Test with local image file")
        print("2. Test with image URL")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            image_path = input("Enter the path to your image file: ").strip()
            disease, confidence = predict_image_from_file(image_path)
            
            if disease:
                print(f"\n🎯 RESULT: {disease} ({confidence * 100:.2f}% confidence)")
                
        elif choice == "2":
            image_url = input("Enter the image URL: ").strip()
            disease, confidence = predict_image_from_url(image_url)
            
            if disease:
                print(f"\n🎯 RESULT: {disease} ({confidence * 100:.2f}% confidence)")
                
        elif choice == "3":
            print("Goodbye! 👋")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
