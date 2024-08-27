import json
import ast
import os

# Function to calculate area of a bounding box
def calculate_area(bbox):
    width = bbox[1]["X"] - bbox[0]["X"]
    height = bbox[1]["Y"] - bbox[0]["Y"]
    return abs(width * height)

# Define a threshold for the minimum area and width/height constraints
min_area_threshold = 50  # Example threshold, adjust according to your needs
min_width = 10
min_height = 30

# Path to the directory containing the label files
directory_path = 'dataset/labels/test'

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory_path, filename)
        
        # Load the JSON data from the file
        with open(file_path, 'r') as file:
            json_string = file.read().strip()

        # Remove outer quotes and unescape the string
        json_string = ast.literal_eval(json_string)

        # Parse the JSON data
        data = json.loads(json_string)

        # Filter out bounding boxes based on area, width, and height constraints
        filtered_tracked_obj = []
        for obj in data.get("TrackedObj", []):
            bbox = obj.get("BB2D", [])
            if len(bbox) == 2:  # Ensure that the bounding box has two points
                width = bbox[1]["X"] - bbox[0]["X"]
                height = bbox[1]["Y"] - bbox[0]["Y"]
                bbox_area = calculate_area(bbox)

                if bbox_area >= min_area_threshold and width >= min_width and height >= min_height:
                    filtered_tracked_obj.append(obj)

        # Update the data with the filtered bounding boxes
        data["TrackedObj"] = filtered_tracked_obj

        # Write the filtered data back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Filtered bounding boxes in file: {filename}")
