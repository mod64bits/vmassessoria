from datetime import date

from django.test import TestCase


from apps.contato.models import Contato


class ContatoModelTest(TestCase):
    def setUp(self):
        self.obj = Contato(
            contato='marcio oliveira',
            email='mod64bits@gmail.com',
            telefone='19999664769',
            assunto='Orçamento',
            mensagem='mensagem de test'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Contato.objects.exists())

    def test_created_at(self):
        """Subscriotion must have an outo created at attr."""
        self.assertIsInstance(self.obj.created_at, date)