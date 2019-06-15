from classes import knjiga

from libs import ui
from libs import db

from classes.korisnik import Korisnik
from classes.bibliotekar import Bibliotekar

db.loadUsers()
db.loadBooks()
db.loadRentedBooks()


def verifyLogin(user):
    if user == None:
        return
    _username = user["Username"]
    _pwd = user["Password"]

    users = db.getUsers()

    for k, v in users.items():
        if _username == k and _pwd == v.password:  # do we have a user with the specified name and pwd?
            if v.isDeleted():
                input("KORISNIK JE IZBRISAN")
                return
            
            loggedInUser = v
            db.setActiveUser(v)
            ui.successfullLogin(loggedInUser)
            return loggedInUser

    print("<NETACNA LOZINKA ILI KORISNICKO IME>")
    return False


exit = False
while not exit:  # continious ui display
    logingInUser = ui.showLogin()  # {username,pwd}
    activeUser = verifyLogin(logingInUser)
    if not activeUser == False:  # we loged in successfully, show the second menu
        _exit = False
        if activeUser == None:
            input("ODUSTALI STE OD PRIJAVE")
            _exit = True
        while not _exit:
            _exit = ui.showUserMenu(activeUser)
            if _exit == "Q" or "q":
                _exit = True
        exit = True
