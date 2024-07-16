# Importing the necessary libraries
from PIL import Image

# Opening an image using PIL (Python Imaging Library)
image = Image.open("example.jpg")

# Opening a file in binary write mode
with open("output.txt", "wb") as output_file:
    # Writing the height of the image to the file
    output_file.write(f"HEIGHT {image.height}\n".encode())
