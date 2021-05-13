# É onde fica o código para a Interface gráfica.
# Tudo que existir de VISUAL vai ficar aqui.
# É principalmente aqui que usaremos o PySimpleGui

import PySimpleGUI as sg

# Window => Janela
# Layout => O que vai mostrar na janela
#           ==> Lista de Listas
#               Cada sublista é uma "Linha" da Janela
#               Cada elemento é um componente visual

Lista = ['Administradores', 'Alunos']

def get_layout():
    layout = [
        [
            sg.Text('Selecione o seu código'),
            sg.In(),
            sg.FileBrowse(
                'Selecione', file_types=(("Arquivos Python", "*.py"),
                ),
            ),
        ],
        [
            sg.Text('Selecione a lista de destinatários'),
            sg.Combo(Lista, default_value=Lista[1]),
        ],
        [
            sg.Text('Insira o título'),
            sg.In(key='-Title-'),
        ],
        [
            sg.Text('Insira o conteúdo do E-mail: '),
            sg.MLine(key='-Content-'),
        ],
        [
            sg.Button('Enviar E-mail', key='-Send-'),
            sg.Button('Gerenciar Listas', key='-ListEditor-'),
        ],
    ]

    return layout

def get_window():
    return sg.Window("Teste de Janela", get_layout())

