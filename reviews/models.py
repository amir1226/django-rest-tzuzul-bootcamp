from django.db import models

# Create your models here.
from movies.models import Movie


class Review(models.Model):
    titulo=models.CharField(max_length=100)
    comentario=models.TextField()
    fecha=models.DateField()
    estrellas = models.DecimalField(decimal_places=1, max_digits=2)

    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE, null=True) #SET_NULL

    def __str__(self):
        return self.titulo