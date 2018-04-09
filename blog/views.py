from django.shortcuts import render

# Create your views here.

def listadoPosts(request):
    return render(request,'blog/listadoPost.html',{})

