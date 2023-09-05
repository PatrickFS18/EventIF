from django.test import TestCase
from .form import ContactForm


class contact_invalidForm(TestCase):

    def test_contact_form_invalid(self):
        form_data = {
            'nome': '',  # Campo obrigatório em branco
            'email': 'invalid-email',  # Email inválido
            'telefone': '53888888888',
            'mensagem': 'teste'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())