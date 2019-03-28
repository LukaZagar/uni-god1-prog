import knjiga
from korisnik import Korisnik
import ui
_users = {}

korisnik1 = Korisnik(1,"LukaZ","123")
korisnik2 = Korisnik(2,"Petar","321")
korisnik2.SetAccessLevel(1) # set to bibliotekar

_users[korisnik1.id] = korisnik1
_users[korisnik2.id] = korisnik2

### Name: verifyLogin
### Desc: Verifies if the inputed data is a valid user
### Param: user Table (Username string, Password string)
### Returns : User if the login is successfull, false if unsucc
def verifyLogin(user):
    _username = user["Username"]
    _pwd = user["Password"]

    if _username == "Q" or "q":
        return False # don't do a loop if he decides to quit
    for k,v in _users.items():  
        if _username == v.username: #do we have a user with the specified name? 
            if _pwd == v.password:
                ui.successfullLogin(v)
                return _users[v.id]
            else:
                print("Unete sifra nije tacna")
    
    print("Korisnik sa imenom "+_username+" ne postoji u bazi!")
    return False   
            


exit = False
while not exit: # continious ui display
    logingInUser = ui.showLogin() # {username,pwd}
    user = verifyLogin(logingInUser)
    if not user == False: # we loged in successfully, show the second menu
        _exit = False
        while not _exit:
            _exit = ui.showUserMenu(user.GetAccessLevel())
            if _exit == "Q" or "q":
                _exit = True
        exit = True



