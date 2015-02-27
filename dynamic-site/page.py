"""
James Stanbridge
26 Feb 2014
Dynamic Site
"""

class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
          <title>Dynamic Site</title>
    </head>

    <body>
        '''

        self._body = '''
        <a href="?genre=fantasy">1</a>
        <a href="?genre=sci-fi">2</a>
        <a href="?genre=historical">3</a>
        <a href="?genre=romance">4</a>
        <a href="?genre=environmental">5</a>
        '''

        self.item ='''
        '''

        self._close = '''
    </body>
</html>
        '''

    def print_out(self):
        return self._head + self._body + self.item + self._close

class ContentPage(Page):
    def __init__(self):
        super(ContentPage, self).__init__()
        self._div_start = '<div id="info">'
        self._div_close = '</div>'

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

