import sys
from PIL import Image

images = []

# for arg in sys.argv:
#     image = Image.open(arg)
#     images.append(image)
for i in range(1,8):
    image = Image.open(f"gifs/021_0{i}.gif")
    images.append(image)

images

images[0].save(
    "animation.gif", save_all=True, append_images=images[1:], diration=200, loop=0
)