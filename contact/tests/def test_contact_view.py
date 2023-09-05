from django.test import TestCase
from django.urls import reverse


class test_view(TestCase):
    def test_contact_view(self):
        response = self.client.get(reverse('contact_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_form.html')
