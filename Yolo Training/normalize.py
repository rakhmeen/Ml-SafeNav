import os

def clamp_and_normalize(center_x, center_y, width, height):
    # Clamp negative values to 0
    center_x = max(0, center_x)
    center_y = max(0, center_y)
    width = max(0, width)
    height = max(0, height)
    
    # Ensure values do not exceed 1 (normalized)
    center_x = min(1, center_x)
    center_y = min(1, center_y)
    width = min(1, width)
    height = min(1, height)
    
    return center_x, center_y, width, height

def process_bounding_boxes(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    new_lines = []
    for line in lines:
        data = line.strip().split()
        class_id = data[0]
        center_x, center_y, width, height = map(float, data[1:])
        
        # Clamp and normalize bounding box
        center_x, center_y, width, height = clamp_and_normalize(center_x, center_y, width, height)
        
        # Create a new line with the corrected values
        new_line = f"{class_id} {center_x:.6f} {center_y:.6f} {width:.6f} {height:.6f}\n"
        new_lines.append(new_line)
    
    # Write the new data back to the file
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

def process_all_txt_files_in_folder(folder_path):
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a .txt file
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            process_bounding_boxes(file_path)
            print(f"Processed {file_path}")

# Example usage for a folder
folder_path = "dataset/labels/val"  # Replace with the actual folder path
process_all_txt_files_in_folder(folder_path)
