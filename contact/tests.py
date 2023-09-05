from django.test import TestCase
from django.urls import reverse
from .form import Contact
from .form import ContactForm


class ContactTests(TestCase):

    def test_contact_form_valid(self):
        form_data = {
            'nome': 'Erick souza',
            'email': 'erick@gmail.com',
            'telefone': '53888888888',
            'mensagem': 'teste'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid(self):
        form_data = {
            'nome': '',  # Campo obrigatório em branco
            'email': 'invalid-email',  # Email inválido
            'telefone': '53888888888',
            'mensagem': 'teste'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

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

    def test_contact_view(self):
        response = self.client.get(reverse('contact_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_form.html')

    def test_contact_view_post(self):
        form_data = {
        'nome': 'Erick souza',
        'email': 'erick@gmail.com',
        'telefone': '53888888888',
        'mensagem': 'teste'
        }
        response = self.client.post(reverse('contact_form'), data=form_data)
    
        # Verifique se a resposta redireciona para a página de confirmação (substitua 'pagina_de_confirmacao' pela URL real)
        self.assertRedirects(response, '/contato/', status_code=302)
