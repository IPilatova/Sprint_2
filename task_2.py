class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f"Комедии: '{self.movies}'" # список взят в '', так как это требуется по заданию -  возвращать записи вида Комедии: '[]' и Драмы: '[]' соответственно)

class Drama(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f"Драмы: '{self.movies}'" # список взят в '', так как это требуется по заданию -  возвращать записи вида Комедии: '[]' и Драмы: '[]' соответственно)


comedy = Comedy()
print(comedy.add_movie('Большой куш'))

drama = Drama()
print(drama.add_movie('Оружейный барон'))