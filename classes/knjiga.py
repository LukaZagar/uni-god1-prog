
class Knjiga:
    def __init__(self, id, autor, godIzdavanja, brojPrimeraka, brojSlobodnihPrimeraka):
        self.id = id
        self.Autor = autor
        self.GodIzdanja = godIzdavanja
        self.BrojPrimeraka = brojPrimeraka
        self.BrojSlobodnihPrimeraka = brojSlobodnihPrimeraka

    def removeBaseStock(self,ammt=1):
        self.BrojPrimeraka = int(self.BrojPrimeraka) - ammt

    def increaseStock(self,ammt=1):
        self.BrojSlobodnihPrimeraka = int(self.BrojSlobodnihPrimeraka) + ammt

    def getReleaseDate(self):
        return self.GodIzdanja

    def getAuthor(self):
        return self.Autor

    def getID(self):
        return self.id

    def toJSON(self):
        return self.__dict__
