from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.geometry('900x700')
load = Image.open('1037.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root,image =render)
img.place(x=0,y=0)


def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("FAQ")
    newWindow.geometry("400x400")
    Label(newWindow, text ="This is FAQ \n What should be clicked to start recording my live audio? \n "
    "-Please click on the mic button\n\n\n\nAvaialble commands\nTug alpha can you red me?").pack()

def openNewWindow1():
    newWindow1 = Toplevel(root)
    newWindow1.title("File Browser")
    newWindow1.geometry("400x400")
    Label(newWindow1, text ="Please insert your pre-recorded audio here \n  \n ").pack()
    filepath = filedialog.askopenfilename()
    botton11 = Button(newWindow1, text = "open",command = filepath)
    #button.pack()
    #window.mainloop()
    filepath = filedialog.askopenfilename()
    #button101 = Button(text = "open")#,command=openfile)

#FAQ Button
img1 = PhotoImage(file = 'button.png')
button1 = Button(root,image = img1,border=100,command = openNewWindow)
button1.place(x=680, y=630)


#Chat Log
img2 = PhotoImage(file = 'chatlog.png')
button2 = Button(root,image = img2,border=0)
button2.place(x=100, y=10)


#record button
img3 = PhotoImage(file = 'record.png')
button3 = Button(root,image = img3,border=00)
button3.place(x=10, y=10)

#FIle Browser Icon
img4 = PhotoImage(file = 'folder.png')
button4 = Button(root,image = img4,border=00,command = openNewWindow1)
button4.place(x=10, y=630)

#logo but used as a button
img5 = PhotoImage(file = 'logo111.png')
button5 = Button(root,image = img5,bd=0)
button5.place(x=680, y=10)


root.mainloop()