import cv2
import os
import matplotlib.pyplot as plt

 
image_folder = 'dataset/images/val'
label_folder = 'dataset/labels/val'

 
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Adjust this for your image extensions
        image_path = os.path.join(image_folder, filename)
        label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + '.txt')

       
        image = cv2.imread(image_path)
        image_height, image_width = image.shape[:2]
 
        if os.path.exists(label_path):
            with open(label_path, 'r') as file:
                lines = file.readlines()

            for line in lines:
                class_id, center_x, center_y, width, height = map(float, line.split())

                # Convert normalized coordinates to pixel values
                x_min = int((center_x - width / 2) * image_width)
                y_min = int((center_y - height / 2) * image_height)
                x_max = int((center_x + width / 2) * image_width)
                y_max = int((center_y + height / 2) * image_height)

                
                cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

           
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
            plt.figure(figsize=(8, 8))
            plt.imshow(image_rgb)
            plt.title(f"Image: {filename}")
            plt.axis('off')
            plt.show()
        else:
            print(f"No label file found for {filename}")
