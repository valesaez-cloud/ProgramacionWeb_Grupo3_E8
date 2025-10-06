from rest_framework import serializers
from core.models import Usuario, Juego

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellidos', 'correo', 'rol']  

class JuegoSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='categoria.nombre', read_only=True)          

    class Meta:
        model = Juego
        fields = ['id', 'titulo', 'precio', 'stock', 'categoria', 'categoria_id', 'marca', 'marca_id']