from django.test import TestCase

from apps.contato.forms import ContatoForm


class ContatoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/contato/')

    def test_get(self):
        """Get /contato/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use contato/contato.html"""
        self.assertTemplateUsed(self.resp, 'contato/contato.html')

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"', 1)
        self.assertContains(self.resp, 'type="submit"')
        # self.assertContains(self.resp, 'textarea"', 1)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_firm(self):
        """Context must have contact form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, ContatoForm)

    def test_form_has_fields(self):
        """Form must have 5 fields"""

        form = self.resp.context['form']
        self.assertSequenceEqual(['contato', 'email', 'telefone', 'assunto', 'mensagem'], list(form.fields))


class PostContatoValid(TestCase):
    def setUp(self):
        data = dict(
            contato='Marcio Oliveira',
            email='mod64bits@gmail.com',
            telefone='19999664769',
            assunto='Contato',
            mensagem='Teste de salvamento'
        )
        self.resp = self.client.post('/contato/', data)

    def test_post(self):
        """Valid POST should redirect to /contato/"""
        self.assertEqual(302, self.resp.status_code)
