import json
import os

 
image_width = 1280
image_height = 720

 
class_map = {
    "Containership": 0,
    "Fishing_Vassel": 1,
    "sailboat": 2,
    "cruiseship": 3,
    "dingyboat": 4,
    "tugboat": 5,
    "Yacht": 6
}

def convert_to_ssd_format(txt_file, output_file):
    with open(txt_file, 'r') as f:
        data = json.load(f)  # Load the JSON content from the .txt file
    
    with open(output_file, 'w') as f:
        for obj in data.get("TrackedObj", []):
            alias = obj["Alias"]
            class_id = class_map.get(alias, -1)
            if class_id == -1:
                continue  # Skip if alias not in class_map

            # Extract and normalize bounding box coordinates
            X1 = obj["BB2D"][0]["X"]
            Y1 = obj["BB2D"][0]["Y"]
            X2 = obj["BB2D"][1]["X"]
            Y2 = obj["BB2D"][1]["Y"]

            xmin = (X1 ) / image_width
            ymin = (Y1 ) / image_height
            xmax = (X2 ) / image_width
            ymax = (Y2 ) / image_height

            # Write the normalized coordinates to the output file
            f.write(f"{class_id} {xmin:.6f} {ymin:.6f} {xmax:.6f} {ymax:.6f}\n")

def process_directory(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    for folder in ['train', 'val', 'test']:
        folder_input_dir = os.path.join(input_dir, folder)
        folder_output_dir = os.path.join(output_dir, folder)
        os.makedirs(folder_output_dir, exist_ok=True)

        for txt_file in os.listdir(folder_input_dir):
            if txt_file.endswith('.txt'):
                input_path = os.path.join(folder_input_dir, txt_file)
                output_path = os.path.join(folder_output_dir, txt_file)  # Output file retains .txt extension
                convert_to_ssd_format(input_path, output_path)

 
input_dir = 'dataset/labels'  # Update this with your actual labels directory
output_dir = 'dataset/ssd_labels'  # Where you want to save the converted labels

 
process_directory(input_dir, output_dir)

print("Label conversion complete!")
