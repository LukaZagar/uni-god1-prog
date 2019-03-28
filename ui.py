

def showLogin():
    print("\n\nUlogovanje u sistem...")
    username = input("Unesite korisnicko ime: ")
    pwd = input("Unesite password: ")
    return {
        "Username": str(username),
        "Password": str(pwd)
    }


def successfullLogin(userClass):
    print("\n=================================")
    print("====== USPESNO ULOGOVANI ========")
    print("=================================")
    print("ID:           "+str(userClass.id))
    print("Nalog:        "+userClass.username)
    print("Vrsta naloga: "+userClass.AccessLevelToString())
    print("=================================\n")

def showUserMenu(userLevel):
    if userLevel == 1: ## bibliotekar
        print("Selektujte opciju:")
    else: ## user or unknown
        print("Selektujte opciju:")
        print("1.Pregled zaduzenih knjiga.")
        print("2.Pretrazivanje knjiga.")
        print("3.Izmena podataka korisnickog naloga.")
        print("4.Izlaz iz sistema")
    
    result = input("Unesite broj zeljene akcije: ")
    return result