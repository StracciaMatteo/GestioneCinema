#Classe che modella i dati del dipendente

class DipendenteModel():
    #Costruttore per l'inizializzazione del dipendente
    def __init__(self,nome,cognome,sesso,data_nascita,luogo_nascita,mansione,cf,stipendio,id,turno_lavoro,girono_lavoro,ferie_dal,ferie_al,commento):
        super(DipendenteModel, self).__init__()
        self.nome=nome
        self.cognome=cognome
        self.sesso=sesso
        self.data_nascita=data_nascita
        self.luogo_nascita=luogo_nascita
        self.mansione=mansione
        self.cf=cf
        self.stipendio=stipendio
        self.id=id
        self.turno_lavoro=turno_lavoro
        self.giorno_libero=girono_lavoro
        self.ferie_dal=ferie_dal
        self.ferie_al=ferie_al
        self.commento=commento