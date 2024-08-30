import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

 
image_path = 'dataset/images/train/0_evening_rain_calm_sea_97.png'
image = Image.open(image_path)

 

label_path = 'dataset/labels/train/0_evening_rain_calm_sea_97.txt'

 
with open(label_path, 'r') as f:
    labels = f.readlines()

 
fig, ax = plt.subplots(1)
ax.imshow(image)

 
class_names = ["Containership", "Fishing_Vassel", "sailboat", "cruiseship", "dingyboat", "tugboat", "Yacht"]

 
image_width, image_height = 640,640

 
for label in labels:
    parts = label.strip().split()
    class_id = int(parts[0])
    xmin = float(parts[1]) * image_width
    ymin = float(parts[2]) * image_height
    xmax = float(parts[3]) * image_width
    ymax = float(parts[4]) * image_height
    
 
    rect = patches.Rectangle(
        (xmin, ymin), xmax - xmin, ymax - ymin, 
        linewidth=2, edgecolor='r', facecolor='none'
    )
    
   
    ax.add_patch(rect)
    
    plt.text(xmin, ymin, class_names[class_id], color='white', fontsize=12, backgroundcolor='red')

 
plt.show()
