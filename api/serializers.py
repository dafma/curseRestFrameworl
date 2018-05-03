from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Movie


class USerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'password')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ( 'title', 'description')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields  = ('url', 'name')