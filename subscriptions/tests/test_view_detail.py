from django.test import TestCase
from subscriptions.models import Subscription 

class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(name='Patrick Souza', cpf='057019302923', email='patrick.souza@aluno.riogrande.ifrs.edu.br', phone='53095939539')
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        sub = self.resp.context['subscription']
        self.assertIsInstance(sub, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)
        for expect in contents:
            with self.subTest():
                self.assertContains(self.resp, expect)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(404, resp.status_code)