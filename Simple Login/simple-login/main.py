import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button()
        about_button.label = "About Us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "Contact Us"
        contact_button.show_label()

class Button(object):
    def __init__(self):
        self.label = ""
        self.__size = 60
        self._color = "0x00000"
        #self.on_roll_over("Hello!!")

    def click(self):
        print "I've been clicked!"

    def on_roll_over(self, message):
        print "You've rolled over me!" + message

    def show_label(self):
        print "My label is " + self.label

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
