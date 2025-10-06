from django.urls import path, include
from .views import home, inicio, login, registrar, recuperar, mi_perfil, resta_clave, mod_perfil, cerrar_sesion, listar_usuarios,  rpg, survival, horror, estrategia, vintage, marca, obtener_categorias_juegos, juegos_externos, obtener_noticias, noticias, api_usuarios, api_juegos

from rest_framework.routers import DefaultRouter
from .views import ( UsuarioViewSet, JuegoViewSet)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'juegos', JuegoViewSet, basename='juego')


urlpatterns = [
    path('home', home, name="home"),
    path('inicio', inicio, name="inicio"),
    path('login', login, name="login"),
    path('registrar', registrar, name="registrar"),
    path('recuperar', recuperar, name="recuperar"),
    path('resta_clave', resta_clave, name="resta_clave"),
    path('mi_perfil', mi_perfil, name="mi_perfil"),
    path('mod_perfil', mod_perfil, name="mod_perfil"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('listar_usuarios', listar_usuarios, name="listar_usuarios"),
    path('rpg', rpg, name="rpg"),
    path('survival', survival, name="survival"),
    path('horror', horror, name="horror"),
    path('estrategia', estrategia, name="estrategia"),
    path('vintage', vintage, name="vintage"),
    path('marca', marca, name="marca"),

    # API EXTERNAS
    path("api/categorias/", obtener_categorias_juegos, name="obtener_categorias_juegos"),
    path("juegos/externos/", juegos_externos, name="juegos_externos"),

    path("api/noticias/", obtener_noticias, name="obtener_noticias"),
    path("juegos/noticias/", noticias, name="noticias"),

    # APIS INTERNAS
    path('api/usuarios/', api_usuarios, name='api_usuarios'),
    path('api/juegos/', api_juegos, name='api_juegos'),

    # APIs REST completas (CRUD) vía router
    path('api/', include(router.urls)),

]
