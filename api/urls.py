from django.urls import path
from .views import IndexView, ExchangeRateView

urlpatterns = [
    path('cotacao/', 
        IndexView.as_view(), 
        name='index'),
    path('cotacao/<str:currency>/<str:start_date>/',
        ExchangeRateView.as_view(),
        name='cotacao'),
    path('cotacao/<str:currency>/<str:start_date>/<str:end_date>/',
        ExchangeRateView.as_view(),
        name='cotacao_por_intervalo'),
]