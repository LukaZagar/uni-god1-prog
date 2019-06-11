import json
from classes.korisnik import Korisnik
from classes.bibliotekar import Bibliotekar

import sys
import os

_users = {}

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
    return (
        isUserUsernameUnique(userArg) and isUserCardNumberUnique(userArg)
        )

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

# korisnik1 = Korisnik(1,"LukaZ","Luka","Zagar","123")
# bibliotekar1 = Bibliotekar(2,"Petar66","Petar","Petric","321")


# addUser(korisnik1)
# addUser(bibliotekar1)

# saveUsers()


# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)