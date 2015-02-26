"""
James Stanbridge
26 Feb 2014
Dynamic Site
"""

class Page(object):
    def __init__(self):
        self._head = '''

        '''

        self._body = '''
        <a href="1">1</a>
        <a href="2">2</a>
        <a href="3">3</a>
        <a href="4">4</a>
        <a href="5">5</a>
        '''

        self._close = '''
        '''

    def print_out(self):
        return self._head + self._body + self._close
