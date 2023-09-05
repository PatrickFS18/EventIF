from django.test import TestCase
from django.urls import reverse



class test_contact_post(TestCase):

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
