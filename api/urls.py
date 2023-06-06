from django.urls import path
from .views import IndexView

urlpatterns = [
    path('cotacao/', IndexView.as_view(), name='index'),
]