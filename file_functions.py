import sys as sys
import os as os
import shutil as sh
import re as re
import PySimpleGUI as sg

def copy(path):
    copied_file = os.path.abspath(path)
    return copied_file

def paste(source_path, dest_path):
    shutil.copy(source_path, dest_path)
