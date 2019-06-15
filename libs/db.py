import json
from classes.korisnik import Korisnik
from classes.bibliotekar import Bibliotekar
from classes.knjiga import Knjiga
from classes.zaduzenje import Zaduzenje

import sys
import os

_users = {}
_books = {}
_rented = {}

_currentUser = False

fileDir = os.path.dirname(os.path.abspath(__file__))
_dataDir = fileDir[:-5]+"/data/"  # odstrani /libs sa kraja


def getUsers():
    return _users


def getActiveUser():
    return _currentUser


def setActiveUser(user):
    global _currentUser
    _currentUser = user
    return _currentUser


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
            id=0,
            username="Petar66",
            fname="Petar",
            lname="Petric",
            password="321",
            cardNumber=1
        )

        addUser(korisnik1)
        addUser(bibliotekar1)

    _saveDict = {}
    for _, _user in _users.items():
        # kljuc je bio pod '' navodnicima, a json to nepodrzava
        _saveDict[_user.GetUserName()] = _user.ToJSON()

    # try:
    with open(usersDir, 'w') as outfile:
        jsonFormat = json.dumps(_saveDict, sort_keys=True, indent=4)
        outfile.write(jsonFormat)
        print("Uspesno sacuvani podatci korisnika!")
        # json.dump(,outfile)
    # except:
    #     print("\n[GRESKA] Greska prilikom cuvanja podataka, podatci NISU SACUVANI, Poruka: ")
    # finally:
    #     print("\nGotovo cuvanje korisnika")


