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
