import cv2
import os

def resize_image_and_bboxes(image, bboxes, target_size):
    original_height, original_width = image.shape[:2]

    
    if original_width > original_height:
        scale = target_size / original_width
        new_width = target_size
        new_height = int(original_height * scale)
        pad_y = (target_size - new_height) // 2
        pad_x = 0
    else:
        scale = target_size / original_height
        new_height = target_size
        new_width = int(original_width * scale)
        pad_x = (target_size - new_width) // 2
        pad_y = 0
 
    resized_image = cv2.resize(image, (new_width, new_height))
    
 
    squared_image = cv2.copyMakeBorder(
        resized_image, pad_y, pad_y, pad_x, pad_x,
        borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0)
    )

  
    adjusted_bboxes = []
    for bbox in bboxes:
        class_id, center_x, center_y, width, height = bbox

       
        new_center_x = (center_x * new_width + pad_x) / target_size
        new_center_y = (center_y * new_height + pad_y) / target_size
        new_width_bbox = (width * new_width) / target_size
        new_height_bbox = (height * new_height) / target_size

        adjusted_bboxes.append([class_id, new_center_x, new_center_y, new_width_bbox, new_height_bbox])
    
    return squared_image, adjusted_bboxes

 
image_folder = 'dataset/images/test'
label_folder = 'dataset/labels/test'
target_size = 640  # Target size for square images
 
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Adjust this if you have different image extensions
        image_path = os.path.join(image_folder, filename)
        label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + '.txt')

        
        image = cv2.imread(image_path)

       
        with open(label_path, 'r') as file:
            lines = file.readlines()
            bboxes = [list(map(float, line.split())) for line in lines]

      
        resized_image, adjusted_bboxes = resize_image_and_bboxes(image, bboxes, target_size)

      
        cv2.imwrite(image_path, resized_image)

 
        with open(label_path, 'w') as file:
            for bbox in adjusted_bboxes:
                file.write(' '.join(map(str, bbox)) + '\n')

print("Resizing and bounding box adjustment for all images complete.")

# image=cv2.imread('dataset/images/train/evening_calm36.png')
# import cv2
# import matplotlib.pyplot as plt

# # Load the image
# # image = cv2.imread('/content/resized_image.jpg')
# image_height=640
# image_width=640

# # Read the bounding box data from the .txt file
# with open('dataset/labels/train/evening_calm36.txt', 'r') as file:
#     lines = file.readlines()

# for line in lines:
#     class_id, center_x, center_y, width, height = map(float, line.split())

#     # Convert normalized coordinates to pixel values
#     x_min = int((center_x - width / 2) * image_width)
#     y_min = int((center_y - height / 2) * image_height)
#     x_max = int((center_x + width / 2) * image_width)
#     y_max = int((center_y + height / 2) * image_height)

#     # Draw the bounding box on the image
#     cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

# # Convert BGR to RGB (since OpenCV loads images in BGR format)
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Display the image with bounding boxes
# plt.imshow(image_rgb)
# plt.axis('off')
# plt.show()
