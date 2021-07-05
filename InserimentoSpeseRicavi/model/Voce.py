import os.path
import pickle

class Voce():
    def __init__(self):
        super(Voce, self).__init__()
        self.lista_movimenti=[]
        self.read()

    # Funzione utilizzata per leggere il file pickle dove vengono salvate le voci
    def read(self):
        self.lista_movimenti.clear()
        if os.path.isfile('spesericavi/datilistaSR/lista_movimenti.pickle'):
            with open('spesericavi/datilistaSR/lista_movimenti.pickle', 'rb')as f:
                self.lista_movimenti= pickle.load(f)

    # Funzione del modello che aggiunge le voci inserite una dopo l'altra,poi chiama il salvataggio e la lettura
    def aggiungi_voce(self, model):
        self.lista_movimenti.append(model)
        self.save()
        self.read()

    # Funzione del modello che rimuove la voce se la descirzione passata è uguale alla descrizione della voce
    def rimuovi_voce(self, descrizione):
        for voce in self.lista_movimenti:
            if descrizione == voce.descrizione:
                self.lista_movimenti.remove(voce)

    # Funzione che serve a salvare, scrivendo i dati sul file pickle
    def save(self):
        with open('spesericavi/datilistaSR/lista_movimenti.pickle','wb')as handle:
            pickle.dump(self.lista_movimenti,handle, pickle.HIGHEST_PROTOCOL)