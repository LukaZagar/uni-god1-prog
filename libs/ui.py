from classes.korisnik import Korisnik
from classes.bibliotekar import Bibliotekar
from classes.knjiga import Knjiga
from classes.zaduzenje import Zaduzenje
import libs.db as db

import datetime

def showLogin():
    print("\n\nUlogovanje u sistem...")
    print('\n\nNapomena: Unesite "Q" ili "q" da odustanete od prijave')
    username = input("Unesite korisnicko ime: ")
    if username == "Q" or username == "q":
        return  # ako zeli da izadje neidi dalje
    pwd = input("Unesite password: ")

    return {
        "Username": str(username),
        "Password": str(pwd)
    }


def successfullLogin(userClass):
    print("\n=================================")
    print("====== USPESNO ULOGOVANI ========")
    print("=================================")
    print("ID:           "+str(userClass.accessLevel))
    print("Nalog:        "+str(userClass.username))
    print("Ime:          "+str(userClass.fname))
    print("Prezime:      "+str(userClass.lname))
    print("Vrsta naloga: "+str(userClass.AccessLevelToString()))
    print("=================================\n")


def showUserMenu(user):
    global activeUser
    activeUser = user
    # userLevel = userLevel or 0

    print("Selektujte opciju:")
    result = printModularMenu("mainMenu")

    print('Q.Izlaz iz sistema')
    return result


def createNewUser(providedUser=False):
    accID = None
    accType = input(
        "Unesite numerican modifikator pristupa naloga (2= Korisnik 1=Bibliotekar):: ") if not providedUser else providedUser.GetAccessLevel()

    if int(accType) == 1:  # ukoliko je bibliotekar, trazi id
        accID = int(input("Unesite ID za bibliotekara:: "))
        if db.librarianIDExists(accID):
            print("Bibliotekar sa datim ID-jem vec postoji!\n")
            createNewUser(providedUser=providedUser)
    accUname = input("Unesite korisnicko ime novog naloga:: ")
    if db.userExists(accUname):
        print("KORISNIK SA IMENOM"+str(accUname)+" VEC POSTOJI, PROBAJTE OPET")
        createNewUser(providedUser=providedUser)
        return
    accFName = input("Unesite ime novog korisnickog naloga:: ")
    accLName = input("Unesite prezime novog korisnickog naloga:: ")
    accPwd = input("Unesite lozinku novog korisnickog naloga:: ")
    accCardNum = input("Unesite jedisntveni broj clanske karte korisnika:: ")

    nalog = None
    if int(accType) == 1:
        nalog = Bibliotekar(
            id=int(accID),
            username=accUname,
            fname=accFName,
            lname=accLName,
            password=accPwd,
            cardNumber=int(accCardNum),
            accType=int(accType)
        )
    elif int(accType) == 2:
        nalog = Korisnik(
            username=accUname,
            fname=accFName,
            lname=accLName,
            password=accPwd,
            cardNumber=int(accCardNum),
            accType=int(accType)
        )

    if not db.isUserCardNumberUnique(nalog):
        print("Morate uneti jednistveni broj clanske karte!")
        createNewUser(providedUser=providedUser)

    if providedUser != False:
        db._users.pop(providedUser.GetUserName(), None)

    addUserRes, errorMsg = db.addUser(nalog)

    if addUserRes:
        print("Uspesno uneti novi nalog!")
        db.saveUsers()
        return nalog
    else:
        print(f"Greska prilikom dodavanja naloga, {errorMsg}")
        return False


def createNewBook(bookID=False):
    # Ukoliko smo vec prosledili ID parametar, nemoj pitati za input
    bookID = input("Unesite ID knjige:: ") if not bookID else bookID
    bookAuthor = input("Unesite autora knjige:: ")
    bookReleaseDate = input("Unesite datum izdanja knjige:: ")
    bookCount = input("Unesite ukupan broj knjiga:: ")
    bookCountAvailable = input("Unesite broj slobodnih knjiga:: ")

    book = Knjiga(
        id=int(bookID),
        autor=bookAuthor,
        godIzdavanja=bookReleaseDate,
        brojPrimeraka=int(bookCount),
        brojSlobodnihPrimeraka=int(bookCountAvailable)
    )

    # db._books[bookID] = None # ukoliko menjamo vec postojecu knjigu, moramo izbrisati vec postojecu vrednost inace ce vratiti gresku ne jedistvenosti ID parametra
    db._books.pop(int(bookID), None)

    addBookRes, errorMsg = db.addBook(book)
    if addBookRes:
        print("Uspesno dodata knjiga!")
        db.saveBooks()
        return book
    else:
        print(f"Greska prilikom dodavanja knjige, {errorMsg}")
        return False


