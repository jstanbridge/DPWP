"""
James Stanbridge
26 Feb 2014
Dynamic Site
"""

import webapp2
#import classes from our other .py files
from page import ContentPage
from data import Movie, Data

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #create instances for the classes we imported
        p = ContentPage()
        m = Movie()
        d = Data()

        #if we have user input or, in this case, some piece of data in the url
        if self.request.GET:
            #then we check for the genre since that's what we're using to determine what gets shown on the page
            genre = self.request.GET['genre']

            #depending on which genre is there, we set Movie() equal to one of our objects in the Data() function
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
        #if nothing has been sent, then we pass and the user will only see the default page which shows the first item in our Data() object
        else:
            m = d.list[0]


        #here we are setting the html elements in our page.py file to equal data from our data.py file
        p._title = m.title
        p._image = m.image
        p._time = m.time
        p._studio = m.studio
        p._year = m.year
        p._genre = m.genre
        p._director = m.director

        #here we call the print_out function to write everything to the page
        self.response.write(p.print_out())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
