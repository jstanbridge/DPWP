#the class is created to gather and store data from the user via form inputs
class PlayerData(object):
    def __init__(self):
        #each of these attributes is private and given a value from a specific form field
        self.__name = ''
        self.__kills = 0
        self.__assists = 0
        self.__deaths = 0
        self.__heals = 0
        self.__abs = 0

    #here (and in each @property below) we are creating a getter for our data values so they can be access by our other functions
    @property
    def name(self):
        return self.__name

    #here (and in each .setter below) we are creating a setter so that outside functions can change the values of the data contained in our PlayerData class
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

#this class handles calculations using data from the PlayerData class
class TeamData(object):
    def __init__(self):
        #here we create an array to store information from the PlayerData class
        self.__team_list = []

    #this function adds each player's name attribute to a list and then prints it
    def add_player(self, p):
        self.__team_list.append(p)
        print p.name

    #this function takes all the data from each other calculation in our TeamData function and prints it, adding in a few html elements that are handle via our css file
    def player_list(self):
        output = ''
        for player in self.__team_list:
            output += '<div class="pinfo">' + '<h2>' + player.name + '</h2>' + '<p>' + str(player.kills) + '/' + str(player.deaths) + '/' + str(player.assists) + '/' + str(player.heals) + '/' + str(player.abs) + '</p>' + '</div>'
        return output

    #this function creates an array and then adds the value of each players kill number to it. then, it totals the kills and returns/prints the value.
    def calc_kills(self):
        kills = []
        for player in self.__team_list:
            kills.append(player.kills)
        top_kills = sum(kills)
        return '<div id="stats">' + '<p>' + 'Your team got ' + str(top_kills) + ' kills in this game.' + '</p>'

    #this function creates an array and then adds the total value of each players death count to it. then it adds them together and divides it by the length of the array to calculate and average. it then returns/prints the average.
    def calc_deaths(self):
        deaths = []
        for player in self.__team_list:
            deaths.append(player.deaths)
        average_deaths = (sum(deaths))/len(deaths)
        return '<p>' + 'Your team averaged ' + str(average_deaths) + ' deaths in this game.' + '</p>'

    #this function creates an array and then adds the value of each players damage mitigated to it. then it sorts the array from lowest to highest and compares the highest and lowest numbers, calculates the difference, and the returns/prints the difference.
    def calc_abs(self):
        abs = []
        for player in self.__team_list:
            abs.append(player.abs)
        abs.sort()
        top_abs = len(abs) - 1
        abs_diff = abs[top_abs] - abs[0]
        return '<p>' + 'Your top defender absorbed ' + str(abs_diff) + ' more damage than your lowest defender.' + '</p>'

    #this function creates and array and then adds the total value of players heals to it, and creates a second array that adds the total value of player damage mitigated to it. then, it compares the two values and based on the results, returns/prints a relevant string.
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
            return '<p>' + "Your team healed more damage than they mitigated." + '</p>' + '</div>'
        elif total_heals == total_abs:
            return '<p>' + "Your team healed as much damage as they mitigated." + '</p>' + '</div>'
        else:
            return '<p>' + "Your team healed less damage than they mitigated." + '</p>' + '</div>'