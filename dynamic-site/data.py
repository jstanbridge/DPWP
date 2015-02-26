"""
James Stanbridge
26 Feb 2014
Dynamic Site
"""

class Data(self):
    def __init__(self):

        cat = Movie()
        cat.title = 'The Cat Returns'
        cat.time = 95
        cat.studio = 'Studio Ghibli'
        cat.year = 2002
        cat.genre = 'Fantasy'
        cat.director = 'Hiroyuki Morita'

        time = Movie()
        time.title = 'The Girl Who Leapt Through Time'
        time.time = 98
        time.studio = 'Studio Ghibli'
        time.year = 2006
        time.genre = 'Fantasy'
        time.director = 'Hiroyuki Morita'

        sword = Movie()
        sword.title = 'Sword of the Stranger'
        sword.time = 98
        sword.studio = 'Studio Ghibli'
        sword.year = 2007
        sword.genre = 'Fantasy'
        sword.director = 'Hiroyuki Morita'

        cent = Movie()
        cent.title = '5 Centimeters Per Second'
        cent.time = 62
        cent.studio = 'Studio Ghibli'
        cent.year = 2007
        cent.genre = 'Fantasy'
        cent.director = 'Hiroyuki Morita'

        spirit = Movie()
        spirit.title = 'Origin: Spirits of the Past'
        spirit.time = 95
        spirit.studio = 'Studio Ghibli'
        spirit.year = 2006
        spirit.genre = 'Fantasy'
        spirit.director = 'Hiroyuki Morita'

        self.list = [cat, time, sword, cent, spirit]
