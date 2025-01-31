from PIL import Image
from pathlib import Path


ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER/'violet.png'
RESIZED_IMAGE = ROOT_FOLDER/'new.jpg'

p_image = Image.open(ORIGINAL)
width, height = p_image.size
new_width = 1980
new_height = round(height * new_width / width)

new_image = p_image.resize(size=(new_width, new_height))
new_image.save(
    RESIZED_IMAGE,
    optimize=True,
    quality=70,
    exit=exit,
)


