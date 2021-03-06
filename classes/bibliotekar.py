from classes.korisnik import Korisnik


class Bibliotekar(Korisnik):
    def __init__(self, id, username, fname, lname, password, cardNumber, accType=1,deleted=False):
        self.id = id
        super().__init__(username, fname, lname, password, cardNumber,accType,deleted)
        # Korisnik.__init__(self,id,username,fname,lname,password)
        self.SetAccessLevel(accType)

    def getID(self):
        return self.id

    def ToJSON(self):
        return self.__dict__
