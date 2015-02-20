'''
James Stanbridge
19 Feb 2015
Reusable Library
'''

import webapp2
from library import PlayerData, TeamData
from pages import ResultsPage, FormPage

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = ResultsPage()

        t = TeamData()


        p1 = PlayerData()
        p1.name = 'One'
        p1.kills = 6
        p1.assists = 0
        p1.deaths = 4
        p1.heals = 0
        p1.abs = 2
        t.add_player(p1)

        p2 = PlayerData()
        p2.name = 'Two'
        p2.kills = 12
        p2.assists = 0
        p2.deaths = 7
        p2.heals = 14
        p2.abs =10
        t.add_player(p2)

        if self.request.GET:
            pass
        #p.body = t.player_list() + t.calc_kills() + t.calc_deaths() + t.calc_abs() + t.calc_heals()
        else:
            p = FormPage()
            self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
