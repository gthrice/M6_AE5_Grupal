import os
import sys
import django

# Configurar Django
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_root, 'Plataforma_eventos'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Plataforma_eventos.settings')
django.setup()

from django.contrib.auth.models import Group, Permission

def crear_grupos():
    """Crear grupos con permisos específicos"""
    
    print("=== CREANDO GRUPOS DE USUARIOS ===")
    
    grupos = {
        'asistentes': ['view_eventos', 'asistir_evento'],
        'asistentes_premium': ['view_eventos', 'asistir_evento', 'ver_eventos_privados'],
        'organizadores': ['view_eventos', 'crear_evento', 'editar_evento', 'asistir_evento'],
        'administradores': ['view_eventos', 'crear_evento', 'editar_evento', 'eliminar_evento', 'asistir_evento', 'ver_eventos_privados']
    }
    
    for nombre_grupo, permisos in grupos.items():
        grupo, creado = Group.objects.get_or_create(name=nombre_grupo)
        if creado:
            print(f"✓ Grupo '{nombre_grupo}' creado")
            
            # Asignar permisos al grupo
            for codigo_permiso in permisos:
                try:
                    permiso = Permission.objects.get(codename=codigo_permiso)
                    grupo.permissions.add(permiso)
                    print(f"  - Permiso '{codigo_permiso}' asignado")
                except Permission.DoesNotExist:
                    print(f"  ✗ Permiso '{codigo_permiso}' no encontrado")
        else:
            print(f"✓ Grupo '{nombre_grupo}' ya existe")
    
    print("\n=== GRUPOS DISPONIBLES PARA REGISTRO ===")
    grupos_existentes = Group.objects.all()
    for grupo in grupos_existentes:
        permisos = [perm.codename for perm in grupo.permissions.all()]
        print(f"- {grupo.name}: {', '.join(permisos)}")

if __name__ == "__main__":
    crear_grupos()
