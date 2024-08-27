import os
import shutil
from sklearn.model_selection import train_test_split

 
class_dirs = ["cloudy_and_medium_wave", "evening_calm", "evening_rain_calm_sea", "foggy_and_calm_sea"]
 
base_dir = "dataset"

 
image_base_dir = os.path.join(base_dir, "images")
label_base_dir = os.path.join(base_dir, "labels")

 
train_image_dir = os.path.join(image_base_dir, "train")
val_image_dir = os.path.join(image_base_dir, "val")
test_image_dir = os.path.join(image_base_dir, "test")

train_label_dir = os.path.join(label_base_dir, "train")
val_label_dir = os.path.join(label_base_dir, "val")
test_label_dir = os.path.join(label_base_dir, "test")

 
for sub_dir in [train_image_dir, val_image_dir, test_image_dir, train_label_dir, val_label_dir, test_label_dir]:
    for class_dir in class_dirs:
        os.makedirs(os.path.join(sub_dir, class_dir), exist_ok=True)
 
def move_files(files, src_dir, dst_dir):
    for file in files:
        src = os.path.join(src_dir, file)
        dst = os.path.join(dst_dir, file)
        shutil.move(src, dst)

 
for class_dir in class_dirs:
     
    current_image_dir = os.path.join(class_dir, "images")
    current_label_dir = os.path.join(class_dir, "text")

    
    images = os.listdir(current_image_dir)
    labels = os.listdir(current_label_dir)

  
    train_images, temp_images, train_labels, temp_labels = train_test_split(images, labels, test_size=0.2, random_state=42)
    val_images, test_images, val_labels, test_labels = train_test_split(temp_images, temp_labels, test_size=0.5, random_state=42)

    
    move_files(train_images, current_image_dir, os.path.join(train_image_dir, class_dir))
    move_files(val_images, current_image_dir, os.path.join(val_image_dir, class_dir))
    move_files(test_images, current_image_dir, os.path.join(test_image_dir, class_dir))

    move_files(train_labels, current_label_dir, os.path.join(train_label_dir, class_dir))
    move_files(val_labels, current_label_dir, os.path.join(val_label_dir, class_dir))
    move_files(test_labels, current_label_dir, os.path.join(test_label_dir, class_dir))

print("Dataset split and moved successfully!")
