import os
 
image_folder = 'foggy and calm sea/images'
text_folder = 'foggy and calm sea/text'

 
image_files = os.listdir(image_folder)
text_files = os.listdir(text_folder)

 
image_ids = {os.path.splitext(file)[0].replace('foggy and calm sea', 'foggy and calm sea') for file in image_files}
text_ids = {os.path.splitext(file)[0] for file in text_files}

 
for image_file in image_files:
    image_id = os.path.splitext(image_file)[0].replace('foggy and calm sea', 'foggy and calm sea')
    if image_id not in text_ids:
        # os.remove(os.path.join(image_folder, image_file))
        print(f"Removed image file: {image_file}")

 
for text_file in text_files:
    text_id = os.path.splitext(text_file)[0]
    if text_id not in image_ids:
        # os.remove(os.path.join(text_folder, text_file))
        print(f"Removed text file: {text_file}")

print("File synchronization completed.")
