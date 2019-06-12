from classes.korisnik import Korisnik
from classes.bibliotekar import Bibliotekar
from classes.knjiga import Knjiga
import libs.db as db

def showLogin():
    print("\n\nUlogovanje u sistem...")
    print('\n\nNapomena: Unesite "Q" ili "q" da odustanete od prijave')
    username = input("Unesite korisnicko ime: ")
    if username == "Q" or username == "q" : return # ako zeli da izadje neidi dalje
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

def createNewUser():
    accType = input("Unesite numerican modifikator pristupa naloga (1= Korisnik 2=Bibliotekar):: ")
    accUname = input("Unesite korisnicko ime novog naloga:: ")
    if db.userExists(accUname):
        print("KORISNIK SA IMENOM"+str(accUname)+" VEC POSTOJI, PROBAJTE OPET")
        createNewUser()
        return 
    accFName = input("Unesite ime novog korisnickog naloga:: ")
    accLName = input("Unesite prezime novog korisnickog naloga:: ")
    accPwd = input("Unesite lozinku novog korisnickog naloga:: ")
    accCardNum = input("Unesite jedisntveni broj clanske karte korisnika:: ")
    korisnik = Korisnik(
        username = accUname,
        fname = accFName,
        lname = accLName,
        password = accPwd,
        cardNumber = accCardNum,
        accType=accType
        )
    
    addUserRes,errorMsg = db.addUser(korisnik)

    if addUserRes:
        print("Uspesno uneti novi korisnik!")
        db.saveUsers()
        return korisnik
    else:
        print(f"Greska prilikom dodavanja korisnika, {errorMsg}")
        return False  

def createNewBook(bookID=False):
    bookID = input("Unesite ID knjige:: ") if not bookID else bookID #Ukoliko smo vec prosledili ID parametar, nemoj pitati za input
    bookAuthor = input("Unesite autora knjige:: ")
    bookReleaseDate = input("Unesite datum izdanja knjige:: ")
    bookCount = input("Unesite ukupan broj knjiga:: ")
    bookCountAvailable = input("Unesite broj slobodnih knjiga:: ")
    
    book = Knjiga(
        id=bookID,
        autor=bookAuthor,
        godIzdavanja=bookReleaseDate,
        brojPrimeraka=bookCount,
        brojSlobodnihPrimeraka=bookCountAvailable
    )

    #db._books[bookID] = None # ukoliko menjamo vec postojecu knjigu, moramo izbrisati vec postojecu vrednost inace ce vratiti gresku ne jedistvenosti ID parametra
    db._books.pop(bookID,None)

    addBookRes,errorMsg = db.addBook(book)
    if addBookRes:
        print("Uspesno dodata knjiga!")
        db.saveBooks()
        return book
    else:
        print(f"Greska prilikom dodavanja knjige, {errorMsg}")
        return False


def editBook():
    
    print("U bazi su trenutno sledece knjige: ")
    for k,v in db._books.items():
        jsonData = v.toJSON()
        print(f"\t[{k}]:\n\t\t {jsonData}")
    change = input("Izaberite redni broj knjige koje podatke zelite da izmenite:: ")
    createNewBook(change) 

_uiMenus = {
    1 : { #bibliotekar
        "mainMenu": {
            1: {
                "text":"Unos i izmena podataka o Knjigama",
                "onSelect": "modifyBook"
            },
            2:{
                "text":"Unos podataka za Bibliotekara i Korisnika",
                "onSelect": "modifyUser"
            },
            3:{
                "text":"Izmena podataka trenutno prijavljenog Bibliotekara",
                "onSelect": "modifyUser"
            },
            4:{
                "text":"Zaduživanje i razduživanje Korisnika",
                "onSelect": "modifyUser"
            }, 
            5:{
                "text":"Rashodovanje knjiga",
                "onSelect": "modifyUser"
            }, 
            6:{
                "text":"Brisanje Korisnika",
                "onSelect": "modifyUser"
            }
        },
        "modifyBook":{
            1:{
                "text":"Unos nove knjige",
                "function":createNewBook
            },
            2:{
                "text":"Izmena podataka vec unete knjige",
                "function":editBook
            }
        },
        "modifyUser":{
            1:{
                "text":"Unesi novog korisnika",
                "onSelect": "modifyUser_CreateNew"
            },
            2:{
                "text":"Modifikuj vec postojeceg korisnika",
                "onSelect": "modifyUser_ModifyExisting"
            },
        },
        "modifyUser_CreateNew":{
            "function": createNewUser
        }
    },
    2 : { #Korisnik
        "mainMenu": {
            1:{
                "text":"Pregled zaduzenih knjiga.",
                "onSelect":"",
            },
            2:{
                "text": "Pretrazivanje knjiga.",
                "onSelect":"",
            },
            3:{
                "text": "Izmena podataka korisnickog naloga.",
                "onSelect":"",
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
        

    for k,v in _uiMenus[acclvl][id].items():
        print("["+str(k)+"] "+v["text"])

    result = input("Unesite broj zeljene akcije:: ")

    try: #
        _menu = _uiMenus[acclvl][id][int(result)]
        _onSelect = _menu["onSelect"] if "onSelect" in _menu else None #modifyBook
        _function = _menu["function"] if "function" in _menu else None

        onSelectPrint = _onSelect != None and _onSelect != ""
        onSelectFunc = _function != None and _function != ""

        if onSelectPrint: printModularMenu(_onSelect) # prikazi sledeci meni ukoliko ima onSelect polje
        if onSelectFunc: _menu["function"]() # ako dodjemo do ovde, znaci da nema onselect vec ima samo funkcija

        
        printModularMenu("mainMenu") #gotovi sa funkcijom, to je jedini nacin da cemo doci do ove linije, znaci vrati na pocetni meni
    except KeyError: # uneta pogresna ili nepostojeca vrednost
        print("Ne postoji opcija "+str(result)+" u meniju "+str(k))
        printModularMenu(id) # prikazi mu isti meni opet

    return result





