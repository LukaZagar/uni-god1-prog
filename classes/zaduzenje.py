
import datetime

class Zaduzenje():
    def __init__(self, bookID, dateIssued, dateReturned, cardNumber):
        self.bookID = bookID
        self.dateIssued = dateIssued
        self.dateReturned = dateReturned
        self.cardNumber = cardNumber


    def getBookID(self):
        return self.bookID


    def setReturned(self):
        self.dateReturned = str(datetime.datetime.now())


    def getCardNumber(self):
        """
            Vraca broj karte korisnika
        """
        return self.cardNumber


    def ToJSON(self):
        return self.__dict__
