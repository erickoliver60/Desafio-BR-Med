from django.urls import path

from .views import IndexView, ExchangeRateView, StoredExchangeRateView


urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name='index'
    ),
    path(
        'cotacao/<str:currency>/<str:start_date>/',
        ExchangeRateView.as_view(),
        name='cotacao'
    ),
    path(
        'cotacao/<str:currency>/<str:start_date>/<str:end_date>/',
        ExchangeRateView.as_view(),
        name='cotacao_por_intervalo'
    ),
    path(
        'cotacao-armazenada/<str:currency>/<str:start_date>/',
        StoredExchangeRateView.as_view(),
        name='cotacao_armazenada'
    ),
    path(
        'cotacao-armazenada/<str:currency>/<str:start_date>/<str:end_date>/',
        StoredExchangeRateView.as_view(),
        name='cotacao_armazenada_por_intervalo'
    ),
]
