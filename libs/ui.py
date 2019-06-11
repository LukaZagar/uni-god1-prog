from classes.korisnik import Korisnik
from classes.bibliotekar import Bibliotekar
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
    db.addUser(korisnik)
    print("Uspesno uneti novi korisnik!")
    db.saveUsers()
    return korisnik


_uiMenus = {
    1 : { #bibliotekar
        "mainMenu": {
            1: {
                "text":"Unos i izmena podataka o Knjigama",
                "onSelect": "modifyUser"
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
    
    try: # da li ima funkcija u ovom pod meniju koju treba da odma pozovemo / Korisnik izabrao operaciju u jednom od podmenija
        _uiMenus[acclvl][id]["function"]()
        printModularMenu("mainMenu")# zavrsili smo sa funkcijom, povratak na glavni meni
    except (KeyError,TypeError) as err:
        print(str(err))
        

    for k,v in _uiMenus[acclvl][id].items():
        print("["+str(k)+"] "+v["text"])

    result = input("Unesite broj zeljene akcije:: ")

    try: #
        printModularMenu(_uiMenus[acclvl][id][int(result)]["onSelect"]) # prikazi sledeci meni
    except KeyError: # uneta pogresna ili nepostojeca vrednost
        print("Ne postoji opcija "+str(result)+" u meniju "+str(k))
        printModularMenu(id) # prikazi mu isti meni opet

    return result





