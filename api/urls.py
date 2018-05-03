
from django.contrib import admin
from django.urls import path, include
from  rest_framework import  routers
from api.views import USerViewSet, MovieViewSet
from .views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', USerViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('authenticate/', CustomObtainAuthToken.as_view()),
]
