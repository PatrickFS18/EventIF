from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from django.core import mail

class MailTest(TestCase):
    def setUp(self):
        data = dict(name='Patrick Souza', cpf='054001000230', email='whesleysouza21@gmail.com', phone='53999999999')
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]
        
    def test_subscription_email_subject(self):
        expect = "Confirmação de inscrição"
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_sender(self):
        expect = 'whesleysouza21@gmail.com'
        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['whesleysouza21@gmail.com', 'whesleysouza21@gmail.com']  # Atualize os endereços de e-mail aqui
        self.assertEqual(expect, self.email.to)
    
    def test_subscription_email_body(self):
        contents = ['Patrick Souza','054001000230', 'whesleysouza21@gmail.com', '53999999999']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)