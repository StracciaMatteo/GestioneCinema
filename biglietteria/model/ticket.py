class ticket():
    def __init__(self, titolofilm, sala, ora, idticket):
        super(ticket, self).__init__()
        self.titolofilm = titolofilm
        self.sala = sala
        self.ora = ora
        self.idticket = idticket