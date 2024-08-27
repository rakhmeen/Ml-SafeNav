import os
 
base_dir = "dataset"

 
image_base_dir = os.path.join(base_dir, "images")
label_base_dir = os.path.join(base_dir, "labels")

 
train_image_dir = os.path.join(image_base_dir, "train")
val_image_dir = os.path.join(image_base_dir, "val")
test_image_dir = os.path.join(image_base_dir, "test")

train_label_dir = os.path.join(label_base_dir, "train")
val_label_dir = os.path.join(label_base_dir, "val")
test_label_dir = os.path.join(label_base_dir, "test")

 
def count_files(dir_path, class_dirs):
    for class_dir in class_dirs:
        full_path = os.path.join(dir_path, class_dir)
        if os.path.exists(full_path):
            num_files = len(os.listdir(full_path))
            print(f"{num_files} files found in {full_path}")
        else:
            print(f"Directory {full_path} does not exist")
 
class_dirs = ["cloudy_and_medium_wave", "evening_calm", "evening_rain_calm_sea", "foggy_and_calm_sea"]

 
print("Counting images in train, val, and test directories:")
count_files(train_image_dir, class_dirs)
count_files(val_image_dir, class_dirs)
count_files(test_image_dir, class_dirs)

print("\nCounting labels in train, val, and test directories:")
count_files(train_label_dir, class_dirs)
count_files(val_label_dir, class_dirs)
count_files(test_label_dir, class_dirs)
