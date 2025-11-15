from django.shortcuts import redirect, render
from .form import EventoForm, CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from .mixins import PermissionProtectedTemplateView
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group_name = request.POST.get('group')
            if group_name:
                user.groups.add('group_name')
            login(request, user)
            messages.success(request, 'Usuario registrado exitosamente')
            return redirect('registrar_usuario')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registrar_usuario.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'usuario o contraseña incorrectos')
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_usuario(request):
    logout(request)
    return render(request,'logout.html')

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')

class agregar_evento(PermissionProtectedTemplateView):
    permission_required = 'eventos.crear_evento'
    form_class = EventoForm
    group_required = ('organizadores','administradores')
    template_name = 'registro_evento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento creado exitosamente')
            return redirect('agregar_evento')
        return render(request, 'agregar_evento.html', {'form': form})

class asistir_evento(PermissionProtectedTemplateView):
    permission_required = 'eventos.view_eventos'
    template_name = 'evento.html'
    group_required = ('organizadores','administradores','asistentes','asistentes_premium')

class asistir_evento_premium(PermissionProtectedTemplateView):
    permission_required = 'eventos.ver_eventos_privados'
    template_name = 'evento_premiun.html'
    group_required = ('organizadores','administradores','asistentes_premium')

class editar_evento(PermissionProtectedTemplateView):
    permission_required = 'eventos.editar_evento'
    template_name = 'editar_evento.html'
    group_required = ('organizadores','administradores')

class eliminar_evento(PermissionProtectedTemplateView):
    permission_required = 'eventos.eliminar_evento'
    group_required = 'administradores'
    template_name = 'eliminar_evento.html'


def handler403(request, exception=None):
    """Manejador personalizado para errores 403 (Permiso denegado)"""
    return render(request, '403.html', status=403)


def handler404(request, exception=None):
    """Manejador personalizado para errores 404 (Página no encontrada)"""
    return render(request, '404.html', status=404)
