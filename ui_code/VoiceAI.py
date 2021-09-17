from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.geometry('900x700')
load = Image.open('ui_code/bg.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root,image =render)
img.place(x=0,y=0)


def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("FAQ")
    newWindow.geometry("400x400")
    Label(newWindow, text ="This is FAQ \n What should be clicked to start recording my live audio? \n "
    "-Please click on the mic button\n\n\n\nAvaialble commands\n[Tug Name], pull/push* [Power Amount]\n"
    "[Tug Name], pull directly* astern\n[Tug Name], all stop\n[Tug Name], move to pull/push - [Tug Name], be ready to pull/push\n"
    "[Tug Name], move to [Position]\n[Tug Name], square up\n\n<Tug Name>'s\nTug Alpha, Bravo, Charlie\nTug 1,2,3\nTug A,B,C\n\n"
    "<Position>\nAft, Fore, Port, Starboard, Port Quarter, Starboard Quarter\n\n<Power Amount>\n5%, 10%, 25%, 50%, 75%, 100%\nminimum, minimum Weight, Bare Weight\n"
    "Quarter Power*, Half Power*, Three Quarters Power*, Full Power*").pack()

def filepath():
    filepath = filedialog.askopenfilename(title="open file",filetypes=(("Insert mp3 files only!!","*.mp3") ,("text files","*.txt")))
    file = open(filepath)
    print(filepath)
    file.close()

def func():
    top = Toplevel()
    top.title('File browser')
    top.geometry("600x400")
    load1 = Image.open('ui_code/w1.png')
    render1 = ImageTk.PhotoImage(load1)
    img11 = Label(top,image =render1)
    img11.place(x=0,y=0) 
    img7 = PhotoImage(file = 'ui_code/button.w.png')
    button7 = Button(top,image=img7,command =filepath)
    button7.pack(pady=10)
    button7.place(x=250, y=100)
    Label(top, text ="Please insert your pre-recorded audio here").pack()
    Label.place(x=100,y=100)

#FAQ Button
img1 = PhotoImage(file = 'ui_code/button.png')
button1 = Button(root,image = img1,border=100,command = openNewWindow)
button1.place(x=680, y=630)


#Chat Log
img2 = PhotoImage(file = 'ui_code/chatlog.png')
button2 = Button(root,image = img2,border=0)
button2.place(x=100, y=10)


#record button
img3 = PhotoImage(file = 'ui_code/record.png')
button3 = Button(root,image = img3,border=00)
button3.place(x=10, y=10)

#FIle Browser Icon
img4 = PhotoImage(file = 'ui_code/folder.png')
button4 = Button(root,image = img4,border=00,command = func)
button4.place(x=10, y=630)

#logo but used as a button
img5 = PhotoImage(file = 'ui_code/logo111.png')
button5 = Button(root,image = img5,bd=0)
button5.place(x=680, y=10)


root.mainloop()