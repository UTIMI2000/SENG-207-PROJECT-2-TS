import PySimpleGUI as sg
import pyttsx3

engine_main = pyttsx3.init()
voice_type= engine_main.getProperty('voices')



layout = [    [sg.Text('Select the type of voice:',text_color='red',background_color='yellow'),sg.Radio('Male', 'RADIO1', default=True, key='male',background_color='orange'),sg.Radio('Female', 'RADIO1', key='Female',background_color='yellow')],
     [sg.Text('Enter text to speak:',text_color='red',background_color='yellow',)],
          
    [sg.InputText(key='userinput'),sg.Button('Speak',button_color='black')],
   
    
]

window = sg.Window('UTIMI ', layout,background_color='white')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['userinput']
        if values['male']:
            engine_main.setProperty('voice', voice_type[0].id)
        elif values['Female']:
             engine_main.setProperty('voice', voice_type[1].id) 
    
        engine_main.say(text)
        engine_main.runAndWait()

window.close()