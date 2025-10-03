from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # aquí se define 'home'
    path('registrar_evento/', views.registrar_evento, name='registrar_evento'),
] 