def editBook():
    print("U bazi su trenutno sledece knjige: ")
    for k, v in db._books.items():
        jsonData = v.toJSON()
        print(f"\t[{k}]:\n\t\t {jsonData}")
    change = input("Izaberite redni broj knjige koje podatke zelite da izmenite:: ")
    createNewBook(change)


def modifyLibrarian():
    _newUser = createNewUser(db.getActiveUser())
    return _newUser


def searchUsers(searchType):
    results = []
    counter = 0
    if searchType == "cardNum":
        cardToSearch = int(
            input("Unesite broj karte koji zelite da pretrazite:: "))
        for _, v in db.getUsers().items():
            if v.GetCardNumber() == cardToSearch:
                results.insert(counter, v)
                counter += 1
    if searchType == "userName":
        unameToSearch = input("Unesite ime korisnickog naloga za pretragu:: ")
        for _, v in db.getUsers().items():
            if unameToSearch in v.GetFirstName():
                results.insert(counter, v)
                counter += 1
    if searchType == "lastName":
        lnameToSearch = input(
            "Unesite prezime korisnickog naloga za pretragu:: ")
        for _, v in db.getUsers().items():
            if lnameToSearch in v.GetLastName():
                results.insert(counter, v)
                counter += 1
    return results


def searchBooks(searchType):
    results = [] #id, autor,god izdanja
    counter = 0
    if searchType == "id":
        searchFor = int(input("Unesite ID knjige:: "))
        for k, v in db._books.items():
            if v.getID() == searchFor:
                results.insert(counter, v)
                counter += 1
    if searchType == "author":
        searchFor = input("Unesite Autora knjige:: ")
        for k, v in db._books.items():
            if v.getAuthor() == searchFor:
                results.insert(counter, v)
                counter += 1
    if searchType == "releaseDate":
        searchFor = input("Unesite datum izdanja knjige:: ")
        for k, v in db._books.items():
            if str(v.getReleaseDate()) in searchFor:
                results.insert(counter, v)
                counter += 1

    return results

def zaduzi(userClass,bookClass):
    zad = Zaduzenje(
        bookID = bookClass.getID(),
        dateIssued = str(datetime.datetime.now()),
        dateReturned = "N/A",
        cardNumber = userClass.GetCardNumber()
    )
    db.addZaduzenje(zad)
    db.saveRentedBooks()
    db.loadRentedBooks()


def razduzi(userClass,zadClass):
    db.removeZaduzenje(zadClass)
    
    db.saveBooks()
    db.saveRentedBooks()
    
    db.loadRentedBooks()
    db.loadBooks()

def handleUsersSearch(res):
    print("Rezultat pretrage korisnika:")
    for pos in range(len(res)):
        _currUser = res[pos]
        print(f"\t\t[{pos}]: {_currUser.ToJSON()}")
    selectedUser = input("Izaberite korisnika kojeg zelite da zaduzite/razduzite:: ")
    _user = res[int(selectedUser)]

    _due = db.getUserZaduzenja(_user)
    print("Trenutna zaduzenja korisnika: \n")
    for pos in range(len(_due)):
        zad = _due[pos]
        print(f"\t\t [{pos}] {zad.ToJSON()}\n")

    whatToDo = int(input("Zelite da\n\t[1]Zaduzite\n\t[2]Razduzite\nIzaberite opciju:: "))
    if whatToDo == 1: #Zaduzivanje
        searchMethod = input("Da li zelite da pretrazite putem:\n\t[1].ID Knjige\n\t[2].Autorom Knjige\n\t[3].Godinom Izdanja knjige\nIzaberite opciju::")
        bookRes = None
        if searchMethod == "1":
            bookRes = searchBooks("id")
        elif searchMethod == "2":
            bookRes = searchBooks("author")
        else:
            bookRes = searchBooks("releaseDate")

        print("Rezultat pretrage je:")
        for count in range(len(bookRes)):
            _currLoopBook = bookRes[count]
            print(f"\t\t[{count}] {_currLoopBook.toJSON()}")
        try:
            zaduziKnjiguNum = int(input("Unesite redni broj knjige koji zelite da zaduzite korisnika:: "))
            zaduzi(_user,bookRes[zaduziKnjiguNum])
        except IndexError:
            input(f"Ne postoji opcija {searchMethod} !")
            handleUsersSearch(res=res)
    else: #Razduzivanje 
        _razduziInput = int(input("Unesite redni broj zaduzenja koji zelite da razduzite korisnika:: "))
        razduzi(_user,_due[_razduziInput])

