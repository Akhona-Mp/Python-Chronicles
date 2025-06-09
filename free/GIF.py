import sys

"""
Takes in a comandline prompt with two arguments,that being the name of the
files with the images that will be used.
"""

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.git",save_all=True, append_images=[images[1]], duration=200,loop=0
)