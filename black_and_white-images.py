from PIL import Image

# Upload Image #
image_file = Image.open(r"colorida.png")

# Convert Image to Black and White #
image_file = image_file.convert('L')

# Save image in black and white #
image_file.save(r"black-and-white.png")
