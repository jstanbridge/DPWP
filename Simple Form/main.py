'''
James Stanbridge
13 Feb 2015
Design Patterns for Web programming
Simple Form
'''

import webapp2 #import that GoogleAppLauncher includes
from pages import Page #import our class "Page()" from pages.py

class MainHandler(webapp2.RequestHandler): #main class that runs our python script
    def get(self):

        p = Page() #set our Page() class equal to p, this makes it easier to type out

        page_head = p.head #set the self.head attribute in Page() equal to the variable page_head for later use
        page_form = p.form #set the self.form attribute in Page() equal to the variable page_form for later use
        page_close = p.close #set the self.close attribute in Page() equal to the variable page_close for later use
        page_results = p.results #set the self.results attribute in Page() equal to the variable page_results for later use

        if self.request.GET: #start the if/else that will determine what to write to the browser depending on user input or lack of input, in this case, when user inputs we:
            username = self.request.GET['su_name'] #set the input value of the form field su_name equal to username
            god = self.request.GET['fav_god'] #set the input value of the form field fav_god equal to username
            role = self.request.GET['role'] #set the input value of the form field role equal to username
            mode = self.request.GET['game_mode'] #set the input value of the form field game_mode equal to username
            self.response.write(page_head + page_results + "<p class='results'>" + username + " | " + god + " | " + role + " | " + mode + "</p>" + page_close)
            #In the above line, we concatenate everything we want the page to write if the user has entered input.
            #We write the page_head html, followed by the page_results html, then we write the entered username/god/role/mode and wrap it in a <p> tag
            #with a class of 'results'. Finally, we add the page_close html, completing the web page.
        else:
            self.response.write(page_head + page_form + page_close)
            #The above line is what is written to the page if the user has not submitted any input via the form.
            #In this case, we print the page_head and page_close html like we did above, but we include the page_form html instead of the results and input responses.

#below is the thing that we are never supposed to touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
