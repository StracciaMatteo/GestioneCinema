from biglietteria.model.ticket import ticket


class controllerTicket():
    def __init__(self):
        self.model = ticket()

    def get_titolofilm(self):
        return self.model.titolofilm

    def get_sala(self):
        return self.model.sala

    def get_ora(self):
        return self.model.ora

    def get_idticket(self):
        return self.model.idticket

    def get_numeroposto(self):
        return self.model.numeroposto

    def get_fila(self):
        return self.model.fila
