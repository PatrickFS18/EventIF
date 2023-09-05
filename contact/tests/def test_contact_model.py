from django.test import TestCase
from .form import Contact



class test_contactModel(TestCase):

    def test_contact_model(self):
        contact = Contact.objects.create(
            nome='Erick Souza',
            email='erick@gmail.com',
            telefone='53888888888',
            mensagem='teste'
        )
        self.assertEqual(contact.nome, 'Erick Souza')
        self.assertEqual(contact.email, 'erick@gmail.com')
        self.assertEqual(contact.telefone, '53888888888')
        self.assertEqual(contact.mensagem, 'teste')

   