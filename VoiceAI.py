from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('900x700')
load = Image.open('ship101.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root,image =render)
img.place(x=0,y=0)

"""FAQ Button"""
img1 = PhotoImage(file = 'FAQ.png')
button1 = Button(root,image = img1,border=0)
button1.place(x=750, y=630)


"""Chat Log"""
img2 = PhotoImage(file = 'button.png')
button2 = Button(root,image = img2,border=0)
button2.place(x=100, y=10)


"""record button"""
img3 = PhotoImage(file = 'micIcon.png')
button3 = Button(root,image = img3,border=00,)
button3.place(x=10, y=10)

"""FIle Browser"""
img4 = PhotoImage(file = 'file.png')
button4 = Button(root,image = img4,border=00,)
button4.place(x=10, y=630)

img5 = PhotoImage(file = 'pivot-logo.png')
button5 = Button(root,image = img5,bd=0,)
button5.place(x=520, y=10)
root.mainloop()




