import tmdb_client
from unittest.mock import Mock
from main import app

# def test_get_poster_url_uses_default_size():
#     # Przygotowanie danych
#     poster_api_path = "some-poster-path"
#     expected_default_size = 'w342'
#     # Wywołanie kodu, który testujemy
#     poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
#     # Porównanie wyników
#     assert expected_default_size in poster_url

# def test_get_movies_list_type_popular():
#     movies_list = tmdb_client.get_movies_list(list_type="popular")
#     assert movies_list is not None

def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking():
   result = some_function_to_mock()

def test_mocking(monkeypatch):
    my_mock = Mock()
    my_mock.return_value = 2
    monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
    result = some_function_to_mock()
    assert result == 2

def test_get_movies_list(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    print(response)
    # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movies_list(list_type="popular")
    print(movies_list)
    assert movies_list == mock_movies_list

def test_homepage(monkeypatch):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        api_mock.assert_called_once_with('movie/popular')