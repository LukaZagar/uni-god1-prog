import json
from Korisnik import Korisnik
from Bibliotekar import Bibliotekar

import sys
import os

_users = {}

def getUsers():
    return _users

def saveUsers():
    print("Cuvanje korisnika...")
    fileDir = os.path.dirname(os.path.abspath(__file__))
    usersDir = fileDir+"/users.json"
   
    _saveDict = {}
    for k,_user in _users:
        _saveDict[k] = _user.ToJSON()

    #try:
    
    with open(usersDir, 'w') as outfile:
        json.dump(json.dumps(_users),outfile)

    # except:
    #     print("\nGreska prilikom cuvanja podataka, podatci NISU SACUVANI")
    # finally:
    #     print("\nGotovo cuvanje korisnika")

def userExists(uname):
    return uname in _users

def addUser(user):
    username = user.GetUserName()
    if not userExists(username):
        _users[username] = user
        #saveUsers()
    
korisnik1 = Korisnik(1,"LukaZ","Luka","Zagar","123")
bibliotekar1 = Bibliotekar(2,"Petar66","Petar","Petric","321")


addUser(korisnik1)
addUser(bibliotekar1)

saveUsers()


# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)