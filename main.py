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
### Returns : True/False (if we loged in successfully)
def verifyLogin(user):
    for k,v in _users.items():  
        if user["Username"] == v.username: #do we have a user with the specified name? 
            if user["Password"] == v.password:
                ui.successfullLogin(v)
                return _users[v.id]
            else:
                print("Unete sifra nije tacna")
        else: #no user found with that name
            print("Korisnik sa imenom "+user["Username"]+" ne postoji u bazi!")
            return False


exit = False
while not exit: # continious ui display
    logingInUser = ui.showLogin() # {username,pwd}
    result = verifyLogin(logingInUser)
    if not result == False: # we loged in successfully, show the second menu
        _exit = False
        while not _exit:
            _exit = ui.showUserMenu()
            if _exit == "4":
                _exit = True
        exit = True



