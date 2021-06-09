class ListaMovimenti():
    def __init__(self):
        super(ListaMovimenti,self).__init__()
        self.lista_movimenti=[]

    def aggiungi_voce(self,descrizione,segno,importo):
        self.lista_movimenti.append(descrizione,segno,importo)