def destroyBook():
    print("U bazi su trenutno sledece knjige: ")
    for k,v in db._books.items():
        print(f"\t\t[{k}] {v.toJSON()}")
    _kill = int(input("Unesite redni broj knjige koji zelite da uklonite:: "))
    _ammt = int(input("Koliko primeraka da se ukloni?::"))
    db._books[_kill].removeBaseStock(_ammt)
    db.saveBooks()
    db.loadBooks()

def deleteUser():
    #counter = 0
    _tempList = []
    for _,user in db.getUsers().items(): #username je kljuc
        if not user.isDeleted():
            #print(f"[{counter}] {user.ToJSON()}")
            _tempList.append(user)
            #counter += 1

    for pos in range(len(_tempList)):
        _currUser = _tempList[pos]
        print(f"[{pos}] {_currUser.ToJSON()}")

    _order66 = int(input("Izaberite korisnika kojeg zelite da izbrisete:: "))
    _tempList[_order66].Delete(True)
    
    db.saveUsers()
    db.loadUsers()

_uiMenus = {
    1: {  # bibliotekar
        "mainMenu": {
            1: {
                "text": "Unos i izmena podataka o Knjigama",
                "onSelect": "modifyBook"
            },
            2: {
                "text": "Unos podataka za Bibliotekara i Korisnika",
                "onSelect": "modifyUser"
            },
            3: {
                "text": "Izmena podataka trenutno prijavljenog Bibliotekara",
                "onSelect": "modifyUser"
            },
            4: {
                "text": "Zaduživanje i razduživanje Korisnika",
                "onSelect": "searchUserMethod"
            },
            5: {
                "text": "Rashodovanje knjiga",
                "function": destroyBook
            },
            6: {
                "text": "Brisanje Korisnika",
                "function": deleteUser
            }
        },
        "searchUserMethod": {
            1: {
                "text": "Pretraga putem broja clanske karte",
                # from functools import partial ali mrsko mi se sa time petljati
                "function": lambda: handleUsersSearch(searchUsers("cardNum"))
            },
            2: {
                "text": "Pretraga putem imena",
                "function": lambda: handleUsersSearch(searchUsers("userName"))
            },
            3: {
                "text": "Pretraga putem prezimena",
                "function": lambda: handleUsersSearch(searchUsers("lastName"))
            },
        },
        "modifyBook": {
            1: {
                "text": "Unos nove knjige",
                "function": createNewBook
            },
            2: {
                "text": "Izmena podataka vec unete knjige",
                "function": editBook
            }
        },
        "modifyUser": {
            1: {
                "text": "Unesi novog korisnika",
                "function": createNewUser
            },
            2: {
                "text": "Modifikuj trenutno prijavnjenog Bibliotekara",
                "function": modifyLibrarian
            },
        }

    },
    2: {  # Korisnik
        "mainMenu": {
            1: {
                "text": "Pregled zaduzenih knjiga.",
                "onSelect": "",
            },
            2: {
                "text": "Pretrazivanje knjiga.",
                "onSelect": "",
            },
            3: {
                "text": "Izmena podataka korisnickog naloga.",
                "onSelect": "",
            },
        },
    },
}


def printModularMenu(id):
    result = False
    acclvl = activeUser.GetAccessLevel()

    # try: # da li ima funkcija u ovom pod meniju koju treba da odma pozovemo / Korisnik izabrao operaciju u jednom od podmenija
    #     _uiMenus[acclvl][id]["function"]()
    #     printModularMenu("mainMenu")# zavrsili smo sa funkcijom, povratak na glavni meni
    # except (KeyError,TypeError) as err:
    #     print(str(err))

    for k, v in _uiMenus[acclvl][id].items():
        if k == "function":
            _uiMenus[acclvl][id]["function"]()
        if "text" in v:
            print("["+str(k)+"] "+v["text"])

    result = input("Unesite broj zeljene akcije:: ")

    if str.lower(result) == "q":
        return

    try:
        _menu = _uiMenus[acclvl][id][int(result)]
        # modifyBook
        _onSelect = _menu["onSelect"] if "onSelect" in _menu else None
        _function = _menu["function"] if "function" in _menu else None

        onSelectPrint = _onSelect != None and _onSelect != ""
        onSelectFunc = _function != None and _function != ""

        if onSelectPrint:
            # prikazi sledeci meni ukoliko ima onSelect polje
            printModularMenu(_onSelect)
        if onSelectFunc:
            # ako dodjemo do ovde, znaci da nema onselect vec ima samo funkcija
            _menu["function"]()

        # gotovi sa funkcijom, to je jedini nacin da cemo doci do ove linije, znaci vrati na pocetni meni
        printModularMenu("mainMenu")
    except KeyError:  # uneta pogresna ili nepostojeca vrednost
        print("Ne postoji opcija "+str(result)+" u meniju "+str(k))
        printModularMenu(id)  # prikazi mu isti meni opet

    return result
