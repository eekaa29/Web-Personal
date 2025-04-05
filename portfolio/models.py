from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length= 200)
    description = models. TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)#Este se ejecuta solo la primera vez(al crearse)
    updated = models.DateTimeField(auto_now= True)#Este se ejecuta cada vez que se actualiza una instancia