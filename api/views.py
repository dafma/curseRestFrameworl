from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import USerSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Movie

from .serializers import USerSerializer, GroupSerializer, MovieSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class USerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = USerSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #authentication_classes = (TokenAuthentication, SessionAuthentication)
    #permission_classes = (IsAuthenticated,)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        serializer = USerSerializer(user, many = False)
        return Response({'token':token.key, 'user': serializer.data})

class GroupViewSet(viewsets.ModelViewSet):
    queryset =  Group.objects.all()
    serializer_class = GroupSerializer