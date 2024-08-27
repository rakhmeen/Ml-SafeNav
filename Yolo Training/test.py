from PIL import Image
import os

image_dir = 'dataset/images/train'
sizes = []

for img_file in os.listdir(image_dir):
    with Image.open(os.path.join(image_dir, img_file)) as img:
        sizes.append(img.size)

# Calculate average image size
avg_width = sum(size[0] for size in sizes) / len(sizes)
avg_height = sum(size[1] for size in sizes) / len(sizes)

print(f"Average image size: {avg_width}x{avg_height}")


 
