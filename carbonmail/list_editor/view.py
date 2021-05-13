# É onde fica o código para a Interface gráfica.
# Tudo que existir de VISUAL vai ficar aqui.
# É principalmente aqui que usaremos o PySimpleGui

import PySimpleGUI as sg

lista = ['Administradores', 'Alunos']

def get_layout():
    
    frame_list = [
        [
            sg.Text('Selecione a lista:'),
            sg.Combo(lista, default_value=lista[1], key='-List-'),
        ],
        [
            sg.Text('Criar uma lista:'),
            sg.In(key='-Listname-'),
            sg.Button('Criar a Lista', key='-Create-', size=(10, 1)),
        ],
        [
            sg.Button('Deletar a Lista', key='-Delete-', size=(15, 1)),
            sg.Button('Mostrar Contatos', key='-Delete-', size=(15, 1)),
        ],
    ]
    
    layout = [
        [sg.Frame('Configurações da Lista', frame_list),],
    ]

    return layout

def get_window():
    return sg.Window('Editor de Lista', get_layout())