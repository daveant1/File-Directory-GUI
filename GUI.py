import sys as sys
import os as os
import shutil as sh
import re as re
import PySimpleGUI as sg
from generate_layout import gen_layout
sys.path.insert(1, r'C:/')

#######Section with sprites and file setup
sg.theme('GreenMono')
folder_icon = os.path.join(r'C:\Desktop\Python\File_GUI\graphics', 'folder_icon.png')
file_icon = os.path.join(r'C:\Desktop\Python\File_GUI\graphics', 'file_icon.png')
dir = r'C:/'                  #Set directory name for testing
listdir = os.listdir(dir)

initial = [[sg.T('Welcome to the FileSystem Editor.\n'
        'Enter your name and press OK to continue.'), sg.InputText(key='__NAME__')],
        [sg.OK()],
        [sg.Exit()]]

window = sg.Window('Welcome Page', initial).Finalize()
win2_active = False
cursor = 0 #cursor is redefined as a different target/path based on what was last clicked on

while True:

    event1, value1 = window.read()
    if event1 in (None, 'Exit'):
        break

    if not win2_active and event1 == 'OK':
        win2_active = True
        window2 = sg.Window(dir, gen_layout(dir)).Finalize()
        window2.Maximize() #(maximizes window, require .finalize() on windows)

    while win2_active:
        event2, value2 = window2.read()
        if event2 == 'Back':
            win2_active = False
            window2.close()
        elif event2 in (None, 'Exit'):
            window2.close()
            window.close()
            sys.exit(0)
        elif event2[4:] in listdir:   ##event2[4:] because four newlines at beginning of event2 name
            newdir = os.path.join(dir, event2[4:])
            window3 = sg.Window(newdir, gen_layout(newdir)).Finalize()
            window3.Maximize()
            win3_active = True
            while win3_active:
                event3, value3 = window3.read()   ##CURRENT BUG: event3 Back and Exit buttons not being read
                if event3 == 'Back':
                    win3_active = False
                    window3.close()
                elif event3 in (None, 'Exit'):
                    window3.close()
                    window2.close()
                    window.close()
window.close()
