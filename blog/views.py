from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostFormulario

# Create your views here.

def listadoPosts(request):
    posts= Post.objects.filter(fechaPublicacion__lte =timezone.now()).order_by('fechaPublicacion')
    return render(request,'blog/listadoPost.html',{'posts':posts})

def detalles(request,pk):
    post = get_object_or_404(Post,pk = pk)
    return render(request,'blog/detalles.html',{'post':post})

def nuevoPost(request):
    if request.method == 'POST':
        form = PostFormulario(request.POST)
        if  form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fechaPublicacion = timezone.now()
            post.save()
            return redirect('detalles',pk=post.pk)
    else:
        form = PostFormulario()
    return render(request, 'blog/editar.html',{'form':form})

def modificar(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostFormulario(request.POST,instance=post)
        if  form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('detalles',pk=post.pk)
    else:
        form = PostFormulario(instance=post)
    return render(request, 'blog/editar.html',{'form':form})
