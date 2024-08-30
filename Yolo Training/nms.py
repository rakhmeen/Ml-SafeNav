import os
import cv2
import numpy as np

def non_max_suppression(boxes, scores, iou_threshold):
    indices = cv2.dnn.NMSBoxes(
        bboxes=boxes,
        scores=scores,
        score_threshold=0.5,
        nms_threshold=iou_threshold
    )
    return indices.flatten()

def filter_small_boxes(boxes, area_threshold=0.01):
    filtered_boxes = []
    for box in boxes:
        x_min, y_min, x_max, y_max = box
        area = (x_max - x_min) * (y_max - y_min)
        if area >= area_threshold:
            filtered_boxes.append(box)
    return filtered_boxes

def process_labels(label_folder, image_folder, iou_threshold=0.4, area_threshold=0.01, image_size=640):
    for label_filename in os.listdir(label_folder):
        if label_filename.endswith('.txt'):
            label_path = os.path.join(label_folder, label_filename)
            image_path = os.path.join(image_folder, os.path.splitext(label_filename)[0] + '.png')  # or '.jpg'

            # Load image to draw bounding boxes
            image = cv2.imread(image_path)
            if image is None:
                continue
            image_height, image_width = image.shape[:2]

            # Read bounding box data
            with open(label_path, 'r') as file:
                lines = file.readlines()

            boxes = []
            scores = []
            for line in lines:
                class_id, center_x, center_y, width, height = map(float, line.split())
                x_min = int((center_x - width / 2) * image_width)
                y_min = int((center_y - height / 2) * image_height)
                x_max = int((center_x + width / 2) * image_width)
                y_max = int((center_y + height / 2) * image_height)

                boxes.append([x_min, y_min, x_max, y_max])
                scores.append(1.0)  # Assuming all boxes have equal confidence, replace with actual if available

             
            indices = non_max_suppression(boxes, scores, iou_threshold)
            boxes_after_nms = [boxes[i] for i in indices]

           
            filtered_boxes = filter_small_boxes(boxes_after_nms, area_threshold)

          
            with open(label_path, 'w') as file:
                for box in filtered_boxes:
                    x_min, y_min, x_max, y_max = box
                    center_x = ((x_min + x_max) / 2) / image_width
                    center_y = ((y_min + y_max) / 2) / image_height
                    width = (x_max - x_min) / image_width
                    height = (y_max - y_min) / image_height
                    file.write(f"0 {center_x} {center_y} {width} {height}\n")  # Assuming class_id = 0

            # # Optional: Draw and save the image with new bounding boxes
            # for box in filtered_boxes:
            #     x_min, y_min, x_max, y_max = box
            #     cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            # cv2.imwrite(f"output_{os.path.splitext(label_filename)[0]}.png", image)

label_folder = 'dataset/labels/test'
image_folder = 'dataset/images/test'
process_labels(label_folder, image_folder)
