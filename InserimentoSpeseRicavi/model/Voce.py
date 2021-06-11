import os.path
import pickle

class Voce():
    def __init__(self):
        super(Voce, self).__init__()
        self.lista_movimenti=[]

        if os.path.isfile('spesericavi/datilistaSR/lista_movimenti.pickle'):
            with open('spesericavi/datilistaSR/lista_movimenti.pickle', 'rb')as f:
                self.lista_movimenti= pickle.load(f)
    def aggiungi_voce(self, model):
        self.lista_movimenti.append(model)
    def save(self):
        with open('spesericavi/datilistaSR/lista_movimenti.pickle','wb')as handle:
            pickle.dump(self.lista_movimenti,handle, pickle.HIGHEST_PROTOCOL)