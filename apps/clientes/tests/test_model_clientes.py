from django.test import TestCase
from datetime import date
from apps.clientes.models import TipoCliente, Cliente


class TipoClienteModelTest(TestCase):
    def setUp(self):
        self.obj = TipoCliente(
            tipo='Contrato'
        )
        self.obj.save()

    def test_create(self):
        """Must create type client"""
        self.assertTrue(TipoCliente.objects.exists())

    def test_created_at(self):
        """Subscriotion must have an outo created at attr."""
        self.assertIsInstance(self.obj.created_at, date)


class ClienteModelTest(TestCase):
    def setUp(self):
        self.tipo_cliente = TipoCliente(
            tipo='contrato'
        )
        self.tipo_cliente.save()
        self.obj = Cliente(
            tipo=self.tipo_cliente,
            nome='Marcio Oliveira',
            slug='marcio-oliveira',
            cpf_cnpj='08008198745',
            email='mod64bits@gmail.com',
            telefone='19999664769',
            endereco='Rua Maria ruana',
            bairro='Liberdade',
            referencia='em frente ao percado preço bom'

        )
        self.obj.save()

    def test_create(self):
        """must create client"""
        self.assertTrue(Cliente.objects.exists())
        self.assertIsInstance(self.obj.created_at, date)
