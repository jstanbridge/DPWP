"""
James Stanbridge
26 Feb 2014
Dynamic Site
"""

import webapp2
from page import Page
from data import *

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()

        self.response.write(p.print_out())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
