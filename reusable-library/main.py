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

        t = TeamData()

        if self.request.GET:
            p1 = PlayerData()
            p1.name = self.request.GET['p1_name']
            p1.kills = int(self.request.GET['p1_kills'])
            p1.assists = int(self.request.GET['p1_deaths'])
            p1.deaths = int(self.request.GET['p1_assists'])
            p1.heals = int(self.request.GET['p1_heals'])
            p1.abs = int(self.request.GET['p1_abs'])
            t.add_player(p1)

            p2 = PlayerData()
            p2.name = self.request.GET['p2_name']
            p2.kills = int(self.request.GET['p2_kills'])
            p2.assists = int(self.request.GET['p2_deaths'])
            p2.deaths = int(self.request.GET['p2_assists'])
            p2.heals = int(self.request.GET['p2_heals'])
            p2.abs = int(self.request.GET['p2_abs'])
            t.add_player(p2)

            p3 = PlayerData()
            p3.name = self.request.GET['p3_name']
            p3.kills = int(self.request.GET['p3_kills'])
            p3.assists = int(self.request.GET['p3_deaths'])
            p3.deaths = int(self.request.GET['p3_assists'])
            p3.heals = int(self.request.GET['p3_heals'])
            p3.abs = int(self.request.GET['p3_abs'])
            t.add_player(p3)

            p4 = PlayerData()
            p4.name = self.request.GET['p4_name']
            p4.kills = int(self.request.GET['p4_kills'])
            p4.assists = int(self.request.GET['p4_deaths'])
            p4.deaths = int(self.request.GET['p4_assists'])
            p4.heals = int(self.request.GET['p4_heals'])
            p4.abs = int(self.request.GET['p4_abs'])
            t.add_player(p4)

            p5 = PlayerData()
            p5.name = self.request.GET['p5_name']
            p5.kills = int(self.request.GET['p5_kills'])
            p5.assists = int(self.request.GET['p5_deaths'])
            p5.deaths = int(self.request.GET['p5_assists'])
            p5.heals = int(self.request.GET['p5_heals'])
            p5.abs = int(self.request.GET['p5_abs'])
            t.add_player(p5)

            p = ResultsPage()
            p.body = t.player_list() + t.calc_kills() +  t.calc_deaths() + t.calc_abs() + t.calc_heals()
            self.response.write(p.print_out())
        else:
            p = FormPage()
            self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
