from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.listadoPosts),
    path('post/<pk>',views.detalles,name='detalles'),
]