from django.test import TestCase
from django.urls import reverse
from .models import Contact
from .formulario import ContactForm


class ContactTests(TestCase):

    def test_contact_form_valid(self):
        form_data = {
            'nome': 'John Doe',
            'email': 'john@example.com',
            'telefone': '123-456-7890',
            'mensagem': 'Hello, World!'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid(self):
        form_data = {
            'nome': '',  # Campo obrigatório em branco
            'email': 'invalid-email',  # Email inválido
            'telefone': '123-456-7890',
            'mensagem': 'Hello, World!'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_contact_model(self):
        contact = Contact.objects.create(
            nome='Jane Doe',
            email='jane@example.com',
            telefone='987-654-3210',
            mensagem='Testing contact model.'
        )
        self.assertEqual(contact.nome, 'Jane Doe')
        self.assertEqual(contact.email, 'jane@example.com')
        self.assertEqual(contact.telefone, '987-654-3210')
        self.assertEqual(contact.mensagem, 'Testing contact model.')

    def test_contact_view(self):
        response = self.client.get(reverse('contact_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_form.html')

    def test_contact_view_post(self):
        form_data = {
        'nome': 'John Doe',
        'email': 'john@example.com',
        'telefone': '123-456-7890',
        'mensagem': 'Hello, World!'
        }
        response = self.client.post(reverse('contact_form'), data=form_data)
    
        # Verifique se a resposta redireciona para a página de confirmação (substitua 'pagina_de_confirmacao' pela URL real)
        self.assertRedirects(response, '/contato/', status_code=302)
