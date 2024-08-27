import os
import shutil

# Paths to the original folders
original_folders = {
    'train': {'images': 'train/images', 'labels': 'train/labels'},
    'test': {'images': 'test/images', 'labels': 'test/labels'},
    'val': {'images': 'val/images', 'labels': 'val/labels'}
}

# Paths to the new dataset structure
new_structure = {
    'train': {'images': 'dataset/images/train', 'labels': 'dataset/labels/train'},
    'test': {'images': 'dataset/images/test', 'labels': 'dataset/labels/test'},
    'val': {'images': 'dataset/images/val', 'labels': 'dataset/labels/val'}
}

# Ensure the new directories exist
for key in new_structure:
    os.makedirs(new_structure[key]['images'], exist_ok=True)
    os.makedirs(new_structure[key]['labels'], exist_ok=True)

# Move the files
for key in original_folders:
    for folder_type in ['images', 'labels']:
        src_folder = original_folders[key][folder_type]
        dest_folder = new_structure[key][folder_type]
        
        for filename in os.listdir(src_folder):
            src_file = os.path.join(src_folder, filename)
            dest_file = os.path.join(dest_folder, filename)
            
            if os.path.isfile(src_file):
                shutil.move(src_file, dest_file)

print("Files have been moved successfully.")
