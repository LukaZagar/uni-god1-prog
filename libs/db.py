import json
from classes.korisnik import Korisnik
from classes.bibliotekar import Bibliotekar
from classes.knjiga import Knjiga

import sys
import os

_users = {}
_books = {}

fileDir = os.path.dirname(os.path.abspath(__file__))
_dataDir = fileDir[:-5]+"/data/" # odstrani /libs sa kraja

def getUsers():
    return _users

def saveUsers(defaultSave=False):
    """
        Sacuva korisnike u JSON formatu u /data direktorijum\n
        Parametri:\n
        <bool> defaultSave - Sacuvaj default korisnike ( ovo je samo u slucaju greske sa ucitanim podatcima )
    """
    usersDir = _dataDir+"users.json"
   
    print(f"Cuvanje korisnika u direktorijum {usersDir}")

    if defaultSave:
        korisnik1 = Korisnik(
            username="LukaZ",
            fname="Luka",
            lname="Zagar",
            password="123",
            cardNumber=0
            )
        bibliotekar1 = Bibliotekar(
            id=2,
            username="Petar66",
            fname="Petar",
            lname="Petric",
            password="321",
            cardNumber=1
            )

        addUser(korisnik1)
        addUser(bibliotekar1)

    _saveDict = {}
    for _,_user in _users.items():
        _saveDict[_user.GetUserName()] = _user.ToJSON()    # kljuc je bio pod '' navodnicima, a json to nepodrzava

    #try:
    with open(usersDir, 'w') as outfile:
        jsonFormat = json.dumps(_saveDict,sort_keys=True,indent=4)
        outfile.write(jsonFormat)
        print("Uspesno sacuvani podatci korisnika!")
        #json.dump(,outfile)
    # except:
    #     print("\n[GRESKA] Greska prilikom cuvanja podataka, podatci NISU SACUVANI, Poruka: ")
    # finally:
    #     print("\nGotovo cuvanje korisnika")


def loadUsers():
    """
        Ucitaj korisnike iz users.json, izbacuje gresku ukoliko nije u mogucnosti da ucita, ukoliko fajl nepostoji , kreira default fajl.
    """

    usersDir = _dataDir+"users.json"
    if os.path.isfile(usersDir) and os.stat(usersDir).st_size != 0: # da li postoji fajl i da nije prazan
        try:
            print("Fajl sa korisnicima postoji, ucitavanje...")
            jsonFile = open(usersDir)
            jsonStr = jsonFile.read()
            jsonData = json.loads(jsonStr)
            global _users

            for k,v in jsonData.items():
                korisnik = Korisnik(
                    username = v["username"],
                    fname = v["fname"],
                    lname = v["lname"],
                    password = v["password"],
                    cardNumber = v["cardNumber"],
                    accType=v["accessLevel"]
                    )
                _users[k] = korisnik
        except:
            print("\n[GRESKA] Greska prilikom ucitavanja podataka")
        finally:
            print("Gotovo ucitavanje korisnika!") 
    else:
        print("Fajl sa korisnicima ne postoji ili ima gesku, cuvanje default korisnika...")
        saveUsers(defaultSave=True)
        loadUsers()

def userExists(uname):
    return uname in _users

def isUserUsernameUnique(userClass):
    return not userExists(userClass.username)

def isUserCardNumberUnique(userClass):
    cardToCheck = userClass.GetCardNumber()
    for _,v in _users.items():
        if cardToCheck == v.GetCardNumber():
            return False

    #return True

def isUserDataUnique(userArg):
    return (isUserUsernameUnique(userArg) and isUserCardNumberUnique(userArg))

def addUser(user):
    username = user.GetUserName()
    if isUserDataUnique(user):
        _users[username] = user
        return True
    else:
        return False,"Korisnik sa tim korisnickim imenom/brojem clanske karte vec postoji!"
        
    # if not userExists(username):
    #     _users[username] = user
    #     saveUsers()

def isBookDataUnique(bookClass):
    return bookClass.getID() in _books

def addBook(bookClass):
    if not isBookDataUnique(bookClass):
        global _books
        _books[bookClass.getID()] = bookClass
        return True
    else:
        return False,"Knjiga sa ovim ID vec postoji!"

def saveBooks(defaultSave=False):
    bookDir = _dataDir+"books.json"
    if defaultSave:
        book1 = Knjiga(
            id=0,
            autor="Mike Litoris",
            godIzdavanja = "1/1/1970",
            brojPrimeraka = 23,
            brojSlobodnihPrimeraka = 12
        )
        addBook(book1)

    _saveDict = {}
    for _,_book in _books.items():
        _saveDict[_book.getID()] = _book.toJSON()    # kljuc je bio pod '' navodnicima, a json to nepodrzava

    with open(bookDir, 'w') as outfile:
        jsonFormat = json.dumps(_saveDict,sort_keys=True,indent=4)
        outfile.write(jsonFormat)
        print("Uspesno sacuvani podatci knjiga!")

def loadBooks():
    bookDir = _dataDir+"books.json"
    if os.path.isfile(bookDir) and os.stat(bookDir).st_size != 0: # da li postoji fajl i da nije prazan
        try:
            print("Fajl sa knjigama postoji, ucitavanje...")
            jsonFile = open(bookDir)
            jsonStr = jsonFile.read()
            jsonData = json.loads(jsonStr)
            global _users

            for k,v in jsonData.items():
                book = Knjiga(
                    id = v["id"],
                    autor = v["Autor"],
                    godIzdavanja = v["GodIzdanja"],
                    brojPrimeraka = v["BrojPrimeraka"],
                    brojSlobodnihPrimeraka = v["BrojSlobodnihPrimeraka"]
                    )
                _books[k] = book
        except:
            print("\n[GRESKA] Greska prilikom ucitavanja podataka")
        finally:
            print("Gotovo ucitavanje knjiga!")
            print(_books) 
    else:
        print("Fajl sa knjigama ne postoji ili ima gesku, cuvanje default knjiga...")
        saveBooks(defaultSave=True)
        loadBooks()


# korisnik1 = Korisnik(1,"LukaZ","Luka","Zagar","123")
# bibliotekar1 = Bibliotekar(2,"Petar66","Petar","Petric","321")


# addUser(korisnik1)
# addUser(bibliotekar1)

# saveUsers()


# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)