from classes.korisnik import Korisnik

class Bibliotekar(Korisnik):
    def __init__(self,id,username,fname,lname,password,cardNumber,accType=1):
        super().__init__(username,fname,lname,password,cardNumber)
        #Korisnik.__init__(self,id,username,fname,lname,password)
        self.SetAccessLevel(accType)