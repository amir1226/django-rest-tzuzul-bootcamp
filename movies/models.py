from django.db import models

# Create your models here.
class Movie(models.Model):
    titulo=models.CharField(max_length=100)
    genero=models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    director = models.CharField(max_length=120)
    #MANY TO MANy
    # director = models.ManyToManyField(Director, through="MovieDirector")

    def __str__(self):
        return self.titulo
