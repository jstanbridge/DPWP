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
        page_form = p.form
        page_close = p.close
        page_results = p.results

        if self.request.GET:
            username = self.request.GET['su_name']
            god = self.request.GET['fav_god']
            role = self.request.GET['role']
            mode = self.request.GET['game_mode']
            self.response.write(page_head + page_results + "<p class='results'>" + username + " | " + god + " | " + role + " | " + mode + "</p>" + page_close)
        else:
            self.response.write(page_head + page_form + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
