import ast
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Function to plot bounding boxes and class names on an image
def plot_bounding_boxes(image_path, data):
    # Load the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Optionally, you can specify a font for the class names
    try:
        font = ImageFont.truetype("arial.ttf", 20)  # Change to a font available on your system
    except IOError:
        font = ImageFont.load_default()

    # Loop through each tracked object and draw bounding boxes and labels
    for obj in data.get("TrackedObj", []):
        bbox = obj.get("BB2D", [])
        if len(bbox) == 2:  # Ensure bounding box has two points
            x1, y1 = bbox[0]["X"], bbox[0]["Y"]
            x2, y2 = bbox[1]["X"], bbox[1]["Y"]
            draw.rectangle([x1, y1, x2, y2], outline="red", width=2)  # Draw rectangle

            # Draw the class name
            class_name = obj.get("Alias", "Unknown")
            text_position = (x1, y1 - 20)  # Position the text above the bounding box
            draw.text(text_position, class_name, fill="red", font=font)  # Draw text

    # Display the image with bounding boxes and class names
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# Path to the text file containing JSON data
file_path = 'dataset/labels/test/0_cloudy_and_medium_wave_7.txt'

# Load the JSON data from the file
with open(file_path, 'r') as file:
    json_string = file.read().strip()

# Convert the JSON string to a dictionary
data = ast.literal_eval(json_string)

# Path to the image file (adjust path according to your setup)
image_path = 'dataset/images/test/0_cloudy_and_medium_wave_7.png'
 
plot_bounding_boxes(image_path, data)
