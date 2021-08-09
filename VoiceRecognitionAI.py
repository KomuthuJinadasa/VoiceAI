import tkinter 
from tkinter import Label, PhotoImage, Tk
from tkinter.constants import LEFT
import PySimpleGUI as sg




layout = [[sg.Button(image_filename="record1.png", image_size = (55, 55), image_subsample=2, border_width=0, button_color=(sg.theme_background_color())),
           sg.Button('Conversation \nLog', button_color = 'blue', size = (10,3), border_width=3),
           sg.Button(image_filename="file-browser-icon-23.jpeg", image_size = (55, 55), image_subsample=2, border_width=0, button_color=(sg.theme_background_color())),
           sg.Button( 'FAQ', button_color = 'red',size = (10,3), border_width=3,)]]
        
window = sg.Window('Voice AI Regconigtion', layout, size=(900,700))

while True:
    event, value = window.read()
    event = sg.WINDOW_CLOSED
    break

window.close()




