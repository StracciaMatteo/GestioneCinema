from spesericavi.model.modelloListaMovimenti import modelloListaMoviemnti


class ControllerListaMovimento():
    def __init__(self):
        super(ControllerListaMovimento,self).__init__()
        self.modelloLista = modelloListaMoviemnti()

    def get_voce(self,modello):
        self.modelloLista.get_voce(modello)


