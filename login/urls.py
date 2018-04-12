from django.urls import path
from . import views

urlpatterns = [
    path('iniciarSesion/',views.iniciarSesion,name='iniciarSesion'),
    path('registrarme/',views.registrarme,name='registrarme'),
    path('restaurar/', views.restaurar, name='restaurar'),
    path('acercaDe/',views.acercaDe,name='acercaDe'),
]
