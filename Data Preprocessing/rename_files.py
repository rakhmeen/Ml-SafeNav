import os

 
folder_path = 'cloudy and medium wave/text'

# Iterate through all the files in the folder
for filename in os.listdir(folder_path):
    if "RawMeta" in filename:
        # Replace "CamFeed" with "cloudy_and_medium_wave"
        new_filename = filename.replace("RawMeta", "cloudy_and_medium_wave")
        
        
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
      
        os.rename(old_file, new_file)

print("Files renamed successfully!")
