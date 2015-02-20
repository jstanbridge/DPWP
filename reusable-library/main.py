'''
James Stanbridge
19 Feb 2015
Reusable Library
'''

import webapp2
from library import MovieData, FavoriteMovies, PlayerData, TeamData
from pages import ResultsPage

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = ResultsPage()
        lib = FavoriteMovies()

        t = TeamData()


        p1 = PlayerData()
        p.name = 'One'
        p1.kills = 0
        p1.assists = 0
        p1.deaths = 0
        p1.heals = 0
        p1.abs = 0
        t.add_player(p1)

        p2 = PlayerData()
        p.name = 'Two'
        p2.kills = 0
        p2.assists = 0
        p2.deaths = 0
        p2.heals = 0
        p2.abs = 0
        t.add_player(p2)


        p.body = lib.compile_list() + lib.calc_time_span()
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
