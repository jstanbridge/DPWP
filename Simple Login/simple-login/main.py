'''
James Stanbridge
13 Feb 2015
Design Patterns for Web programming
Simple Login
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Login</title>
    </head>
    <body>'''


        page_body ='''<form method="GET">
            <label>Name: </label><input type="text" name="user" />
            <label>Email: </label><input type="text" name="email" />
            <input type="submit" value="Submit" />'''

        page_close = '''
        </form>
    </body>
</html>
        '''
        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' ' + email + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
