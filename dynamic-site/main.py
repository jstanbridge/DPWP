"""
James Stanbridge
26 Feb 2014
Dynamic Site
"""

import webapp2
from page import Page, ContentPage
from data import Movie, Data

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = ContentPage()
        m = Movie()
        d = Data()

        if self.request.GET:
            genre = self.request.GET['genre']

            if genre == 'fantasy':
                m = d.list[0]
            elif genre == 'sci-fi':
                m = d.list[1]
            elif genre == 'historical':
                m = d.list[2]
            elif genre == 'romance':
                m = d.list[3]
            elif genre == 'environmental':
                m = d.list[4]

        else:
            pass

        p._title = m.title
        p._image = m.image
        p._time = m.time
        p._studio = m.studio
        p._year = m.year
        p._genre = m.genre
        p._director = m.director
        print p._div_start

        #p.item = '<img src="' + m.image + '" />' + m.title + str(m.time) + m.studio + str(m.year) + m.genre + m.director

        self.response.write(p.print_out())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
