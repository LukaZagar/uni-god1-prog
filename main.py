import knjiga
from Korisnik import Korisnik
from Bibliotekar import Bibliotekar
import ui

_users = {}

korisnik1 = Korisnik(1,"LukaZ","Luka","Zagar","123")
bibliotekar1 = Bibliotekar(2,"Petar66","Petar","Petric","321")
#korisnik2.SetAccessLevel(1) # set to bibliotekar

def addUserToDB(user):
    _users[user.id] = user

addUserToDB(korisnik1)
addUserToDB(bibliotekar1)

### Name: verifyLogin
### Desc: Verifies if the inputed data is a valid user
### Param: user Table (Username string, Password string)
### Returns : User if the login is successfull, false if unsucc
def verifyLogin(user):
    if user == None : return 
    _username = user["Username"]
    _pwd = user["Password"]

    for k,v in _users.items():  
        if _username == v.username and _pwd == v.password: #do we have a user with the specified name and pwd?            
            ui.successfullLogin(v)
            return _users[k]
        
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



