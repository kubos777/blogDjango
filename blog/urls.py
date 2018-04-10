from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.listadoPosts,name='inicio'),
    path('post/<pk>',views.detalles,name='detalles'),
    path('post/nuevo/',views.nuevoPost,name = 'nuevoPost'),
    path('post/<pk>/modificar/', views.modificar, name='modificar'),
    path('tareaPrebes/',views.tarea,name='tarea'),
]