def loadUsers():
    """
        Ucitaj korisnike iz users.json, izbacuje gresku ukoliko nije u mogucnosti da ucita, ukoliko fajl nepostoji , kreira default fajl.
    """

    usersDir = _dataDir+"users.json"
    # da li postoji fajl i da nije prazan
    if os.path.isfile(usersDir) and os.stat(usersDir).st_size != 0:
        try:
            print("Fajl sa korisnicima postoji, ucitavanje...")
            jsonFile = open(usersDir)
            jsonStr = jsonFile.read()
            jsonData = json.loads(jsonStr)
            global _users

            for k, v in jsonData.items():
                korisnik = None
                if v["accessLevel"] == 1:
                    korisnik = Bibliotekar(
                        id=v["id"],
                        username=v["username"],
                        fname=v["fname"],
                        lname=v["lname"],
                        password=v["password"],
                        cardNumber=v["cardNumber"],
                        accType=v["accessLevel"],
                        deleted=v["deleted"]
                    )
                else:
                    korisnik = Korisnik(
                        username=v["username"],
                        fname=v["fname"],
                        lname=v["lname"],
                        password=v["password"],
                        cardNumber=v["cardNumber"],
                        accType=v["accessLevel"],
                        deleted=v["deleted"]
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


def increaseBookStock(bookClass,ammount=1):
    bookClass.increaseStock(ammount)

def addZaduzenje(zadClass):
    zadCardNum = zadClass.getCardNumber()
    _rented[zadCardNum] = zadClass
    return True


def removeZaduzenje(zadClass):
    #zadCardNum = zadClass.getCardNumber()
    #_rented.pop(zadCardNum,None)
    zadClass.setReturned()
    _book = _books[zadClass.getBookID()]
    _book.increaseStock(1)
    return True


def saveRentedBooks(defaultSave=False):
    """
        Sacuva zaduzenja korisnika,u JSON fajlu kljuc liste je cardNumber korisnika
        defaultSave- sacuvaj test(default) vrednosti 
    """

    rentedDir = _dataDir+"rented.json"
    print(f"Cuvanje podataka o zaduzenjima u direktorijum {rentedDir}")

    if defaultSave:
        zad1 = Zaduzenje(
            bookID=0,
            dateIssued="1/1/1970",
            dateReturned="2/2/1970",
            cardNumber=1
        )
        zad2 = Zaduzenje(
            bookID=1,
            dateIssued="1/1/1970",
            dateReturned="2/2/1970",
            cardNumber=1
        )
        zad3 = Zaduzenje(
            bookID=2,
            dateIssued="1/1/1970",
            dateReturned="2/2/1970",
            cardNumber=2
        )
        addZaduzenje(zad1)
        addZaduzenje(zad2)
        addZaduzenje(zad3)

    _saveDict = {}
    for _, _zaduzenje in _rented.items():
        # kljuc je bio pod '' navodnicima, a json to nepodrzava
        _saveDict[_zaduzenje.getCardNumber()] = _zaduzenje.ToJSON()

    # try:
    with open(rentedDir, 'w') as outfile:
        jsonFormat = json.dumps(_saveDict, sort_keys=True, indent=4)
        outfile.write(jsonFormat)
        print("Uspesno sacuvani podatci zaduzenja!")


def loadRentedBooks():
    rentedDir = _dataDir+"rented.json"

    # da li postoji fajl i da nije prazan
    if os.path.isfile(rentedDir) and os.stat(rentedDir).st_size != 0:
        try:
            print("Fajl sa zaduzenjima postoji, ucitavanje...")
            jsonFile = open(rentedDir)
            jsonStr = jsonFile.read()
            jsonData = json.loads(jsonStr)
            global _users
            for _userCardNum, _rentedData in jsonData.items():
                zad = Zaduzenje(
                    bookID=_rentedData["bookID"],
                    dateIssued=_rentedData["dateIssued"],
                    dateReturned=_rentedData["dateReturned"],
                    cardNumber=int(_rentedData["cardNumber"])
                )
                addZaduzenje(zad)
        except:
            print("\n[GRESKA] Greska prilikom ucitavanja podataka")
        finally:
            print("Gotovo ucitavanje korisnika!")
    else:
        print("Fajl sa zaduzenjima prazan ili greska, cuvanje default vrednosti...")
        saveRentedBooks(defaultSave=True)
        loadRentedBooks()


def userExists(uname):
    return uname in _users


def isUserUsernameUnique(userClass):
    return not userExists(userClass.username)


def isUserCardNumberUnique(userClass):
    """
        Proverava da li je data user klasa ima jednistveni broj clanske karte\n
        exactNumber - Proveri tacno taj broj, znaci nismo prosledili klasu nego direktan broj
    """
    cardToCheck = userClass.GetCardNumber()
    for loopUname, loopUser in _users.items():
        _cardNum = loopUser.GetCardNumber()
        # pobrini se da ukoliko modifikujemo trenutnog bibliotekara, dozvoli da ima isti ID
        if ((cardToCheck == _cardNum) and not(userClass.GetUserName() == loopUname)):
            return False

    return True


def librarianIDExists(accID):
    for _, v in _users.items():
        loopAccLevel = v.GetAccessLevel()
        if loopAccLevel == 1 and v.getID() == accID:
            return True

    return False


def isUserDataUnique(userArg):
    return (isUserUsernameUnique(userArg) and isUserCardNumberUnique(userArg))


def addUser(user):
    username = user.GetUserName()
    if isUserDataUnique(user):
        _users[username] = user
        return True, "Uspesno dodati korisnik!"
    else:
        return False, "Korisnik sa tim korisnickim imenom/brojem clanske karte vec postoji!"

    # if not userExists(username):
    #     _users[username] = user
    #     saveUsers()


def getUserZaduzenja(userClass):
    _result = []
    for k,v in _rented.items():
        if int(k) == userClass.GetCardNumber():
            _result.append(v)
    return _result


def isBookDataUnique(bookClass):
    for k, _ in _books.items():
        if int(k) == bookClass.getID():
            return False

    return True
 

def addBook(bookClass):
    if isBookDataUnique(bookClass):
        global _books
        _books[bookClass.getID()] = bookClass
        return True, "Uspesno dodata knjiga!"
    else:
        return False, "Knjiga sa ovim ID vec postoji!"


def saveBooks(defaultSave=False):
    bookDir = _dataDir+"books.json"
    if defaultSave:
        book1 = Knjiga(
            id=0,
            autor="Mike Litoris",
            godIzdavanja="1/1/1970",
            brojPrimeraka=23,
            brojSlobodnihPrimeraka=12
        )
        addBook(book1)

    _saveDict = {}
    for _, _book in _books.items():
        # kljuc je bio pod '' navodnicima, a json to nepodrzava
        _saveDict[_book.getID()] = _book.toJSON()

    with open(bookDir, 'w') as outfile:
        jsonFormat = json.dumps(_saveDict, sort_keys=True, indent=4)
        outfile.write(jsonFormat)
        print("Uspesno sacuvani podatci knjiga!")


def loadBooks():
    bookDir = _dataDir+"books.json"
    # da li postoji fajl i da nije prazan
    if os.path.isfile(bookDir) and os.stat(bookDir).st_size != 0:
        try:
            print("Fajl sa knjigama postoji, ucitavanje...")
            jsonFile = open(bookDir)
            jsonStr = jsonFile.read()
            jsonData = json.loads(jsonStr)
            global _users

            for k, v in jsonData.items():
                book = Knjiga(
                    id=int(v["id"]),
                    autor=v["Autor"],
                    godIzdavanja=v["GodIzdanja"],
                    brojPrimeraka=int(v["BrojPrimeraka"]),
                    brojSlobodnihPrimeraka=int(v["BrojSlobodnihPrimeraka"])
                )
                _books[int(k)] = book
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
