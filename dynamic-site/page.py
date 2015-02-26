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
        '''

        self._close = '''
        '''

    def print_out(self):
        return self._head + self._body + self._close
