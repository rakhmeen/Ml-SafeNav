import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
source_folder = 'foggy and calm sea'
image_folder = os.path.join(source_folder, 'images')
label_folder = os.path.join(source_folder, 'text')

# Destination folders
dest_folders = {
    'train': 'train',
    'val': 'val',
    'test': 'test'
}

# Create destination directories if they don't exist
for folder in dest_folders.values():
    os.makedirs(os.path.join(folder, 'images'), exist_ok=True)
    os.makedirs(os.path.join(folder, 'labels'), exist_ok=True)

# Get list of images and corresponding labels
images = [f for f in os.listdir(image_folder) if f.endswith('.png')]
labels = [f.replace('.png', '.txt') for f in images]
 
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.3, random_state=42)
val_images, test_images, val_labels, test_labels = train_test_split(test_images, test_labels, test_size=0.33, random_state=42)  # 0.33 * 0.3 = 0.1

 
def move_files(file_list, src_folder, dest_folder):
    for file_name in file_list:
        shutil.move(os.path.join(src_folder, file_name), os.path.join(dest_folder, file_name))

 
move_files(train_images, image_folder, os.path.join(dest_folders['train'], 'images'))
move_files(train_labels, label_folder, os.path.join(dest_folders['train'], 'labels'))

move_files(val_images, image_folder, os.path.join(dest_folders['val'], 'images'))
move_files(val_labels, label_folder, os.path.join(dest_folders['val'], 'labels'))

move_files(test_images, image_folder, os.path.join(dest_folders['test'], 'images'))
move_files(test_labels, label_folder, os.path.join(dest_folders['test'], 'labels'))

print("Dataset split completed.")
