import json
import ast
import os

 
def calculate_area(bbox):
    width = bbox[1]["X"] - bbox[0]["X"]
    height = bbox[1]["Y"] - bbox[0]["Y"]
    return abs(width * height)

 
min_area_threshold = 50  
min_width = 10
min_height = 30
 
directory_path = 'dataset/labels/train'

 
for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory_path, filename)
        
     
        with open(file_path, 'r') as file:
            json_string = file.read().strip()

       
        json_string = ast.literal_eval(json_string)

  
        data = json.loads(json_string)

    
        filtered_tracked_obj = []
        for obj in data.get("TrackedObj", []):
            bbox = obj.get("BB2D", [])
            if len(bbox) == 2:  # Ensure that the bounding box has two points
                width = bbox[1]["X"] - bbox[0]["X"]
                height = bbox[1]["Y"] - bbox[0]["Y"]
                bbox_area = calculate_area(bbox)

                if bbox_area >= min_area_threshold and width >= min_width and height >= min_height:
                    filtered_tracked_obj.append(obj)

    
        data["TrackedObj"] = filtered_tracked_obj
 
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Filtered bounding boxes in file: {filename}")
