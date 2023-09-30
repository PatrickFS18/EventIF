from django.test import TestCase
from contact.formulario import ContactForm

class test_contact_form(TestCase):

    def test_form_valido(self):
        data = {
            'name': 'Patrick',
            'phone': '5399999999',
            'email': 'patrick.souza@aluno.riogrande.ifrs.edu.br',
            'message': 'Eai, bro'
        }
        form = ContactForm(data)
        self.assertTrue(form.is_valid())

    def test_form_invalido(self):
        data = {}  
        form = ContactForm(data)
        self.assertFalse(form.is_valid())

