import json


class Korisnik:
    #Access levels
    #1.Bibliotekar
    # NILL .Korisnik

    def __init__(self,accType,username,fname,lname,password):
        self.accessLevel = accType
        self.username = username
        self.fname = fname
        self.lname = lname
        self.password = password
    
    def GetUserName(self):
        return self.username
    

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

    def ToJSON(self):# Vratiti json.dumps verziju sa time sto specifiramo parametar "default" i govorimo mu da koristi ugradjenu funkciju klase "__dict__"
        return self.__dict__
