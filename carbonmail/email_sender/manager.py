# Onde estarão todas as funções deste pacote.
# Ele é quem vai coordenar esse pacote.


def initialize():
    from carbonmail.email_sender import Email_sender
    
    ems = Email_sender()
    ems.enable_window()
