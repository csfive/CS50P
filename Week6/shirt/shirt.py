from PIL import Image, ImageOps
import sys

if len(sys.argv) != 3:
    sys.exit("Invalid arguments.")

input = sys.argv[1]
output = sys.argv[2]
types = (".jpg", ".jpeg", ".png")
if (
    not input.endswith(types)
    or not output.endswith(types)
    or input.split(".")[1] != output.split(".")[1]
):
    sys.exit("Invalid arguments.")


shirt = Image.open("shirt.png")
try:
    with Image.open(input) as im:
        im = ImageOps.fit(im, shirt.size)
        im.paste(shirt, shirt)
        im.save(output)
except FileNotFoundError:
    sys.exit("File does not exist.")
