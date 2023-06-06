from django.test import TestCase, Client
from datetime import date

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get('/cotacao/')
        self.assertEqual(response.status_code, 200)

    def test_exchange_rate_view(self):
        today = date.today().strftime('%Y-%m-%d')
        response = self.client.get(f'/cotacao/BRL/{today}/')
        self.assertEqual(response.status_code, 200)

    def test_exchange_rate_view_with_interval(self):
        start_date = '2023-05-04'
        end_date = '2023-05-07'
        response = self.client.get(f'/cotacao/BRL/{start_date}/{end_date}/')
        self.assertEqual(response.status_code, 200)