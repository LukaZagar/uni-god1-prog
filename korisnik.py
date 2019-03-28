import ui

class Korisnik:
    #Access levels
    #1.Bibliotekar
    # NILL .Korisnik

    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password
        self.accessLevel = 0
    
    def SetAccessLevel(self,level):
        self.accessLevel = level

    def GetAccessLevel(self):
        return self.accessLevel

    def AccessLevelToString(self):
        _tostringText = "No Data!"
        
        if self.accessLevel == 1:
            _tostringText = "Bibliotekar"
        else:
            _tostringText = "Korisnik"
        
        return _tostringText
    
    def Delete(self,izbrisi):
        self.deleted = izbrisi

    def SetPassword(self,pwd):
        self.password = pwd

