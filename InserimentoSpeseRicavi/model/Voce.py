import os.path
import pickle

class Voce():
    def __init__(self):
        super(Voce, self).__init__()
        self.lista_movimenti=[]
        self.read()

    def read(self):
        self.lista_movimenti.clear()
        if os.path.isfile('spesericavi/datilistaSR/lista_movimenti.pickle'):
            with open('spesericavi/datilistaSR/lista_movimenti.pickle', 'rb')as f:
                self.lista_movimenti= pickle.load(f)

    def aggiungi_voce(self, model):
        self.lista_movimenti.append(model)
        self.save()
        self.read()

    def rimuovi_voce(self, descrizione):
        for voce in self.lista_movimenti:
            if descrizione == voce.descrizione:
                self.lista_movimenti.remove(voce)

    def save(self):
        with open('spesericavi/datilistaSR/lista_movimenti.pickle','wb')as handle:
            pickle.dump(self.lista_movimenti,handle, pickle.HIGHEST_PROTOCOL)