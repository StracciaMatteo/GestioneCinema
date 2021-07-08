from unittest import TestCase

from InserimentoSpeseRicavi.controller.ControlloreInserimentoSR import ControlloreInserimentoSR
from InserimentoSpeseRicavi.model.ModelVoce import ModelVoce


class TestControlloreInserimentoSR(TestCase):
    def setUp(self) -> None:
        self.controller = ControlloreInserimentoSR()
        self.voce = ModelVoce("-", 200.00, "test")

    def test_aggiungi_voce(self):
        try:
            self.controller.aggiungi_voce(self.voce)
        except:
            pass
        self.assertTrue(self.voce in self.controller.model.lista_movimenti)

    def test_rimuovi_voce(self):
        try:
            self.controller.aggiungi_voce(self.voce)
        except:
            pass
        self.controller.rimuovi_voce(self.voce.descrizione)
        self.assertFalse(self.voce in self.controller.model.lista_movimenti)
