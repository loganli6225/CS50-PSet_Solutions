import sys
from PIL import Image
from PIL import ImageOps
import os

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].lower().endswith(".jpg") and not sys.argv[1].lower().endswith(".jpeg") and not sys.argv[1].lower().endswith(".png"):
    sys.exit("Invalid input")
else:
    if not sys.argv[2].lower().endswith(".jpg") and not sys.argv[2].lower().endswith(".jpeg") and not sys.argv[2].lower().endswith(".png"):
        sys.exit("Invalid input")

# root1, extension1 = sys.argv[1].split(".")
# root2, extension2 = sys.argv[2].split(".")
# if extension1 != extension2:
#     sys.exit("Input and output have different extensions")

root1, extension1 = os.path.splitext(sys.argv[1])
root2, extension2 = os.path.splitext(sys.argv[2])
if extension1 != extension2:
    sys.exit("Input and output have different extensions")

try:
    Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt_image = Image.open("shirt.png")
image = Image.open(sys.argv[1])
size = shirt_image.size
image = ImageOps.fit(image, size)
image.paste(shirt_image, shirt_image)
image.save(sys.argv[2])
