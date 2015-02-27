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
        <ul id="menu">
            <li><a href="?genre=fantasy">The Cat Returns</a></li>
            <li><a href="?genre=sci-fi">The Girl Who Leapt Through Time</a></li>
            <li><a href="?genre=historical">Sword of the Stranger</a></li>
            <li><a href="?genre=romance">5 Centimeters Per Second</a></li>
            <li><a href="?genre=environmental">Origin: Spirits of the Past</a></li>
        </ul>
        '''

        self._close = '''
    </body>
</html>
        '''

    def print_out(self):
        return self._head + self._body + self._close

class ContentPage(Page):
    def __init__(self):
        super(ContentPage, self).__init__()
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

    def print_out(self):
        return self._head + self._body + self._div_start + '<h1>' + self._title + '</h1>' + '<h2>' + 'Directed by ' + self._director + '</h2>' +  '<img src="' + self._image + '" />' + '<p>Released in: ' + str(self._year) + ' | ' + 'Running time: ' + str(self._time) + ' | ' + 'Studio: ' + self._studio + ' | ' + 'Genre: ' + self._genre +  self._div_close