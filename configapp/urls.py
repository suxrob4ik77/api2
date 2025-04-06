

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, MovieCreateView, ActorCreateView, CommitApi

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = [
    path('movies/create/', MovieCreateView.as_view(), name='movie-create'),
    path('actors/create/', ActorCreateView.as_view(), name='actor-create'),
    path('commit/', CommitApi.as_view(), name='commit-api'),  # Qo'shtirnoq va trailing slash
    path('', include(router.urls)),
]




# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
#
#
# from .views import *
#
#
# router = DefaultRouter()
# router.register(r'movies', MovieViewSet, basename='movie')
#
# urlpatterns = [
#     path('movies/create/', MovieCreateView.as_view(), name='movie-create'),
#     path('actors/create/', ActorCreateView.as_view(), name='actor-create'),
#     path('commit',CommitApi.as_view()),
#     path('', include(router.urls)),
# ]
#
