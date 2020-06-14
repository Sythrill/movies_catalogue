import requests
import os

API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")

def get_movies():
    url = "https://api.themoviedb.org/3/movie/popular"
    api_token = API_TOKEN
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(url, headers = headers)
    json_response = response.json()
    return json_response

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_number_of_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = API_TOKEN
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")

def search(search_query):
    base_url = "https://api.themoviedb.org/3/"
    headers = {
       "Authorization": f"Bearer {API_TOKEN}"
    }
    endpoint = f"{base_url}search/movie/?query={search_query}"
    response = requests.get(endpoint, headers=headers)
    response = response.json()
    return response['results']

def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()