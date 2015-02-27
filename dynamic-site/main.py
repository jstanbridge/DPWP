"""
James Stanbridge
26 Feb 2014
Dynamic Site
"""

import webapp2
from page import Page
from data import Movie, Data

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()
        m = Movie()
        d = Data()

        if self.request.GET:
            genre = self.request.GET['genre']

            if genre == 'fantasy':
                p.item = 'fantasy'
            elif genre == 'sci-fi':
                p.item = 'sci-fi'
            elif genre == 'historical':
                p.item = 'historical'
            elif genre == 'romance':
                p.item = 'romance'
            elif genre == 'environmental':
                p.item = 'environmental'

            print genre

        else:
            pass

        self.response.write(p.print_out())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
