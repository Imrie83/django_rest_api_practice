from django.shortcuts import render, HttpResponse
from rest_framework import generics
from django.views import View
from .models import Cinema, Screening
from .serializers import CinemaSerializer


class CinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer