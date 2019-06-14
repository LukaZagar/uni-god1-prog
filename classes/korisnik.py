import json


class Korisnik:
    #Access levels
    #1.Bibliotekar
    # NILL .Korisnik

    def __init__(self,username,fname,lname,password,cardNumber,accType=2):
        self.username = username
        self.fname = fname
        self.lname = lname
        self.password = password
        self.cardNumber = cardNumber
        self.accessLevel = accType or 2
    
    def GetCardNumber(self):
        return self.cardNumber

    def GetUserName(self):
        return self.username
    
    def GetFirstName(self):
        return self.fname
    
    def GetLastName(self):
        return self.fname
    
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

    def ToJSON(self):
        return self.__dict__
