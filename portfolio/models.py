from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length= 200)
    description = models. TextField()
    image = models.ImageField(upload_to="projects")#le digo que cree la carpeta projects para que guarde las imgs
    created = models.DateTimeField(auto_now_add=True)#Este se ejecuta solo la primera vez(al crearse)
    updated = models.DateTimeField(auto_now= True)#Este se ejecuta cada vez que se actualiza una instancia

    class Meta():#para añadir configuraciones extendidas
        ordering = ["-created"]#La lista es por si lo quiero ordenar en base a más cosas, con el signo de menos logro ordenarlo de más nuevo a más viejo
    
    def __str__(self):
        return self.title