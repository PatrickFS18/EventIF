from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from django.core import mail
from subscriptions.models import Subscription
from django.shortcuts import resolve_url as r

class SubscriptionsNewGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('subscriptions:new'))

    def test_get(self):
        """GET /inscricao/ must return status_code 200"""
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')
    
    def test_html(self):
        """HTML must contain input tags"""
        tags = (("<form", 1), ("<input", 6),('type="text"',3), ('type="email"', 1),('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)
    
    def test_csrf(self):
        """HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context["form"]
        self.assertIsInstance(form, SubscriptionForm)



class SubscriptionsNewPostValid(TestCase):
    def setUp(self):
        data = dict(name='Patrick Souza', cpf='03050320539', email='patrick.souza@aluno.riogrande.ifrs.edu.br', phone='53999001530')
        self.response = self.client.post(r('subscriptions:new'), data)

    def test_post(self): 
        self.assertRedirects(self.response, r('subscriptions:detail',1))
    
    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))
    
    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())
    

class SubscriptionsNewPostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post(r('subscriptions:new'), {})

    def test_post(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_error(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())