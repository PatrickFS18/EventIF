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
        #email enviado
        self.assertEqual(response.status_code, 302)
        #possui email na outbox
        self.assertEqual(len(mail.outbox), 1)  
        #Contato do evento é o subject do email
        self.assertEqual(mail.outbox[0].subject, 'Contato do Evento') 
        #email destino é patrick...
        expect= ['contato@eventif.com.br', 'patrick.souza@aluno.riogrande.ifrs.edu.br'] 
        self.assertEqual(expect, mail.outbox[0].to)
        
