from django.test import TestCase, Client


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_index_view(self):
        response = self.client.get('/cotacao/')
        self.assertEqual(response.status_code, 200)

    def test_exchange_rate_view(self):
        today = '2023-06-06'
        response = self.client.get(f'/cotacao/BRL/{today}/')
        self.assertEqual(response.status_code, 200)

    def test_exchange_rate_view_with_interval(self):
        start_date = '2023-05-04'
        end_date = '2023-05-07'
        response = self.client.get(f'/cotacao/BRL/{start_date}/{end_date}/')
        self.assertEqual(response.status_code, 200)

    def test_exchange_rate_view_with_invalid_currency(self):
        response = self.client.get('/cotacao/INVALID/2023-05-04/')
        self.assertEqual(response.status_code, 400)

    def test_exchange_rate_view_with_start_bigger_than_end_date(self):
        response = self.client.get('/cotacao/BRL/2023-04-06/2023-04-04/')
        self.assertEqual(response.status_code, 422)

    def test_exchange_rate_view_with_date_with_more_than_five_days(self):
        response = self.client.get('/cotacao/BRL/2023-03-02/2023-03-14/')
        self.assertEqual(response.status_code, 200)
