import sys as sys
import os as os
import shutil as sh
import re as re
import PySimpleGUI as sg
folder_icon = os.path.join(r'C:\Users\dopal\Desktop\Python\File_GUI\graphics', 'folder_icon.png')
file_icon = os.path.join(r'C:\Users\dopal\Desktop\Python\File_GUI\graphics', 'file_icon.png')

##Screen size is 5x8 icons
def gen_layout(dir):
    listdir = os.listdir(dir)       ##Generate list of filenames/dirs for current directory
    if len(listdir) > 40:
        print('Error! Too many files/directories to display at this time!')
        sys.exit(0)
    dir_layout = []    ##empty output layout
    icon_count = 0     ##int to count number of icons printed
    element = []       ##element (empty list)
    for name in sorted(listdir, key=str.lower):  ##sort directory list, ignore casing
            path = os.path.join(dir, name)
            if os.path.isdir(path) and icon_count < 8:         ##Check if path of current object is a folder or file
                element.append(sg.Button('\n\n\n\n'+ name, image_filename = folder_icon, image_size = (160,160)))   ##append another button to the element (row)
                icon_count = icon_count + 1
            elif os.path.isfile(path) and icon_count < 8:
                element.append(sg.Button('\n\n\n\n' + name, button_color = ('black', 'white'), image_filename = file_icon, image_size = (160,160)))     ##append another button to the element (row)
                icon_count = icon_count + 1
            else:
                dir_layout.append(element)      ##complete element added to directory layout
                icon_count = 0                  ##reset variables
                element = []

    dir_layout.append([sg.Button('Back'), sg.Button('Exit')])
    return dir_layout
