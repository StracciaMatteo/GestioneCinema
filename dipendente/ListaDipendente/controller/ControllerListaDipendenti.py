from dipendente.ListaDipendente.model.ListaDipendenti import ListaDipendenti

#Classe controllore modello lista dipendenti

class ControllerListaDipendenti():
    def __init__(self):
        super(ControllerListaDipendenti, self).__init__()
        self.modeldip = ListaDipendenti() #oggetto della classe ListaDipendenti

    #metodo che peremette di aggiungere un nuovo dipendente alla lista dipendenti e che chiama il metodo della classe ListaDipendenti e prende com parametro:
    #modello:oggetto della classe DipendenteModel

    def aggiungi_dipendente(self, modello):
        self.modeldip.aggiungi_dipendente(modello)

    #metodo per cercare il dipendente con il nome e il cognome e chiama il metodo della classe listaDipendenti

    def get_dipendente_by_name(self,name,cognome):
        return self.modeldip.get_dipendente_by_name(name,cognome)

    #metodo per eliminare un dipendente dalla lista dipendente con il nome o il cognome e chiama il metodo della classe listadipendenti

    def remove_dipendente_by_name(self, name ,cognome):
        self.modeldip.remove_dipendente_by_name(name,cognome)


    #metodo per slavare la lista sul file pickle chiamando il metodo save della classe  ListaDipendenti

    def save(self):
        self.modeldip.save()