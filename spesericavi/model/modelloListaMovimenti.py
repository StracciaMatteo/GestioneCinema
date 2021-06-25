import os.path
import pickle

class modelloListaMovimenti():
    def __init__(self):
        super(modelloListaMovimenti,self).__init__()
        self.listamovimenti = []

        if os.path.isfile ('spesericavi/datilistaSR/lista_movimenti.pickle'):
            with open ('spesericavi/datilistaSR/lista_movimenti.pickle', 'rb') as f:
                self.listamovimenti = pickle.load(f)

    def rimuovi_voce(self,descrizione):
        for voce in self.listamovimenti:
            if descrizione == voce.descrizione:
                self.listamovimenti.remove(voce)

    # salva il file
    def save(self):
        with open('spesericavi/datilistaSR/lista_movimenti.pickle',"wb") as handle:
            pickle.dump(self.listamovimenti, handle,pickle.HIGHEST_PROTOCOL)


