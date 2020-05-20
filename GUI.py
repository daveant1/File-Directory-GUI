import sys as sys
import os as os
import shutil as sh
import re as re
import PySimpleGUI as sg
from generate_layout import main_page
sys.path.insert(1, r'C:/')

#######Section with sprites and file setup
sg.theme('GreenMono')
folder_icon = os.path.join(r'C:\Users\dopal\Desktop\Projects\File-Directory-GUI\graphics', 'folder_icon.png')
file_icon = os.path.join(r'C:\Users\dopal\Desktop\Projects\File-Directory-GUI\graphics', 'file_icon.png')
init_dir = r'C:/'                  #Set inital directory name for testing
listdir = os.listdir(init_dir)      #List of files/directories within current directory

initial = [[sg.T('Welcome to the FileSystem Editor.\n'
        'Enter your name and press OK to continue.'), sg.InputText(key='__NAME__')],
        [sg.OK()],
        [sg.Exit()]]

window = sg.Window('Welcome Page', initial).Finalize()
win2_active = False
new_active = False
cursor = 0 #cursor is redefined as a different target/path based on what was last clicked on

while True:

    event1, value1 = window.read()
    user_name = value1['__NAME__']              ##sets user's name for program

    if event1 in (None, 'Exit'):
        window.close()
        sys.exit(0)

    if not win2_active and event1 == 'OK':
        win2_active = True
        window2 = sg.Window(init_dir, main_page(init_dir).page).Finalize()
        window2.Maximize() #(maximizes window, require .finalize() on windows)

     ##window2 is our initial file directory interface, which goes to new_active loop to generate new windows
    while win2_active:
        event2, value2 = window2.read()

        if event2 == 'Back':
            win2_active = False
            window2.close()

        elif event2 in (None, 'Exit'):
            window2.close()
            window.close()
            sys.exit(0)

        elif event2[4:] in listdir:   ##event2[4:] because four newlines at beginning of event2 name (goes to open new window loop)
            newdir = os.path.join(init_dir, event2[4:])
            if os.path.isdir(newdir):
                listdir = os.listdir(newdir)    ##Update directory list for current directory
                window.close()
                window2.close()                 ##Close window2 and set flag false
                win2_active = False
                newpage = main_page(newdir)
                new_window = sg.Window(newdir, newpage.page).Finalize()   ##Open new window and set new flag true
                new_window.Maximize()
                new_active = True
            else:
                os.system("start " + newdir)          ##Start the file
                newdir = os.path.dirname(newdir)      ##Reset path to directory minus the filename

    while new_active:
                new_event, new_value = new_window.read()

                if new_event == 'Back':
                    newdir = os.path.dirname(newdir)      ##Reset directory to previous path
                    prevdir = newdir
                    listdir = os.listdir(prevdir)           ##update listdir to previous directory
                    new_window.close()
                    newpage = main_page(prevdir)
                    new_window = sg.Window(prevdir, newpage.page).Finalize()
                    new_window.Maximize()

                elif new_event[4:] in listdir:
                    newdir = os.path.join(newdir, new_event[4:])
                    if os.path.isdir(newdir):
                        listdir = os.listdir(newdir)            ##update listdir to new relevant directory
                        new_window.close()
                        new_window = sg.Window(newdir, main_page(newdir).page).Finalize()
                        new_window.Maximize()
                    else:
                        os.system("start " + newdir)          ##Start the file
                        newdir = os.path.dirname(newdir)      ##Reset path to directory minus the filename

                elif new_event in (None, 'Exit'):
                    new_window.close()
                    sys.exit(0)
