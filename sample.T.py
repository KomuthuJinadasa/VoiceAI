import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, height=300,width= 500)
canvas.pack()

frame = tk.Frame(root, bg='light green')
frame.place(relwidth=1, relheight=0.10)

button = tk.Button(root, text="Test Button", bg='red', fg='purple' )
button.pack()

root.mainloop()
