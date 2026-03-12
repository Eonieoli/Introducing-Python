# pip install Wand
from wand.image import Image
from wand.display import display

img = Image(filename="O'Reilly_logo.png")
img.size(154, 141)
print(img.format)
display(img)