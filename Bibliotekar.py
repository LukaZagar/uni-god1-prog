from korisnik import Korisnik

class Bibliotekar(Korisnik):
    def __init__(self,id,username,password):
        Korisnik.__init__(self,id,username,password)