from django.urls import path
from .views import formulario_view
urlpatterns = [
    path('', formulario_view, name='formulario'),
]