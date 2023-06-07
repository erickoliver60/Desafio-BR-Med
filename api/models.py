from django.db import models

class CurrencyQuote(models.Model):
    base_currency = models.CharField(max_length=3)
    target_currency = models.CharField(max_length=3)
    quote = models.DecimalField(max_digits=20, decimal_places=16)
    date = models.DateField()

    def __str__(self):
        return f'{self.base_currency} to {self.target_currency} on {self.date}'
