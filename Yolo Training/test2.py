import ast
import json
import os

# Define image dimensions
image_width = 1280
image_height = 720

class_mapping = {
    "Containership": 0,
    "Fishing_Vassel": 1,
    "sailboat": 2,
    "cruiseship": 3,
    "dingyboat": 4,
    "tugboat": 5,
    "Yacht": 6
}

input_dir = 'dataset/labels/val'
output_dir = 'dataset/labels/val_yolo_format'

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)

        with open(input_file_path, 'r') as file:
            json_string = file.read().strip()

        json_string = ast.literal_eval(json_string)
        data = json.loads(json_string)

        lines = []
        for obj in data["TrackedObj"]:
            class_id = class_mapping.get(obj["Alias"])
            if class_id is None:
                continue
            
            x_min, y_min = obj["BB2D"][0]["X"], obj["BB2D"][0]["Y"]
            x_max, y_max = obj["BB2D"][1]["X"], obj["BB2D"][1]["Y"]

            # Normalize values
            x_center = ((x_min + x_max) / 2) / image_width
            y_center = ((y_min + y_max) / 2) / image_height
            width = (x_max - x_min) / image_width
            height = (y_max - y_min) / image_height

            lines.append(f"{class_id} {x_center} {y_center} {width} {height}")

        with open(output_file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')

print("Conversion complete.")
