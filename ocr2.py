# import the following libraries
# will convert the image to text string
# https://github.com/UB-Mannheim/tesseract/wiki install Tesseract

import pytesseract

# adds image processing capabilities
from PIL import Image

# opening an image from the source path
img = Image.open('images/num.jpeg')

# describes image format in the output
print(img)

# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)

# write text in a text file and save it to source path
with open('imagetotext.txt', mode='w') as file:
    file.write(result)
    print(result)