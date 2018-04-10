from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def listadoPosts(request):
    posts= Post.objects.filter(fechaPublicacion__lte =timezone.now()).order_by('fechaPublicacion')
    return render(request,'blog/listadoPost.html',{'posts':posts})

def detalles(request,pk):
    post = get_object_or_404(Post,pk = pk)
    return render(request,'blog/detalles.html',{'post':post})
