from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # aquí se define 'home'
    path('registrar_evento/', views.agregar_evento.as_view(), name='registrar_evento'),
    path('asistir_evento/', views.asistir_evento.as_view(), name='asistir_evento'),
    path('asistir_evento_premium/', views.asistir_evento_premium.as_view(), name='asistir_evento_premium'),
    path('editar_evento/', views.editar_evento.as_view(), name='editar_evento'),
    path('eliminar_evento/', views.eliminar_evento.as_view(), name='eliminar_evento'),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
] 