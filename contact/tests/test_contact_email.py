from django.test import TestCase
from django.core import mail
from django.urls import reverse

class test_contact_email(TestCase):

    def test_envio_email(self):
        
        data = {
            'name': 'Patrick f',
            'phone': '53 999203230',
            'email': 'patrick.souza@aluno.riogrande.ifrs.edu.br',
            'message': 'Funcionou certin'
        }  
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(len(mail.outbox), 1)  
        self.assertEqual(mail.outbox[0].subject, 'Contato do Evento') 

