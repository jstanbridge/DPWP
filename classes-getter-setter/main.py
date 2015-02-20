import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "MyPage"
        p.css = "css/styles.css"
        self.response.write(p.whole_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
