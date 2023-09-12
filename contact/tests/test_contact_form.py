from django.test import TestCase
from contact.formulario import ContactForm

class test_contact_form(TestCase):

    def test_form_valido(self):
        data = {
            'name': 'Patrikc',
            'phone': '53999101031',
            'email': 'patrick@gmail.com',
            'message': 'teste mensagem.'
        }
        form = ContactForm(data)
        self.assertTrue(form.is_valid())

    def test_form_invalido(self):
        data = {}  
        form = ContactForm(data)
        self.assertFalse(form.is_valid())

