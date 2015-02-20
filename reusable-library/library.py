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


#add class for player data
class PlayerData(object):
    def __init__(self):
        self.__name = ''
        self.__kills = 0
        self.__assists = 0
        self.__deaths = 0
        self.__heals = 0
        self.__abs = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, p_name):
        self.__name = p_name

    @property
    def kills(self):
        return self.__kills

    @kills.setter
    def kills(self, p_kills):
        self.__kills = p_kills

    @property
    def assists(self):
        return self.__assists

    @assists.setter
    def assists(self, p_assists):
        self.__assists = p_assists

    @property
    def deaths(self):
        return self.__deaths

    @deaths.setter
    def deaths(self, p_deaths):
        self.__deaths = p_deaths

    @property
    def heals(self):
        return self.__heals

    @heals.setter
    def heals(self, p_heals):
        self.__heals = p_heals

    @property
    def abs(self):
        return self.__abs

    @abs.setter
    def abs(self, p_abs):
        self.__abs = p_abs

#add class for team data

class TeamData(object):
    def __init__(self):
        self.__team_list = []

    def add_player(self, p):
        self.__team_list.append(p)
        print p.name

    def player_list(self):
        output = ''
        for player in self.__team_list:
            output += 'Name: ' + player.name + '<br />' + str(player.kills) + '/' + str(player.deaths) + '/' + str(player.assists) + '/' + str(player.heals) + '/' + str(player.abs) + '<br />'
        return output

    def calc_kills(self):
        kills = []
        for player in self.__team_list:
            kills.append(player.kills)
        top_kills = sum(kills)
        return 'Your team got ' + str(top_kills) + ' kills in this game.'

    def calc_deaths(self):
        deaths = []
        for player in self.__team_list:
            deaths.append(player.deaths)
        average_deaths = (sum(deaths))/len(deaths)
        return 'Your team averaged ' + str(average_deaths) + ' deaths in this game.'