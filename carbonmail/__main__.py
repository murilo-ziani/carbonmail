# Arquivo principal (inicial) ao ser executado.
# Quando iniciamos o projeto (carbonmail) ele é o primeiro ao Python executar.
# Nós usamos também para ser o ponto de entrada da aplicação

from carbonmail.email_sender import view

import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED

def enable_window():
    window = view.get_window()

    while True:
        event, values = window.read()

        if event == WIN_CLOSED:
            window.close()
            break

enable_window()
