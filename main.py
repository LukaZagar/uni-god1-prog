import knjiga

import ui
import db

from Korisnik import Korisnik
from Bibliotekar import Bibliotekar


def verifyLogin(user):
    if user == None : return 
    _username = user["Username"]
    _pwd = user["Password"]

    for k,v in db.getUsers().items():  
        if _username == v.username and _pwd == v.password: #do we have a user with the specified name and pwd?            
            ui.successfullLogin(v)
            return db.getUsers()[k]
        
    print("<NETACNA LOZINKA ILI KORISNICKO IME>")
    return False  
            


exit = False
while not exit: # continious ui display
    logingInUser = ui.showLogin() # {username,pwd}
    activeUser = verifyLogin(logingInUser)
    if not activeUser == False: # we loged in successfully, show the second menu
        _exit = False
        if activeUser == None:
            print("ODUSTALI STE OD PRIJAVE")
            _exit = True
        while not _exit:
            _exit = ui.showUserMenu(activeUser)
            if _exit == "Q" or "q":
                _exit = True
        exit = True



