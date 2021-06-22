import os
import pickle


class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.listdipendent = []

        if os.path.isfile('dipendente/ListaDipendente/datidip/lista_dipendenti.pickle'):
            with open('dipendente/ListaDipendente/datidip/lista_dipendenti.pickle', 'rb') as f:
                self.listdipendent = pickle.load(f)


    def aggiungi_dipendente(self, modello):
        self.listdipendent.append(modello)

    def get_dipendente_by_name(self, name):
        for dipendente in self.listdipendent:
            if name == dipendente.cognome.split()[0]:
                return dipendente

    def remove_dipendente_by_name(self,name):
        for dipendente in self.listdipendent:
            if name == dipendente.cognome.split()[0]:
                self.listdipendent.remove(dipendente)

    def save(self):
        # salvataggio lista dipendente
        with open('dipendente/ListaDipendente/datidip/lista_dipendenti.pickle','wb') as handel:
            pickle.dump(self.listdipendent, handel, pickle.HIGHEST_PROTOCOL)