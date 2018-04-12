from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
def iniciarSesion(request):
    return render(request,'login/iniciarSesion.html',{})

def registrarme(request):
    return render(request,'login/registrarse.html',{})

def restaurar(request):
    return render(request,'login/restaurar.html',{})

def acercaDe(request):
    return render(request,'login/acercaDe.html',{})
