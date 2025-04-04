from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('interface1/', views.interface1, name='interface1'),  # Page pour l'interface1
]

