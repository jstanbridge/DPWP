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

    def calc_abs(self):
        abs = []
        for player in self.__team_list:
            abs.append(player.abs)
        abs.sort()
        top_abs = len(abs) - 1
        abs_diff = abs[top_abs] - abs[0]
        return 'Your top defender absorbed ' + str(abs_diff) + ' more damage than your lowest defender.'

    def calc_heals(self):
        heals = []
        for player in self.__team_list:
            heals.append(player.heals)
        abs = []
        for player in self.__team_list:
            abs.append(player.abs)
        total_heals = sum(heals)
        total_abs = sum(abs)
        if total_heals > total_abs:
            return "Your team healed more damage than they mitigated."
        elif total_heals == total_abs:
            return "Your team healed as much damage as they mitigated."
        else:
            return "Your team healed less damage than they mitigated."