import json
import ast

# Function to calculate area of a bounding box
def calculate_area(bbox):
    width = bbox[1]["X"] - bbox[0]["X"]
    height = bbox[1]["Y"] - bbox[0]["Y"]
    return abs(width * height)

# Define a threshold for the minimum area (tweak as needed)
min_area_threshold = 50  # Example threshold, adjust according to your needs

# Load the JSON data from the file
file_path = 'dataset/labels/train/0_cloudy_and_medium_wave_1.txt'
with open(file_path, 'r') as file:
    json_string = file.read().strip()

# Remove outer quotes and unescape the string
json_string = ast.literal_eval(json_string)

# Parse the JSON data
data = json.loads(json_string)

# Filter out bounding boxes with an area close to zero
filtered_tracked_obj = []
for obj in data["TrackedObj"]:
    bbox_area = calculate_area(obj["BB2D"])
    if bbox_area >= min_area_threshold:
        filtered_tracked_obj.append(obj)

# Update the data with the filtered bounding boxes
data["TrackedObj"] = filtered_tracked_obj

# Write the filtered data back to the file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Filtered bounding boxes with small areas.")
