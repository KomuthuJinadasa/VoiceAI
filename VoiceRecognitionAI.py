import PySimpleGUI as sg

sg.theme('LightGreen')

layout = [[sg.Button(image_filename="micIcon.png", image_size = (55, 55), image_subsample=5, border_width=0, button_color=(sg.theme_background_color())),
           sg.Button('Conversation \nLog', button_color = 'blue', size = (10,3), border_width=3)]

]

window = sg.Window('Voice AI Regconigtion', layout, size=(900,700))

while True:
    event, value = window.read()
    event = sg.WINDOW_CLOSED
    break

window.close()

