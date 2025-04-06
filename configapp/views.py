
from rest_framework.views import APIView
from .serializers import *
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Movie, Actors, CommitMovie


class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]


class ActorCreateView(generics.CreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated]


class MovieViewSet(GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def add_actor(self, request, pk=None):
        movie = self.get_object()
        actor_id = request.data.get("actor_id")
        actor = get_object_or_404(Actors, id=actor_id)
        movie.actor.add(actor)
        return Response({"message": "Actor added successfully"}, status=status.HTTP_200_OK)


class CommitApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = {"success": True}
        commits = CommitMovie.objects.filter(author=request.user)  # Faqat o‘zining commitlari
        serializer = CommitSerializer(commits, many=True)
        response['data'] = serializer.data
        return Response(data=response)

    def post(self, request):
        response = {"success": True}
        serializer = CommitSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)  # Token orqali author
            response['data'] = serializer.data
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# from rest_framework.views import APIView
# from .serializers import *
# from rest_framework import generics, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.viewsets import GenericViewSet
# from django.shortcuts import get_object_or_404
# from .models import *
# from .serializers import MovieSerializer, ActorSerializer
#
#
#
# class MovieCreateView(generics.CreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#
# class ActorCreateView(generics.CreateAPIView):
#     queryset = Actors.objects.all()
#     serializer_class = ActorSerializer
#
#
# class MovieViewSet(GenericViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#     @action(detail=True, methods=['post'])
#     def add_actor(self, request, pk=None):
#         movie = self.get_object()
#         actor_id = request.data.get("actor_id")
#         actor = get_object_or_404(Actors, id=actor_id)
#         movie.actor.add(actor)
#         return Response({"message": "Actor added successfully"}, status=status.HTTP_200_OK)
#
# class CommitApi(APIView):
#     def get(self,request):
#         response={"success":True}
#         commit=CommitMovie.objects.all()
#         serializer=CommitSerializer(commit,many=True)
#         response['data']=serializer.data
#         return Response(data=response)
#     def post(self,request):
#         response={"success":True}
#         serializer=CommitSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             response['data']=serializer.data
#             return Response(data=response)
#         return Response(data=serializer.data)
