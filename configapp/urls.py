from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieCreateView, ActorCreateView, MovieViewSet


router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = [
    path('movies/create/', MovieCreateView.as_view(), name='movie-create'),
    path('actors/create/', ActorCreateView.as_view(), name='actor-create'),
    path('', include(router.urls)),
]

