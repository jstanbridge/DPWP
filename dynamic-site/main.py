"""
James Stanbridge
26 Feb 2014
Dynamic Site
"""

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
