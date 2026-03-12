# pip install Pillow
import tkinter
from PIL import Image, ImageTk

main = tkinter.Tk()
img = Image.open("O'Reilly_logo.png")
tkimg = ImageTk.PhotoImage(img)
tkinter.Label(main, image=tkimg).pack()
main.mainloop()