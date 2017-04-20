from django.db import models

# Create your models here.
class Animales(models.Model):
    nombre=models.CharField(max_length=30)
    numero=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to='fotos')
    class Meta:
        verbose_name_plural="Animales"
