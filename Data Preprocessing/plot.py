import ast
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

 
def plot_bounding_boxes(image_path, data):
    # Load the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

   
    try:
        font = ImageFont.truetype("arial.ttf", 20)  # Change to a font available on your system
    except IOError:
        font = ImageFont.load_default()
 
    for obj in data.get("TrackedObj", []):
        bbox = obj.get("BB2D", [])
        if len(bbox) == 2:  # Ensure bounding box has two points
            x1, y1 = bbox[0]["X"], bbox[0]["Y"]
            x2, y2 = bbox[1]["X"], bbox[1]["Y"]
            draw.rectangle([x1, y1, x2, y2], outline="red", width=2)  # Draw rectangle

        
            class_name = obj.get("Alias", "Unknown")
            text_position = (x1, y1 - 20)  # Position the text above the bounding box
            draw.text(text_position, class_name, fill="red", font=font)  # Draw text

   
    plt.imshow(image)
    plt.axis('off')
    plt.show()

 
file_path = 'dataset/labels/test/0_cloudy_and_medium_wave_7.txt'

 
with open(file_path, 'r') as file:
    json_string = file.read().strip()

 
data = ast.literal_eval(json_string)

 
image_path = 'dataset/images/test/0_cloudy_and_medium_wave_7.png'
 
plot_bounding_boxes(image_path, data)
