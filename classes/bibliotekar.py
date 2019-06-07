from classes.korisnik import Korisnik

class Bibliotekar(Korisnik):
    def __init__(self,id,username,fname,lname,password):
        Korisnik.__init__(self,id,username,fname,lname,password)
        self.SetAccessLevel(1)