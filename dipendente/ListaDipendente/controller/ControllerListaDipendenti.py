from dipendente.ListaDipendente.model.ListaDipendenti import ListaDipendenti


class ControllerListaDipendenti():
    def __init__(self):
        super(ControllerListaDipendenti, self).__init__()
        self.modeldip = ListaDipendenti()

    # funzioni riguardanti i film
    def aggiungi_dipendente(self, modello):
        self.modeldip.aggiungi_dipendente(modello)

    def get_dipendente_by_name(self,name):
        return self.modeldip.get_dipendente_by_name(name)

    def save(self):
        self.modeldip.save()