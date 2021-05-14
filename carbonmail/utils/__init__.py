# Arquivo usado para transformar a pasta em pacote
# Ele é sempre executado ao importar este pacote

import PySimpleGUI as sg
import os
import sys

def inner_element_space(width=100):
    return [sg.Text(' ' * width, font=('Arial', 1)),]

def root_folder():
    try:
        main_file = os.path.abspath(sys.modules['__main__'].__file__)
    except:
        main_file = sys.executable
    
    # irá retornar esse caminho C:\PROJETOS PYTHON\JORNADA\carbonmail\carbonmail\__main__.py
    return os.path.join(os.path.dirname(main_file),os.pardir)