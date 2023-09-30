from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from django.core import mail
from django.shortcuts import resolve_url as r
class MailTest(TestCase):
    def setUp(self):
        data = dict(name='Patrick Souza', cpf='057019302923', email='patrick.souza@aluno.riogrande.ifrs.edu.br', phone='539999999')
        self.response = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]
        
    def test_subscription_email_subject(self):
        expect = "Confirmação de inscrição"
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_sender(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['contato@eventif.com.br', 'patrick.souza@aluno.riogrande.ifrs.edu.br'] 
        self.assertEqual(expect, self.email.to)
    
    def test_subscription_email_body(self):
        contents = ['Patrick Souza','057019302923', 'patrick.souza@aluno.riogrande.ifrs.edu.br', '539999999']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)