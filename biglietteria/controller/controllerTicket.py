class controllerTicket():
    def __init__(self, ticket):
        self.model = ticket

    def get_titolofilm(self):
        return self.model.titolofilm

    def get_sala(self):
        return self.model.sala

    def get_ora(self):
        return self.model.ora

    def get_idticket(self):
        return self.model.idticket
