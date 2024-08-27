import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Load the image
image_path = 'dataset/images/train/0_evening_rain_calm_sea_97.png'
image = Image.open(image_path)

# Load the corresponding label file

label_path = 'dataset/labels/train/0_evening_rain_calm_sea_97.txt'

# Read the labels from the SSD formatted .txt file
with open(label_path, 'r') as f:
    labels = f.readlines()

# Create a plot
fig, ax = plt.subplots(1)
ax.imshow(image)

# Define the class names
class_names = ["Containership", "Fishing_Vassel", "sailboat", "cruiseship", "dingyboat", "tugboat", "Yacht"]

# Image dimensions (for scaling the bounding boxes back to original size)
image_width, image_height = 640,640

# Iterate over each bounding box and plot it
for label in labels:
    parts = label.strip().split()
    class_id = int(parts[0])
    xmin = float(parts[1]) * image_width
    ymin = float(parts[2]) * image_height
    xmax = float(parts[3]) * image_width
    ymax = float(parts[4]) * image_height
    
    # Create a rectangle patch for the bounding box
    rect = patches.Rectangle(
        (xmin, ymin), xmax - xmin, ymax - ymin, 
        linewidth=2, edgecolor='r', facecolor='none'
    )
    
    # Add the bounding box to the plot
    ax.add_patch(rect)
    
    # Add the class label above the bounding box
    plt.text(xmin, ymin, class_names[class_id], color='white', fontsize=12, backgroundcolor='red')

# Show the plot
plt.show()
