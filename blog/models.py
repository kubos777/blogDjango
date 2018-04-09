from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    '''
    Modelo para almacenar todos los Post
    '''
    autor =  models.ForeignKey('auth.User', on_delete= models.CASCADE)
    titulo =  models.CharField(max_length = 200)
    texto =  models.TextField()

    fechaCreacion =  models.DateTimeField(
        default =  timezone.now)

    fechaPublicacion = models.DateTimeField(
        blank = True, null = True)

    def publicar(self):
        '''
        Funcion para obtener la fecha de publicacion cuando
        se publique algun Post
        '''
        self.fechaPublicacion = timezone.now()
        self.save()

    #Metodo magico que nos permite castear un objeto a una cadena
    def __str__(self):
        return self.titulo



