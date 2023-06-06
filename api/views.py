from datetime import datetime, timedelta

import requests
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class DateGenerator:
    @staticmethod
    def generate_dates(start_date, end_date):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        dates = []
        delta = timedelta(days=1)

        while start_date <= end_date:
            dates.append(start_date.strftime('%Y-%m-%d'))
            start_date += delta

        return dates


class ExchangeRateView(View):
    SYMBOLS = {'BRL': 'R$', 'EUR': '€', 'JPY': '¥'}

    SYMBOLS_API = {
        "EUR": {"name": "Euro", "symbol": "€"},
        "JPY": {"name": "Japanese Yen", "symbol": "¥"},
        "BRL": {"name": "Brazilian Real", "symbol": "R$"}
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.currency = None
        self.start_date = None
        self.end_date = None
        self.today = datetime.today().date()

    def get(self, request, currency, start_date, end_date=None):
        self.currency = currency
        self.start_date = start_date
        self.end_date = end_date if end_date else start_date
        return self.get_cotacao()

    def get_cotacao(self):
        if self.currency and self.currency.upper() not in ['BRL', 'EUR', 'JPY']:
            return self._render_error("Erro: currency inválida", status=400)

        if self._is_invalid_date():
            return self._render_error("Erro: a data final é maior que a data inicial.", status=422)

        dates = DateGenerator.generate_dates(self.start_date, self.end_date)

        if len(dates) > 5:
            return self._render_error(
                "Erro: o intervalo de data deve ser de no máximo 5 dias")

        results, values = self._get_exchange_rates(dates)

        symbol, name = self._get_currency_symbol_and_name()

        return render(self.request, 'cotacao.html',
                      {'results': results, 'dates': dates, 'values': values, 'symbol': symbol, 'name': name})

    def _is_invalid_date(self):
        start_date = datetime.strptime(self.start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(self.end_date, '%Y-%m-%d').date()

        return start_date > end_date or start_date > self.today or end_date > self.today

    def _render_error(self, message, status=200):
        return render(self.request, 'error.html', {'error_message': message}, status=status)

    def _get_exchange_rates(self, dates):
        results = []
        values = []

        for date in dates:
            response = requests.get(f'https://api.vatcomply.com/rates?base=USD&date={date}')

            if response.status_code == 200:
                data = response.json()
                rates = data.get('rates', {})
                results.append(f"Data: {date}, Dólar - {self.currency.upper()}: {rates.get(self.currency.upper(), 'N/A')}")
                values.append(rates.get(self.currency.upper(), 0))
            else:
                results.append(f"Erro ao obter cotações para a data {date}")

        return results, values

    def _get_currency_symbol_and_name(self):
        symbol = self.SYMBOLS.get(self.currency.lower(), '$')
        name = self.SYMBOLS_API.get(self.currency.upper(), {}).get('name', 'US Dollar')
        symbol = self.SYMBOLS_API.get(self.currency.upper(), {}).get('symbol', symbol)

        return symbol, name
