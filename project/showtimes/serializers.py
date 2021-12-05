from showtimes.models import Cinema, Screening
from movielist.models import Movie
from rest_framework import serializers


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-detail',
    )

    # def transform_movies(self, movies):
    #     return movies.filter(y)

    class Meta:
        model = Cinema
        fields = ['name', 'city', 'movies']


class ScreeningSerializer(serializers.ModelSerializer):
    cinema = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Cinema.objects.all()
    )
    movie = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Movie.objects.all()
    )

    class Meta:
        model = Screening
        fields = ['cinema', 'movie', 'date']