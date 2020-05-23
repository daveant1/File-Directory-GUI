import sys as sys
import os as os
import shutil as sh
import re as re
import PySimpleGUI as sg
#from gen_layout import *
from file_functions import *

prog_dir = os.getcwd() #program directory (location of GUI.py and other main files)

#######Section with sprites and file setup##########
sg.theme('GreenMono')
init_dir = r'C:/'                  #Set inital directory name for testing

initial = [[sg.T('Welcome to the FileSystem Editor.\n'
        'Enter your name and press OK to continue.'), sg.InputText(key='__NAME__')],
        [sg.OK()],
        [sg.Exit()]]

start = sg.Window('Welcome Page', initial).Finalize()

########Starting Screen (input name)#########
while True:
    event1, value1 = start.read()

    if event1 in (None, 'Exit'):
        start.close()
        sys.exit(0)

    if event1 == 'OK':
        if(re.search(r'\W+', value1['__NAME__']) == None):
            username = value1['__NAME__']              #sets user's name for program
        else:
            gen_error(1)
            continue
        listdir = os.listdir(init_dir)
        curr_dir = init_dir
        prevpath = init_dir
        new_window = gen_window(start, init_dir, listdir)
        new_window.Maximize()               #maximizes window, requires .Finalize() on window
        break

###Phase that the program spends majority of time in (default new window view)###
while True:
        new_event, new_value = new_window.read()
        if new_event in (None, 'Exit'):
            new_window.close()
            sys.exit(0)

        elif new_event == 'Back':
            if curr_dir==init_dir:  #generate error window and poll for 'Close' button using gen_error function
                gen_error(0)   #Type 0 error
                continue
            listdir = os.listdir(prevpath)           #update listdir to previous directory
            curr_dir = prevpath
            prevpath = os.path.dirname(curr_dir)
            new_window = gen_window(new_window, curr_dir, listdir)
            new_window.Maximize()

        elif new_event[4:] in listdir:
            prevpath = curr_dir
            curr_dir = os.path.join(curr_dir, new_event[4:])
            if os.path.isdir(curr_dir):
                listdir = os.listdir(curr_dir)
            new_window = gen_window(new_window, curr_dir, listdir)
            new_window.Maximize()
            if os.path.isfile(curr_dir):
                curr_dir = os.path.dirname(curr_dir)
                prevpath = os.path.dirname(curr_dir)

        elif new_event == 'Next Page':
            new_window = gen_window(new_window, curr_dir, listdir[40:])
            new_window.Maximize()

        elif new_event == 'New Folder':
            listdir = gen_new(curr_dir,1)  #calls new directory generation function (refreshes list directory)
            new_window = gen_window(new_window, curr_dir, listdir)
            new_window.Maximize()

        elif new_event == 'New File':
            listdir = gen_new(curr_dir,0)
            new_window = gen_window(new_window, curr_dir, listdir)
            new_window.Maximize()
