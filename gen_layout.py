import sys as sys
import os as os
import shutil as sh
import re as re
import PySimpleGUI as sg

prog_dir = os.getcwd()
folder_icon = os.path.join(prog_dir,r'graphics', 'folder_icon.png')
file_icon = os.path.join(prog_dir,r'graphics', 'file_icon.png')

#Screen size is 5x8 icons
#We define a class for mainpage, the default page that shows the current working directory
#Constructed from list of filenames
class mainpage:
    def __init__(self, dir, listdir):
        #listdir = os.listdir(dir)
        #if len(listdir) > 40:
        #    print('Error! Too many files/directories to display at this time!')
        #    return
        dir_layout = []    #empty output layout
        icon_count = 0     #int to count number of icons printed
        element = []       #element (empty list)
        for name in sorted(listdir, key=str.lower):  #sort directory list, ignore casing
            path = os.path.join(dir, name)
            if icon_count >= 8:
                dir_layout.append(element)      #complete element added to directory layout
                icon_count = 0                  #reset variables
                element = []
            if os.path.isfile(path):        #Check if path of current object is a folder or file
                element.append(sg.Button('\n\n\n\n' + name, button_color = ('black', 'white'), image_filename = file_icon, image_size = (160,160)))     #append another button to the element (row)
                icon_count += 1
            else:
                element.append(sg.Button('\n\n\n\n'+ name, image_filename = folder_icon, image_size = (160,160)))   #append another button to the element (row)
                icon_count += 1

        dir_layout.append(element)  #append last element to finish layout
        dir_layout.append([sg.Button('Back'), sg.Button('Exit'), sg.Button('New Folder'), sg.Button('New File')])

        if(len(listdir) > 40):
            dir_layout.append([sg.Button('Next Page')])

        self.page = dir_layout     #member variable that holds layout
