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
            #p1 = PlayerData()
            #p1.name = self.request.GET['p1_name']
            #p1.kills = self.request.GET['p1_kills']
            #p1.assists = self.request.GET['p1_deaths']
            #p1.deaths = self.request.GET['p1_assists']
            #p1.heals = self.request.GET['p1_heals']
            #p1.abs = self.request.GET['p1_abs']
            #t.add_player(p1)

            #p2 = PlayerData()
            #p2.name = self.request.GET['p2_name']
            #p2.kills = self.request.GET['p2_kills']
            #p2.assists = self.request.GET['p2_deaths']
            #p2.deaths = self.request.GET['p2_assists']
            #p2.heals = self.request.GET['p2_heals']
            #p2.abs = self.request.GET['p2_abs']
            #t.add_player(p2)

            #p3 = PlayerData()
            #p3.name = self.request.GET['p3_name']
            #p3.kills = self.request.GET['p3_kills']
            #p3.assists = self.request.GET['p3_deaths']
            #p3.deaths = self.request.GET['p3_assists']
            #p3.heals = self.request.GET['p3_heals']
            #p3.abs = self.request.GET['p3_abs']
            #t.add_player(p3)

            #p4 = PlayerData()
            #p4.name = self.request.GET['p4_name']
            #p4.kills = self.request.GET['p4_kills']
            #p4.assists = self.request.GET['p4_deaths']
            #p4.deaths = self.request.GET['p4_assists']
            #p4.heals = self.request.GET['p4_heals']
            #p4.abs = self.request.GET['p4_abs']
            #t.add_player(p4)

            #p5 = PlayerData()
            #p5.name = self.request.GET['p5_name']
            #p5.kills = self.request.GET['p5_kills']
            #p5.assists = self.request.GET['p5_deaths']
            #p5.deaths = self.request.GET['p5_assists']
            #p5.heals = self.request.GET['p5_heals']
            #p5.abs = self.request.GET['p5_abs']
            #t.add_player(p5)

            #p.body = t.player_list() + t.calc_kills() + t.calc_deaths() + t.calc_abs() + t.calc_heals()
        else:
            p = FormPage()
            self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
