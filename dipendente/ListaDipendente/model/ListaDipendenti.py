import os
import pickle

#Classe modello lista dei dipendenti

class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.listdipendent = [] #definizione della lista

        #leggere dal file pickle e popolare la lista

        if os.path.isfile('dipendente/ListaDipendente/datidip/lista_dipendenti.pickle'):
            with open('dipendente/ListaDipendente/datidip/lista_dipendenti.pickle', 'rb') as f:
                self.listdipendent = pickle.load(f)

    #metodo per aggiungere un nuovo dipendente alla lista che prende come parametro:
    #modello: oggetto della classe DipendenteModel

    def aggiungi_dipendente(self, modello):
        self.listdipendent.append(modello)
    #metodo per cercare un dipendente che prende come parametri:
    #name: nome del dipendente
    #cognome:cognome del dipendente

    def get_dipendente_by_name(self, name,cognome):
        for dipendente in self.listdipendent:
            if cognome == dipendente.cognome.split()[0] and name== dipendente.nome.split()[-1]:
                return dipendente

    # metodo per eliminare un dipendente dalla lista che prende come parametri:
    # name: nome del dipendente
    # cognome:cognome del dipendente

    def remove_dipendente_by_name(self,name,cognome):
        for dipendente in self.listdipendent:
            if cognome == dipendente.cognome.split()[0] and name== dipendente.nome.split()[-1]:
                self.listdipendent.remove(dipendente)
    #metodo per salvare la lista sul file pickle

    def save(self):
        # salvataggio lista dipendente
        with open('dipendente/ListaDipendente/datidip/lista_dipendenti.pickle','wb') as handel:
            pickle.dump(self.listdipendent, handel, pickle.HIGHEST_PROTOCOL)