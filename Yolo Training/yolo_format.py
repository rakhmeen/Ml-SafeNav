import json
import os

def convert_bbox_to_yolo(width, height, bbox):
    x1, y1 = bbox[0]['X'], bbox[0]['Y']
    x2, y2 = bbox[1]['X'], bbox[1]['Y']

    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    bbox_width = x2 - x1
    bbox_height = y2 - y1

    center_x /= width
    center_y /= height
    bbox_width /= width
    bbox_height /= height

    return center_x, center_y, bbox_width, bbox_height

def convert_json_to_yolo(json_file, img_width, img_height):
    with open(json_file, 'r') as f:
        data = json.load(f)

    objects = data.get('TrackedObj', [])
    yolo_labels = []

    class_id_map = {
        "Containership": 0,
        "sailboat": 2,
        "cruiseship": 3,
        "Fishing_Vassel": 1,
        "dingyboat":4,
        "tugboat":5,
        "Yacht":6

        
  
         
    }

    for obj in objects:
        class_name = obj['Alias']
        bbox = obj['BB2D']
        class_id = class_id_map.get(class_name, -1)

        if class_id != -1:
            center_x, center_y, width, height = convert_bbox_to_yolo(img_width, img_height, bbox)
            yolo_labels.append(f"{class_id} {center_x} {center_y} {width} {height}")

    return yolo_labels

def process_label_files(folder, img_width, img_height):
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            json_file = os.path.join(folder, filename)
            yolo_labels = convert_json_to_yolo(json_file, img_width, img_height)
            
          
            yolo_file = os.path.join(folder, filename.replace(".json", ".txt"))
            with open(yolo_file, 'w') as f:
                for label in yolo_labels:
                    f.write(label + '\n')

 
dataset_folder = 'dataset/labels/val'
image_width = 1280
image_height = 720
process_label_files(dataset_folder, image_width, image_height)
 

 
