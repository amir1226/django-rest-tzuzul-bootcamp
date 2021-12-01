from rest_framework import serializers
from .models import Review

class ReviewSerializerFirst(serializers.ModelSerializer):
    movie = serializers.StringRelatedField(many=False)
    class Meta:
        model = Review
        #fields = ['titulo','comentario','fecha','estrellas','movie']
        fields = '__all__'

class ReviewMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','titulo']

class ReviewSerializer(serializers.Serializer):
    titulo = serializers.CharField()
    comentario = serializers.CharField()
    fecha = serializers.DateField()
    estrellas = serializers.DecimalField(decimal_places=1, max_digits=2)
    movie = serializers.StringRelatedField(many=False)