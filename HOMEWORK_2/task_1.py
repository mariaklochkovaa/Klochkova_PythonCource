import requests
from datetime import datetime, timedelta
import csv


class MovieData:
    def __init__(self, num_pages):
        self.num_pages = num_pages
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMTI3NGFmYTRlNTUyMjRjYzRlN2Q0NmNlMTNkOTZjOSIsInN1YiI6IjVkNmZhMWZmNzdjMDFmMDAxMDU5NzQ4OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lbpgyXlOXwrbY0mUmP-zQpNAMCw_h-oaudAJB6Cn5c8"
        }
        self.movie_data = []
        self.movie_data_copy = []
        self.genre_data = {}

        self.fetch_movie_data()
        self.fetch_genre_data()

    # 1. Fetch the data from desired amount of pages
    def fetch_movie_data(self):
        for page in range(1, self.num_pages + 1):
            url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&sort_by=popularity.desc&page={page}"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                self.movie_data.extend(data.get("results", []))
            else:
                print(f"Failed to fetch data from page {page}")

    # Отримуємо дані про жанри
    def fetch_genre_data(self):
        url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            for genre in data.get("genres", []):
                self.genre_data[genre['id']] = genre['name']
        else:
            print('Failed to fetch genre data.')

    #  2. Give a user all data
    def get_all_data(self):
        return self.movie_data

    #  3. All data about movies with indexes from 3 till 19 with step 4
    def get_data_slice(self):
        return self.movie_data[3:20:4]

    #  4. Name of the most popular title
    def get_most_popular_title(self):
        most_popular_movie = max(self.movie_data, key=lambda x: x.get('popularity', 0))
        return most_popular_movie.get('title')

    # 5. Names of titles which has in description key words which a user put as parameters
    def get_titles_with_keyword(self, keyword):
        return [movie['title'] for movie in self.movie_data if keyword in movie.get('overview', '')]

    #  6. Unique collection of present genres (the collection should not allow inserts)
    def get_unique_genres(self):
        return set(self.genre_data.values())

    # 7. Delete all movies with user provided genre
    def delete_by_genre(self, genre_name):
        genre_id = None
        for id, name in self.genre_data.items():
            if name.lower() == genre_name.lower():
                genre_id = id
                break
        if genre_id:
            self.movie_data = [movie for movie in self.movie_data if genre_id not in movie.get('genre_ids', [])]
        else:
            print(f"Genre '{genre_name}' not found.")

    # 8. Names of most popular genres with numbers of time the appear in the data
    def get_most_popular_genres(self):
        genre_count = {}
        for movie in self.movie_data:
            for genre_id in movie.get('genre_ids', []):
                if genre_id in genre_count:
                    genre_count[genre_id] += 1
                else:
                    genre_count[genre_id] = 1
        popular_genres = [(self.genre_data[genre_id], count) for genre_id, count in genre_count.items()]
        popular_genres.sort(key=lambda x: x[1], reverse=True)
        return popular_genres

    # 9. Collection of film titles  grouped in pairs by common genres (the groups should not allow inserts)
    def get_pairs_by_common_genres(self):
        titles_by_genre = {}
        for movie in self.movie_data:
            for genre_id in movie.get('genre_ids', []):
                genre_name = self.genre_data.get(genre_id)
                if genre_name:
                    if genre_name not in titles_by_genre:
                        titles_by_genre[genre_name] = []
                    titles_by_genre[genre_name].append(movie['title'])
        return titles_by_genre

    # 10. Return initial data and copy of initial data where first id in list of film genres was replaced with 22
    def modify_list_of_genres(self):
        self.movie_data_copy = self.movie_data.copy()
        self.movie_data_copy[0]['genre_ids'][0] = 22

    # 11. Collection of structures
    def get_movie_structures(self):
        movie_structures = []
        for movie in self.movie_data:
            structure = {
                'Title': movie.get('title', ''),
                'Popularity': round(movie.get('popularity', 0), 1),
                'Score': int(movie.get('vote_average', 0)),
                'Last_day_in_cinema': (
                        datetime.strptime(movie.get('release_date', ''), "%Y-%m-%d") + timedelta(days=77)).strftime(
                    "%Y-%m-%d")
            }
            movie_structures.append(structure)
        movie_structures.sort(key=lambda x: (x['Score'], x['Popularity']), reverse=True)
        return movie_structures

    # 12. Write information from previous step to a csv file using path provided by user
    def write_to_csv(self, path):
        movie_structures = self.get_movie_structures()
        with open(path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for structure in movie_structures:
                writer.writerow(structure.items())


obj = MovieData(num_pages=3)

print(f' get all data: {obj.get_all_data()}')

print(f'get data slice:{obj.get_data_slice()}')

print(f'get most popular title:{obj.get_most_popular_title()}')

print(f'get titles with keyword("story"):{obj.get_titles_with_keyword("story")}')

print(f'get unique genres: {obj.get_unique_genres()}')

obj.delete_by_genre("Action")

print(f'get most popular genres: {obj.get_most_popular_genres()}')

print(f'get_pairs_by_common_genres: {obj.get_pairs_by_common_genres()}')

obj.modify_list_of_genres()
print(f'movie data copy: {obj.movie_data_copy}')

print(f'get movie structures: {obj.get_movie_structures()}')

obj.write_to_csv("movie_data.csv")
