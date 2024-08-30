import json
import ast
from PIL import Image, ImageDraw, ImageFont

with open('cloudy and medium wave/text/0_RawMeta_120.txt', 'r') as file:
    json_string = file.read().strip()

 
json_string = ast.literal_eval(json_string)

data = json.loads(json_string)

image = Image.open('cloudy and medium wave/images/0_CamFeed_120.png')
width, height = image.size

draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

 
for obj in data['TrackedObj']:
    alias = obj['Alias']
    bb = obj['BB2D']
    
    
    x1 = max(0, min(width - 1, bb[0]['X']))
    y1 = max(0, min(height - 1, bb[0]['Y']))
    x2 = max(0, min(width - 1, bb[1]['X']))
    y2 = max(0, min(height - 1, bb[1]['Y']))
    
   
    draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
    
     
    label = alias
    label_bbox = draw.textbbox((x1, y1), label, font=font)
    label_width = label_bbox[2] - label_bbox[0]
    label_height = label_bbox[3] - label_bbox[1]
    
    draw.rectangle([x1, y1 - label_height - 4, x1 + label_width, y1], fill="red")
    draw.text((x1, y1 - label_height - 2), label, font=font, fill="white")

 
image.save('output_image.jpg')
print(f"Image saved as 'output_image.jpg'. Image size: {width}x{height}")
