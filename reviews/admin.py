from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('titulo','comentario')


admin.site.register(Review, ReviewAdmin)


# Registrar el modelo
# Agregar 5 registros de reviews
# Probar primera ruta
# Probar segunda ruta