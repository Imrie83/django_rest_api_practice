from django.shortcuts import render, HttpResponse
from rest_framework import generics
from django.views import View
from .models import Cinema, Screening
from .serializers import CinemaSerializer, ScreeningSerializer
from django_filters import rest_framework as filters


class CinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class ScreeningView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer


class ScreeningListView(generics.ListCreateAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
    filterset_fields = ['movie', 'cinema']
