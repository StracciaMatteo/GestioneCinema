from unittest import TestCase

from dipendente.DatiDipendente.model.DipendenteModel import DipendenteModel
from dipendente.ListaDipendente.controller.ControllerListaDipendenti import ControllerListaDipendenti


class TestControllerListaDipendenti(TestCase):
    def setUp(self) -> None:
        self.controller = ControllerListaDipendenti()
        self.dipendente = DipendenteModel("nome", "cognome", "m", None, "luogo_nascita", None, "cf", None, "id",
                                          None, None, None, None, None)
    def test_aggiungi_dipendente(self):
        self.controller.aggiungi_dipendente(self.dipendente)
        self.assertTrue(self.dipendente in self.controller.modeldip.listdipendent)

    def test_get_dipendente_by_name(self):
        self.controller.aggiungi_dipendente(self.dipendente)
        dip = self.controller.get_dipendente_by_name("nome", "cognome")
        self.assertTrue(dip.nome == "nome")
        self.assertTrue(dip.cognome == "cognome")

    def test_remove_dipendente_by_name(self):
        self.controller.aggiungi_dipendente(self.dipendente)
        self.controller.remove_dipendente_by_name("nome", "cognome")
        dip = self.controller.get_dipendente_by_name("nome", "cognome")
        self.assertIsNone(dip)
