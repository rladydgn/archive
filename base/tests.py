from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class LocationTestCase(APITestCase):
    def setUp(self):
        self.test_url = reverse('location')

    def test_status(self):
        data = {
            'lon': 126.9784039920235,
            'lat': 37.566627074987274,
            'limit': 1,
            'user_id': "asdf"
        }
        response = self.client.get(self.test_url, data=data)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class RoadTestCase(APITestCase):
    def setUp(self):
        self.test_url = reverse('road')

    def test_status(self):

        data = {
            'id': 'asdf'
        }

        response = self.client.get(self.test_url, data=data)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)