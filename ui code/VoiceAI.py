from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('900x700')
load = Image.open('1037.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root,image =render)
img.place(x=0,y=0)

"""FAQ Button"""
img1 = PhotoImage(file = 'button.png')
button1 = Button(root,image = img1,border=100)
button1.place(x=750, y=630)


"""Chat Log"""
img2 = PhotoImage(file = 'chatlog.png')
button2 = Button(root,image = img2,border=0)
button2.place(x=100, y=10)


"""record button"""
img3 = PhotoImage(file = 'record.png')
button3 = Button(root,image = img3,border=00,)
button3.place(x=10, y=10)

"""FIle Browser"""
img4 = PhotoImage(file = 'folder.png')
button4 = Button(root,image = img4,border=00,)
button4.place(x=10, y=630)

""""logo but used as a button"""
img5 = PhotoImage(file = 'logo111.png')
button5 = Button(root,image = img5,bd=0,)
button5.place(x=680, y=10)
root.mainloop()




