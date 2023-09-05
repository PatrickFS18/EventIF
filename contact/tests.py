
from django.test import TestCase, override_settings
from .formulario import ContactForm
from django.urls import reverse
from .models import Contact
from django.core import mail
#teste do formulario

class ContactFormTest(TestCase):

    def test_valid_contact_form(self):
        data = {
            'nome': 'Patrick F',
            'email': 'patrick@gmail.com',
            'mensagem': 'teste',
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_contact_form(self):
        data = {
            'email': 'patrick@gmail.com',
            'mensagem': 'teste',
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())

#teste da view


class ContactViewTest(TestCase):
    def test_contact_view_get(self):
        response = self.client.get(reverse('contact_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')

    def test_contact_view_post(self):
        data = {
            'nome': 'Patrick F',
            'email': 'patrick@gmail.com',
            'mensagem': 'teste',
        }
        response = self.client.post(reverse('contact_form'), data=data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Contact.objects.count(), 1)  




# teste envio de email

class ContactEmailTest(TestCase):
    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_send_contact_email(self):
        data = {
            'nome': 'Patrick F',
            'email': 'patrick@gmail.com',
            'mensagem': 'teste',
        }
        response = self.client.post(reverse('contact_form'), data=data)
        self.assertEqual(len(mail.outbox), 1) 
        email = mail.outbox[0]
        self.assertEqual(email.subject, 'Nova Mensagem de Contato')  
