from django.test import TestCase
from .form import ContactForm


class test_contact_valid(TestCase):

    def test_contact_form_valid(self):
        form_data = {
            'nome': 'Erick souza',
            'email': 'erick@gmail.com',
            'telefone': '53888888888',
            'mensagem': 'teste'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    