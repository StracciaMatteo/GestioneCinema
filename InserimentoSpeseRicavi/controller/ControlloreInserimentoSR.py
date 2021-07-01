from InserimentoSpeseRicavi.model.Voce import Voce


class ControlloreInserimentoSR():
    def __init__(self):
        super(ControlloreInserimentoSR,self).__init__()
        self.model= Voce()

    def aggiungi_voce(self,model):
        self.model.aggiungi_voce(model)

    def rimuovi_voce(self,descrizione):
        self.model.rimuovi_voce(descrizione)

    def save(self):
        self.model.save()

