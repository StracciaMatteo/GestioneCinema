import os
import pickle

from PyQt5.QtWidgets import QLineEdit


class loginModel():
    def __init__(self):
        super(loginModel, self).__init__()
        self.listadipendenti = []

        # carica la lista dei dipendenti per poter leggere i loro id e permettere il login
        if os.path.isfile('dipendente/ListaDipendente/datidip/lista_dipendenti.pickle'):
            with open('dipendente/ListaDipendente/datidip/lista_dipendenti.pickle', 'rb') as f:
                self.listadipendenti = pickle.load(f)

    def hide_or_show_pw(self, vista):
        vista.Codice.setEchoMode(QLineEdit.Normal)
        if not vista.btn_visibilita_password.isChecked():
            vista.Codice.setEchoMode(QLineEdit.Password)

    def login(self, pw):
        # rimuovere
        if pw == "":
            return "prova"

        for item in self.listadipendenti:
            if pw == item.id:
                return item.nome + " " + item.cognome
        else:
            return False
