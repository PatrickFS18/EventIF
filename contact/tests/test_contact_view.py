from django.test import TestCase
from django.urls import reverse
from django.core import mail

class test_contact_view(TestCase):

    def test_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_form.html')
        
    def test_csrf(self):
        response = self.client.get(reverse('contact'))
        self.assertContains(response, 'csrfmiddlewaretoken')
        
    def test_post_valido(self):
        
        data = {
            'name': 'Patrick',
            'phone': '5399999999',
            'email': 'patrick.souza@aluno.riogrande.ifrs.edu.br',
            'message': 'Eai, bro'
        }  
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(len(mail.outbox), 1)
        
    def test_post_invalido(self):
        data = {} 
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200) 
    
