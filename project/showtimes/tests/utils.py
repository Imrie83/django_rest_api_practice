from random import sample
from faker import Faker
# from project.moviebase import TIME_ZONE
from movielist.models import Movie
from showtimes.models import Cinema, Screening
import pytz
from pytz import timezone

faker = Faker("pl_PL")
tz = timezone('Europe/Warsaw')


def random_movies():
    """Return 3 random Movies from db."""
    movies = list(Movie.objects.all())
    return sample(movies, 3)


def add_screenings(cinema):
    """Add 3 screenings for given cinema."""
    movies = random_movies()
    for movie in movies:
        Screening.objects.create(cinema=cinema, movie=movie, date=faker.date_time(tzinfo=tz))


def fake_cinema_data():
    """Generate fake data for cinema."""
    return {
        "name": faker.name(),
        "city": faker.city(),
    }


def create_fake_cinema():
    """Create fake cinema with some screenings."""
    cinema = Cinema.objects.create(**fake_cinema_data())
    add_screenings(cinema)