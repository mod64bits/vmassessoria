from django.test import TestCase


class ContatoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('contato')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
