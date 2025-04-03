from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework.generics import CreateAPIView
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import MovieSerializer, ActorSerializer


class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ActorCreateView(generics.CreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['post'])
    def add_actor(self, request, pk=None):
        movie = self.get_object()
        actor_id = request.data.get("actor_id")
        actor = get_object_or_404(Actor, id=actor_id)
        movie.actor.add(actor)
        return Response({"message": "Actor added successfully"}, status=status.HTTP_200_OK)


