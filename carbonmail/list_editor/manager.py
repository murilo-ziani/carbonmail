# Onde estarão todas as funções deste pacote.
# Ele é quem vai coordenar esse pacote.

def initialize(email_sender):
    from carbonmail.list_editor import List_editor
    
    ems = List_editor(email_sender)
    ems.enable_window()

