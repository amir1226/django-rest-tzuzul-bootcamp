from rest_framework import serializers

from reviews.serializers import ReviewMovieSerializer
from .models import Movie

class ModelSerializer(serializers.ModelSerializer):
    reviews = ReviewMovieSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'