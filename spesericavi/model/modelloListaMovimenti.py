import pickle
import os.path

class modellaListaMovimenti():
    def __init__(self):
        super(modellaListaMovimenti,self).__init__()
        self.lista_movimenti = []
        if os.path.isfile('spesericavi/datalistaSR/lista_movimenti.pickle'):
            with open('spesericavi/datalistaSR/lista_movimenti.pickle', 'rb') as f:
                self.lista_movimenti= pickle.load(f)



    def aggiungi_voce(self,segno,importo,descrizione):
        self.lista_movimenti.append(descrizione,segno,importo)

    def get_lista_movimenti(self,index):
        return self.lista_movimenti[index]


    def save_data(self):
        with open('spesericavi/datalistaSR/lista_movimenti.pickle', 'wb') as handle:
            pickle.dump(self.lista_movimenti,handle,pickle.HIGHEST_PROTOCOL)