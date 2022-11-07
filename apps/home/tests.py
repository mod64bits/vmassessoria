from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('home:home')

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        print()
        self.assertTemplateUsed(self.response, 'home/index.html')


class ServicosTest(TestCase):
    """get servicos list"""
    def setUp(self):
        self.response = self.client.get('home:servicos_home')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use servico list"""
        self.assertTemplateUsed(self.response, 'servicos_home.html')