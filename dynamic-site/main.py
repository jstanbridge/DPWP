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

        p = Page()
        c = ContentPage()
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

        c._title = m.title
        c._image = m.image
        c._time = m.time
        c._studio = m.studio
        c._year = m.year
        c._genre = m.genre
        c._director = m.director
        print c._title

        p.item = '<img src="' + m.image + '" />' + m.title + str(m.time) + m.studio + str(m.year) + m.genre + m.director

        self.response.write(p.print_out())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
