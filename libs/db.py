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
    usersDir = _dataDir+"users.json"
   
    print(f"Cuvanje korisnika u direktorijum {usersDir}")

    if defaultSave:
        korisnik1 = Korisnik(1,"LukaZ","Luka","Zagar","123")
        bibliotekar1 = Bibliotekar(2,"Petar66","Petar","Petric","321")

        addUser(korisnik1)
        addUser(bibliotekar1)

    _saveDict = {}
    for _,_user in _users.items():
        _saveDict[_user.GetUserName()] = _user.ToJSON()    # kljuc je bio pod '' navodnicima, a json to nepodrzava

    #try:
    with open(usersDir, 'w') as outfile:
        jsonFormat = json.dumps(_saveDict,sort_keys=True,indent=4)
        print(jsonFormat)
        outfile.write(jsonFormat)
        #json.dump(,outfile)
    # except:
    #     print("\n[GRESKA] Greska prilikom cuvanja podataka, podatci NISU SACUVANI, Poruka: ")
    # finally:
    #     print("\nGotovo cuvanje korisnika")


def loadUsers():
    usersDir = _dataDir+"users.json"
    if os.path.isfile(usersDir):
        print("Fajl sa korisnicima postoji, ucitavanje...")
        jsonFile = open(usersDir)
        jsonStr = jsonFile.read()
        jsonData = json.loads(jsonStr)
        _users = jsonData
        print("Gotovo ucitavanje korisnika!") 
    else:
        print("Fajl sa korisnicima ne postoji ili ima gesku, cuvanje default korisnika...")
        saveUsers(defaultSave=True)

def userExists(uname):
    return uname in _users

def addUser(user):
    username = user.GetUserName()
    if not userExists(username):
        _users[username] = user
        #saveUsers()

# korisnik1 = Korisnik(1,"LukaZ","Luka","Zagar","123")
# bibliotekar1 = Bibliotekar(2,"Petar66","Petar","Petric","321")


# addUser(korisnik1)
# addUser(bibliotekar1)

# saveUsers()


# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)