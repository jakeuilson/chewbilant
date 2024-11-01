import urllib
from rembg import remove
from PIL import Image

fileimg = url_to_image("https://pixabay.com/photos/cat-pet-animal-feline-kitten-9165952/")
input_path = fileimg

# Don't try to output to JPG, most convenient file format with an alpha channel is PNG
output_path = 'result.png'

input = Image.open(input_path)
output = remove(input)

output.save(output_path)
