# from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import reviews.models
from movies.models import Movie
from .models import Review
from .serializers import ReviewSerializer, ReviewSerializerFirst
from rest_framework.generics import ListAPIView
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

@api_view(['GET'])
def get_reviews(request):
    reviews = Review.objects.all()
    movie_name = request.query_params.get('movie')
    if movie_name is not None:
        movie = Movie.objects.filter(titulo=movie_name).first()
        reviews = reviews.filter(movie=movie)
    count = reviews.count()
    reviews_serializer = ReviewSerializerFirst(reviews, many=True)
    response = {"reviews":reviews_serializer.data,"count":count}
    return Response(response)

@api_view()
def get_all_reviews(request):
    reviews = Review.objects.all()
    review_serialized = ReviewSerializer(reviews, many=True)
    return Response(review_serialized.data)

#Más sencillo pero menos control
class AllReviews(ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()
        movie_name = self.request.query_params.get('movie')
        if movie_name is not None:
            movie = Movie.objects.filter(titulo=movie_name).first()
            queryset = queryset.filter(movie=movie)
        return queryset

class ReviewsViewSet(ModelViewSet):
    queryset = Review.objects
    serializer_class = ReviewSerializerFirst

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        movie_name = self.request.query_params.get('movie')
        if movie_name is not None:
            movie = Movie.objects.filter(titulo=movie_name).first()
            queryset = self.queryset.filter(movie=movie)
        return queryset

class Login(APIView):
    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if not user:
            return Response({"error":"Credenciales incorrectas"}, status=HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=HTTP_200_OK)


def paginaPrincipal(request):
    return render(request,"inicio.html")