from django.shortcuts import redirect, render
from .form import EventoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registrar_usuario(request):
    return render(request, 'registrar_usuario.html')

def login_usuario(request):
    return render(request, 'login_usuario.html')

def logout_usuario(request):
    return render(request, 'logout_usuario.html')

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')

def registrar_evento(request):
    if request.method == 'POST':
        evento_form = EventoForm(request.POST)
        if evento_form.is_valid():
            evento_form.save()
            return redirect('registro_exitoso')
    return render(request, 'registrar_evento.html')

