# from rest_framework import serializers
# from .models import Cinema
#
#
# class CinemaSerializer(serializers.ModelSerializer):
#     movies = serializers.HyperlinkedRelatedField(
#         many=True,
#         read_only=True,
#         view_name='movie-detail'
#     )
#
#     class Meta:
#         model = Cinema
#         fields = ['name', 'city', 'movies']

from showtimes.models import Cinema, Screening
from rest_framework import serializers


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-detail'
    )
    class Meta:
        model = Cinema
        fields = ['name', 'city', 'movies']


