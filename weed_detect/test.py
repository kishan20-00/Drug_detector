import requests

# URL of the hosted Flask app (replace with your actual URL)
url = 'http://127.0.0.1:5000/predict'  # Example: 'http://localhost:5000/predict'

# Path to the image file you want to test
image_path = 'images/20170711-115741-0.jpg'  # Replace with the path to your test image

# Open the image file in binary mode
with open(image_path, 'rb') as img_file:
    # Create the payload for the POST request
    files = {'file': img_file}
    
    # Send the POST request with the image file
    response = requests.post(url, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the predicted class (weed variety)
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
