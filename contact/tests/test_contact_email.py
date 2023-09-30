from django.test import TestCase
from django.core import mail
from django.urls import reverse

class test_contact_email(TestCase):

    def test_envio_email(self):
        
        data = {
            'name': 'Patrick',
            'phone': '5399999999',
            'email': 'patrick.souza@aluno.riogrande.ifrs.edu.br',
            'message': 'Eai, bro'
        }  
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)  
        self.assertEqual(mail.outbox[0].subject, 'Contato do Evento') 
        
    def test_email_from(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, mail.outbox[0].from_email)
    
    def test_email_to(self):
        expect = ['contato@eventif.com.br', 'patrick.souza@aluno.riogrande.ifrs.edu.br'] 
        self.assertEqual(expect, mail.outbox[0].to)