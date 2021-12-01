from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from movies.models import Movie
from movies.serializers import ModelSerializer
from reviews.models import Review


class MoviesViewSet(ModelViewSet):
    queryset = Movie.objects
    serializer_class = ModelSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        review_id = self.request.query_params.get('review_id')
        if review_id is not None:
            review = Review.objects.filter(id=review_id).first()
            queryset = self.queryset.filter(reviews=review)
        return queryset
