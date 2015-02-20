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

        m = PlayerData()
        t = TeamData()


        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.year = 1989
        md1.director = "Rob Reiner"
        lib.add_movie(md1)

        md2 = MovieData()
        md2.title = "Dune"
        md2.year = 1986
        md2.director = "David Lynch"
        lib.add_movie(md2)

        md3 = MovieData()
        md3.title = "Star Wars"
        md3.year = 1977
        md3.director = "George Lucas"
        lib.add_movie(md3)


        p.body = lib.compile_list() + lib.calc_time_span()
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
