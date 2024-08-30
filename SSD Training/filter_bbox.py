import json
import ast

 
def calculate_area(bbox):
    width = bbox[1]["X"] - bbox[0]["X"]
    height = bbox[1]["Y"] - bbox[0]["Y"]
    return abs(width * height)

 
min_area_threshold = 50  # Example threshold 

 
file_path = 'dataset/labels/train/0_cloudy_and_medium_wave_1.txt'
with open(file_path, 'r') as file:
    json_string = file.read().strip()

 
json_string = ast.literal_eval(json_string)

 
data = json.loads(json_string)

 
filtered_tracked_obj = []
for obj in data["TrackedObj"]:
    bbox_area = calculate_area(obj["BB2D"])
    if bbox_area >= min_area_threshold:
        filtered_tracked_obj.append(obj)
 
data["TrackedObj"] = filtered_tracked_obj

 
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Filtered bounding boxes with small areas.")
