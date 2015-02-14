'''
James Stanbridge
13 Feb 2015
Design Patterns for Web programming
Simple Form
'''

import webapp2
from pages import Page



class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()

        page_head = p.head
        page_body = p.form
        page_close = p.close

        self.response.write(page_head + page_body + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
