class ticket():
    def __init__(self, titolofilm, sala, ora, numeroposto, fila):
        super(ticket, self).__init__()
        self.titolofilm = titolofilm
        self.sala = sala
        self.ora = ora
        self.idticket = ""
        self.numeroposto = numeroposto
        self.fila = fila