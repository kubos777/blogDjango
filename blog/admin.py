from django.contrib import admin
from .models import Post

# Register your models here.
#Registamos el modelo de Post para que pueda ser leido
#desde el administrador de Django

admin.site.register(Post)
