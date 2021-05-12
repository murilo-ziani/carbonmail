# É onde fica o código para a Interface gráfica.
# Tudo que existir de VISUAL vai ficar aqui.
# É principalmente aqui que usaremos o PySimpleGui

import PySimpleGUI as sg

# Window => Janela
# Layout => O que vai mostrar na janela
#           ==> Lista de Listas
#               Cada sublista é uma "Linha" da Janela
#               Cada elemento é um componente visual

def get_layout():
    layout = [
        [
            sg.Text('Eu sou um texto')
        ],
        [
            sg.Text('Eu sou um texto'),
            sg.Button('Eu sou um botão')
        ],
    ]

    return layout

def get_window():
    return sg.Window("Teste de Janela", get_layout())

