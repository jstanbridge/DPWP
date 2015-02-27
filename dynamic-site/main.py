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
                m = d.list[0]
                print m.title
            elif genre == 'sci-fi':
                p.item = 'sci-fi'
                m = d.list[1]
                print m.title
            elif genre == 'historical':
                p.item = 'historical'
                m = d.list[2]
                print m.title
            elif genre == 'romance':
                p.item = 'romance'
                m = d.list[3]
                print m.title
            elif genre == 'environmental':
                p.item = 'environmental'
                m = d.list[4]
                print m.title

        else:
            pass

        #print d.list[0].title

        self.response.write(p.print_out())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
