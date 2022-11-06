from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

login_view = MyTokenObtainPairView.as_view()