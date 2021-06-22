import os.path
import pickle

import spesericavi.view.VistaListaMovimenti


class modelloListaMoviemnti():
    def __init__(self):
        super(modelloListaMoviemnti,self).__init__()
        self.modelloListaMovimenti = []
        self.tabella= spesericavi.view.VistaListaMovimenti.table_ListaMov


        if os.path.isfile('spesericavi/datilistaSR/lista_movimenti.pickle'):
            with open('spesericavi/datilistaSR/lista_movimenti.pickle', 'rb')as f:
                self.lista_movimenti = pickle.load(f)

    def get_voce (self,segno,importo,descrizione):
        row = 0
        for voce in self.lista_movimenti:
            self.tabella.setItem(row,1,segno)
            self.tabella.setItem(row,1,importo)
            self.tabella.setItem(row,2,descrizione)
            row = row+1


