_uiMenus = {
    1 : { #bibliotekar
        "mainMenu": {
            1: "Unos i izmena podataka o Knjigama",
            2: "Unos podataka za Bibliotekara i Korisnika",
            3: "Izmena podataka trenutno prijavljenog Bibliotekara",
            4: "Zaduživanje i razduživanje Korisnika",
            5: "Rashodovanje knjiga",
            6: "Brisanje Korisnika",
        }    
    }
}

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

def printModularMenu(acclvl,id):
    for k,v in _uiMenus[acclvl][id]
        print("[ "+k+"] "+v)


def successfullLogin(userClass):
    print("\n=================================")
    print("====== USPESNO ULOGOVANI ========")
    print("=================================")
    print("ID:           "+str(userClass.id))
    print("Nalog:        "+userClass.username)
    print("Vrsta naloga: "+userClass.AccessLevelToString())
    print("=================================\n")

def showUserMenu(user):
    # userLevel = userLevel or 0
    userLevel = user.GetAccessLevel()
    
    if userLevel == 1: ## bibliotekar
        print("Selektujte opciju:")
        printModularMenu(userLevel,"mainMenu")
        # print("1.Unos i izmena podataka o Knjigama")
        # print("2.Unos podataka za Bibliotekara i Korisnika")
        # print("3.Izmena podataka trenutno prijavljenog Bibliotekara")
        # print("4.Zaduživanje i razduživanje Korisnika")
        # print("5.Rashodovanje knjiga")
        # print("6.Brisanje Korisnika")
    else: ## user or unknown
        print("Selektujte opciju:")
        print("1.Pregled zaduzenih knjiga.")
        print("2.Pretrazivanje knjiga.")
        print("3.Izmena podataka korisnickog naloga.")
        #print("4.Izlaz iz sistema")
    
    print('Q.Izlaz iz sistema')
    result = input("Unesite broj zeljene akcije: ")
    return result