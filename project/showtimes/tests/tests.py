import pytest

from movielist.models import Movie, Person
from showtimes.models import Cinema, Screening
from movielist.tests.utils import fake_movie_data, random_person
from showtimes.tests.utils import fake_cinema_data


@pytest.mark.django_db
def test_add_cinema(client, set_up):
    cinemas_count = Cinema.objects.count()
    new_cinema = fake_cinema_data()
    response = client.post("/cinemas/", new_cinema, format='json')
    assert response.status_code == 201
    assert Cinema.objects.count() == cinemas_count + 1
    for key, value in new_cinema.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_get_cinema_list(client, set_up):
    response = client.get('/cinemas/', {}, format='json')

    assert response.status_code == 200
    assert Cinema.objects.count() == len(response.data)


@pytest.mark.django_db
def test_get_cinema_detail(client, set_up):
    cinema = Cinema.objects.first()
    response = client.get(f'/cinemas/{cinema.id}/', {}, format='json')

    assert response.status_code == 200
    for field in ('name', 'city', 'movies'):
        assert field in response.data


@pytest.mark.django_db
def test_delete_cinema(client, set_up):
    cinema_count = Cinema.objects.count()
    cinema = Cinema.objects.first()
    response = client.delete(f'/cinemas/{cinema.id}/', {}, format='json')
    cinema_ids = [cinema.id for cinema in Cinema.objects.all()]

    assert response.status_code == 204
    assert Cinema.objects.count() == cinema_count - 1
    assert cinema.id not in cinema_ids


@pytest.mark.django_db
def test_update_cinema(client, set_up):
    cinema = Cinema.objects.first()
    response = client.patch(
        f'/cinemas/{cinema.id}/', {'name': 'new_test_name'}, format='json'
    )
    assert response.status_code == 200
    assert cinema.name != response.data['name']
    assert response.data['name'] == 'new_test_name'