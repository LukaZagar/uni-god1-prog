class Zaduzenje():
    def __init__(self, bookID, dateIssued, dateReturned, cardNumber):
        self.bookID = bookID
        self.dateIssued = dateIssued
        self.dateReturned = dateReturned
        self.cardNumber = cardNumber

    def getCardNumber(self):
        return self.cardNumber

    def ToJSON(self):
        return self.__dict__
