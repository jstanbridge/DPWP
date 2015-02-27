"""
James Stanbridge
26 Feb 2014
Dynamic Site
"""

#create the Page class, which is a generic class to create the basis of our htm layout
class Page(object):
    def __init__(self):
        #define head attribute to contain all head html info
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
          <title>Dynamic Site</title>
          <link type="text/css" href="css/styles.css" rel="Stylesheet>
    </head>

    <body>
        '''

        #define body attribute to contain body html that will be on every page
        self._body = '''
        <div id="container">
            <ul id="menu">
                <li><a href="?genre=fantasy">The Cat Returns</a></li>
                <li><a href="?genre=sci-fi">The Girl Who Leapt Through Time</a></li>
                <li><a href="?genre=historical">Sword of the Stranger</a></li>
                <li><a href="?genre=romance">5 Centimeters Per Second</a></li>
                <li><a href="?genre=environmental">Origin: Spirits of the Past</a></li>
            </ul>
        '''

        #define close attribute to contain all closing tags that will be on each page + footer
        self._close = '''
            <footer>
                <p>Some cool footer stuff</p>
            </footer>
        </div>
    </body>
</html>
        '''

    #basic print out function to send html to browser
    def print_out(self):
        return self._head + self._body + self._close

#content page is our dynmic html creation class that we populate with info from the data.py file which is sent via the main.py file
class ContentPage(Page):
    def __init__(self):
        #since this is a subclass, we have to declare the initializer for the super class it is inheriting from
        super(ContentPage, self).__init__()
        #for everything below: we create appropriate attributes to set/contain html and data object info and add setters/getters for each so that they can be accessed and changed
        self._div_start = '<div id="info">'

        @property
        def div_start(self):
            pass

        self._div_close = '</div>'

        @property
        def div_close(self):
            pass

        self._title = ''

        @property
        def title(self):
            pass

        @title.setter
        def title(self, new_title):
            self._title = new_title

        self._image = ''

        @property
        def image(self):
            pass

        @image.setter
        def image(self, new_image):
            self._image = new_image

        self._time = 0

        @property
        def time(self):
            pass

        @time.setter
        def time(self, new_time):
            self._time = new_time

        self._genre = ''

        @property
        def genre(self):
            pass

        @genre.setter
        def genre(self, new_genre):
            self._genre = new_genre

        self._director = ''

        @property
        def director(self):
            pass

        @director.setter
        def director(self, new_director):
            self._director = new_director

        self._year  = 0

        @property
        def year(self):
            pass

        @year.setter
        def year(self, new_year):
            self._year = new_year

        self._studio = ''

        @property
        def studio(self):
            pass

        @studio.setter
        def studio(self, new_studio):
            self._studio = new_studio

    #we create a new print out function containing the additional attributes we create in the contentpage subclass - this will overwrite the print out we created in the page class
    def print_out(self):
        return self._head + self._body + self._div_start + '<h1>' + self._title + '</h1>' + '<h2>' + 'Directed by ' + self._director + '</h2>' +  '<img src="' + self._image + '" />' + '<p>Released in: ' + str(self._year) + ' | ' + 'Running time: ' + str(self._time) + ' | ' + 'Studio: ' + self._studio + ' | ' + 'Genre: ' + self._genre +  self._div_close + self._close