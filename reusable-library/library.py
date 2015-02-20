class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []

    def add_movie(self, m):
        self.__movie_list.append(m)
        print m.title

    def compile_list(self):
        output = ''
        for movie in self.__movie_list:
            output += 'Title: ' + movie.title + ' (' + str(movie.year) + ')' + '<br />'
        return output

    def calc_time_span(self):
        years = []
        for movie in self.__movie_list:
            years.append(movie.year)

        years.sort()

        num = len(years) - 1
        span = years[num] - years[0]

        return 'The span between films entered is ' + str(span)


class MovieData(object):
    def __init__(self):
        self.title = ''
        self.__year = 0
        self.director = ''

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if new_year > 2015:
           print "Error, invalid year!"
           self.__year = 2014
        else:
            self.__year = new_year


#add class for player data
class PlayerData(object):
    def __init__(self):
        self.__kills = 0
        self.__assists = 0
        self.__deaths = 0
        self.__heals = 0
        self.__abs = 0

#add class for team data

class TeamData(object):
    def __init__(self):
        self.__team_list = []