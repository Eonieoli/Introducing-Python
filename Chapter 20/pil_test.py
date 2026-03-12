# pip install Pillow
from PIL import Image

img = Image.open("O'Reilly_logo.png")
print(img.format)
print(img.size)
print(img.mode)
img.show()

crop = (55, 70, 85, 100)
img2 = img.crip(crop)
img2.show()

img2.save('cropped.gif', 'GIF')
img3 = Image.open('cropped.gif')
print(img3.format)
img3.size(30, 30)