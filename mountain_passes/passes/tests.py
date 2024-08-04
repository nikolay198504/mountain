# passes/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Pass

class PassSubmitViewTests(APITestCase):
    def test_create_pass(self):
        url = reverse('submitData')
        data = {
            "beautyTitle": "Beautiful Pass",
            "title": "Pass Title",
            "other_titles": "Other Titles",
            "connect": "Connection Information",
            "latitude": 45.123,
            "longitude": 12.456,
            "height": 3000,
            "user": {
                "email": "user@example.com",
                "phone": "1234567890",
                "fam": "Doe",
                "name": "John",
                "otc": "Smith"
            }
        }
        response = self.client.post(url, data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print("Response data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pass.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Pass.objects.get().title, 'Pass Title')

# Add more tests as needed
