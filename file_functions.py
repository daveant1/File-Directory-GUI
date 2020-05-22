import sys as sys
import os as os
import shutil as sh
import re as re
import PySimpleGUI as sg
from gen_layout import mainpage

#Generates Error Window layout opens window (int Type specifies type of error)
def gen_error(type):
    if type == 0:
        error = [[sg.T('Warning: Cannot travel up a directory. Limit reached.')], [sg.Button('Close')]]  #Error window layout
    elif type == 1:
        error = [[sg.T('Warning: Please choose a valid name. No special characters allowed.')], [sg.Button('Close')]]
    elif type == 2:
        error = [[sg.T('Bah boo boo beep')], [sg.Button('Close')]]
    err_wind = sg.Window('Error!', error).Finalize()
    #error window loop
    while True:
        err_event, err_value = err_wind.read()
        if err_event == 'Close':
            err_wind.close()
            break


#Input: current window to be closed, path of current directory, listdir for layout template
#Output: new window layout to be opened
def gen_window(curr, path, listdir):   #Function to generate new window layout from path or open file (curr is the current window)
    curr.close()
    if os.path.isdir(path):
        newpage = mainpage(path, listdir)
        new_window = sg.Window(path, newpage.page).Finalize()
        return new_window
    else:
        os.system("start " + path)          #Start the file, but don't close previous window
        newpage = mainpage(os.path.dirname(path), listdir)
        new_window = sg.Window(path, newpage.page).Finalize()
        return new_window

#input: destination to create folder or file (0 for file, 1 for folder)
#ouput: refreshed listdir of curr_dir
def gen_new(curr_dir, type):
    if type:
        new_dir_wind = [[sg.T('Input Desired Folder Name: '), sg.InputText(key='__NAME__')], [sg.Button('OK'), sg.Button('Cancel')]] #New dir menu layout
        new_window = sg.Window('Create New Folder', new_dir_wind).Finalize()
    else:
        new_dir_wind = [[sg.T('Input Desired File Name: '), sg.InputText(key='__NAME__')], [sg.Button('OK'), sg.Button('Cancel')]]
        new_window = sg.Window('Create New File', new_dir_wind).Finalize()

    while True:
        new_event, new_value = new_window.read()

        if new_event == 'OK':
            match = re.search(r'\W+', new_value['__NAME__'])  #Check if any non-word characters in name
            if match == None or (match.group() == "." and type == 0):
                new_path = os.path.join(curr_dir, new_value['__NAME__'])
                new_window.close()
                if type:
                    os.mkdir(new_path)
                else:
                    f = open(new_path, "w")
                listdir = os.listdir(curr_dir)     #Refresh curr_dir after adding file/folder
                return listdir
            else:
                gen_error(1)
                continue

        elif new_event == 'Cancel':
            new_window.close()
            return (os.listdir(curr_dir))

###TO BE CONTINUED........
def copy(path):
    copied_file = os.path.abspath(path)
    return copied_file

def paste(source_path, dest_path):
    shutil.copy(source_path, dest_path)
