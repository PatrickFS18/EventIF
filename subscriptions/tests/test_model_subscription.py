from django.test import TestCase
from subscriptions.models import Subscription
from datetime import datetime

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(name = 'Patrick Souza', cpf = '1223456789', email = 'patrick.souza@aluno.riogrande.ifrs.edu.br', phone='53095939539')
        self.obj.save()
    def test_create(self):
        self.assertTrue(Subscription.objects.exists())
    
    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)
    
    def test_str(self):
        self.assertEqual('Patrick Souza', str(self.obj))