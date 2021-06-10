import os.path
import pickle

from spesericavi.model.modelloListaMovimenti import ListaMovimenti


class ControlloreListaSpeseRicavi():
    def __init__(self):
        super(ControlloreListaSpeseRicavi,self).__init__()
        self.model= ListaMovimenti()
        if os.path.isfile("spesericavi/InsermentoSpeseRicavi/datilistaSR/lista_movimenti.pickle"):
            print("Esiste")
            with open("spesericavi/InsermentoSpeseRicavi/datilistaSR/lista_movimenti.pickle","rb")as f:
                lista_movimenti= pickle.load()
            self.model= lista_movimenti

    def aggiungi_voce(self,descrizione,segno,importo):
        self.model.aggiungi_voce(descrizione,importo,segno)
        with open("spesericavi/InsermentoSpeseRicavi/datilistaSR/lista_movimenti.pickle","wb") as handle:
            pickle.dump(self.model,handle,pickle.HIGHEST_PROTOCOL)

