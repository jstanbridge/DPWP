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
        time.studio = 'MADHOUSE'
        time.year = 2006
        time.genre = 'Sci-Fi'
        time.director = 'Mamoru Hosoda'

        sword = Movie()
        sword.title = 'Sword of the Stranger'
        sword.time = 98
        sword.studio = 'Bones'
        sword.year = 2007
        sword.genre = 'Historical'
        sword.director = 'Masahiro Ando'

        cent = Movie()
        cent.title = '5 Centimeters Per Second'
        cent.time = 62
        cent.studio = 'CoMix Wave Inc.'
        cent.year = 2007
        cent.genre = 'Romance'
        cent.director = 'Makoto Shinkai'

        spirit = Movie()
        spirit.title = 'Origin: Spirits of the Past'
        spirit.time = 95
        spirit.studio = 'GONZO'
        spirit.year = 2006
        spirit.genre = 'Environmental'
        spirit.director = 'Keiichi Sugiyama'

        self.list = [cat, time, sword, cent, spirit]
