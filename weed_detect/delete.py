import os
import pandas as pd

# Load the CSV file containing weed variety and image filenames
csv_file = 'labels.csv'  # Path to your CSV file
df = pd.read_csv(csv_file)

# Specify the folder containing the images
image_folder = 'images/'  # Path to your image folder

# Filter the rows where the Weed_Variety is 'negative'
negative_images = df[df['Species'] == 'Negative']['Filename'].values

# Function to delete images
def delete_images(image_folder, filenames):
    deleted_count = 0
    for filename in filenames:
        image_path = os.path.join(image_folder, filename)
        if os.path.exists(image_path):
            os.remove(image_path)
            deleted_count += 1
            print(f"Deleted: {filename}")
        else:
            print(f"File not found: {filename}")
    return deleted_count

# Delete the 'negative' images
deleted_count = delete_images(image_folder, negative_images)
print(f"Total deleted images: {deleted_count}")