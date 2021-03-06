# Arquivo usado para transformar a pasta em pacote
# Ele é sempre executado ao importar este pacote

from carbonmail.database.manager import delete_list
from carbonmail.list_editor.manager import create_list, create_contact, get_list_contacts, import_contact, update_lists
import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from carbonmail.list_editor import view

class List_editor():
    def __init__(self, email_sender):
        self.window = None
        self.ems = email_sender
        
    def instantiate(self):
        if self.window == None:
            self.window = view.get_window()

    def enable_window(self):
        self.instantiate()

        while True:
            event, values = self.window.read()

            if values is not None:
                self.list = values['-Lists-']

            if event in (WIN_CLOSED, '-Back-'):
                self.window.close()
                self.ems.unhide_window()
                break

            elif event == '-Create-':
                list_name = values['-Listname-']

                if create_list(list_name):
                    sg.Popup('Sua lista foi criada', title='Sucesso')
                    update_lists(self.window, self.list)
                else:
                    sg.Popup('Digite um nome válido', title='Erro')

            elif event == '-Import-':
                csv_path = values['-CSV-']
                status_code = import_contact(csv_path, self.list)

                if status_code == -1:
                    sg.Popup('Arquivo não encontrado', title='Erro')
                elif status_code == 0:
                    sg.Popup('Corrija os cabeçalhos (name e email)', title='Erro')
                else:
                    sg.Popup('Sua lista foi importada com sucesso', title='Sucesso')
            
            elif event == '-Add-':
                name = values['-Name-']
                email = values['-Email-']

                if create_contact(name, email, self.list):
                    sg.Popup('Seu contato foi criado', title='Sucesso')
                else:
                   sg.Popup('Insira um e-mail e nome válidos', title='Erro')

            elif event == '-Delete-':             
                answer = sg.Popup(
                    'Isso irá remover todos os contatos da lista. Deseja continuar?',
                    title='Cuidado!',
                    custom_text=("Sim", "Não")
                )

                if answer == "Sim":
                    delete_list(self.list)
                    update_lists(self.window)
                    sg.Popup('A lista foi deletada', title='Sucesso')

            elif event == '-ShowContacts-':
                contacts_list = [
                    f'{contact[0]} <{contact[1]}>'
                    for contact in get_list_contacts(self.list)
                ]
                contacts = "\n".join(contacts_list)

                sg.popup_scrolled(
                    f'Contatos da lista: {self.list}', 
                    contacts, 
                    title="Contatos",
                )

    def close_window(self):
        if self.window != None:
            self.window.Close()
        self.window = None    
    
    def hide_window(self):
        if self.window != None:
            self.window.Hide()
    
    def unhide_window(self):
        if self.window != None:
            self.window.UnHide()
    