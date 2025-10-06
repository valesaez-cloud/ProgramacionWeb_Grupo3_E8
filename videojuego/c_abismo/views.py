from django.shortcuts import render, redirect
from django.http import JsonResponse 
from core.models import Usuario, Juego
from rest_framework import viewsets
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from .serializers import UsuarioSerializer, JuegoSerializer
from rest_framework import viewsets
import requests


# Create your views here.
def home(request):
    nombre_usuario = request.session.get('usuario_nombre', None)
    return render(request, 'index.html', {'usuario_nombre': nombre_usuario})

def inicio(request): 
    nombre_usuario =  request.session.get('usuario_nombre', None)
    return render(request, 'index.html', {'usuario_nombre': nombre_usuario})

def login(request):
    return render(request, 'login.html')

def registrar(request):
    return render(request, 'registrar_usr.html')

def recuperar(request):
    return render(request, 'recuperar_cta.html')

def resta_clave(request):
    return render(request, 'restablecer_clave.html')

def mi_perfil(request):
    nombre_usuario =  request.session.get('usuario_nombre', None)
    return render(request, 'perfil.html', {'usuario_nombre': nombre_usuario})
    
def mod_perfil(request):
    nombre_usuario =  request.session.get('usuario_nombre', None)
    return render(request, 'mod_perfil.html', {'usuario_nombre': nombre_usuario})

def cerrar_sesion(request):
    request.session.flush()
    return redirect('inicio')

def listar_usuarios(request): 
    nombre_usuario =  request.session.get('usuario_nombre', None)
    usuarios = Usuario.objects.all()
    return render(request, 'admin.html', {'usuarios': usuarios, 'usuario_nombre': nombre_usuario})


# categorías
def rpg(request):
    nombre_usuario =  request.session.get('usuario_nombre', None)
    return render(request, 'rpg.html', {'usuario_nombre': nombre_usuario})    

def survival(request):
    nombre_usuario =  request.session.get('usuario_nombre', None)
    return render(request, 'survival.html', {'usuario_nombre': nombre_usuario}) 

def horror(request):
    nombre_usuario =  request.session.get('usuario_nombre', None)
    return render(request, 'horror.html', {'usuario_nombre': nombre_usuario}) 


def estrategia(request):
    nombre_usuario =  request.session.get('usuario_nombre', None)
    return render(request, 'estrategia.html', {'usuario_nombre': nombre_usuario}) 

def vintage(request):
    nombre_usuario =  request.session.get('usuario_nombre', None)
    return render(request, 'vintage.html', {'usuario_nombre': nombre_usuario}) 

def marca(request):
    nombre_usuario =  request.session.get('usuario_nombre', None)
    return render(request, 'marca.html', {'usuario_nombre': nombre_usuario}) 


#APIS EXTERNAS
def obtener_categorias_juegos(request):
    try:
        r = requests.get("https://www.freetogame.com/api/games", timeout=10)
        r.raise_for_status()
        juegos = r.json()
        # Agrupar por género
        categorias = {}
        for j in juegos:
            gen = (j.get("genre") or "Otros").strip()
            # guardo una mini info de muestra por género
            if gen not in categorias:
                categorias[gen] = {
                    "name": gen,
                    "thumb": j.get("thumbnail"),     # una imagen cualquiera del género
                    "description": f"Juegos del género {gen}"
                }
        # Convertir a lista como la API de tu profe
        data = {"categories": list(categorias.values())}
        return JsonResponse(data, safe=False)
    except requests.RequestException as e:
        return JsonResponse({"error": "No se pudo obtener la información", "detalle": str(e)}, status=500)

def juegos_externos(request):
    return render(request, "juegos_externos.html")

def obtener_noticias(request):
    url = "https://www.mmobomb.com/api1/latestnews"
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        data = r.json()
        # data es una lista de noticias; la devolvemos tal cual
        return JsonResponse(data, safe=False)
    except requests.RequestException as e:
        return JsonResponse({"error": f"No se pudo obtener noticias: {e}"}, status=500)

def noticias(request):
    return render(request, "noticias.html")


# API INTERNAS
def api_usuarios(request):
    usuarios = Usuario.objects.all()
    data = UsuarioSerializer(usuarios, many=True).data
    return JsonResponse(data, safe=False)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


def api_juegos(request):
    juegos = Juego.objects.select_related('categoria').all()
    data = JuegoSerializer(juegos, many=True).data
    return JsonResponse(data, safe=False)

class JuegoViewSet(viewsets.ModelViewSet):
    queryset = Juego.objects.select_related('categoria').all()
    serializer_class = JuegoSerializer
