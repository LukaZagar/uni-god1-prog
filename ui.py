


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




def successfullLogin(userClass):
    print("\n=================================")
    print("====== USPESNO ULOGOVANI ========")
    print("=================================")
    print("ID:           "+str(userClass.id))
    print("Nalog:        "+userClass.username)
    print("Vrsta naloga: "+userClass.AccessLevelToString())
    print("=================================\n")

def showUserMenu(user):
    global activeUser 
    activeUser = user
    # userLevel = userLevel or 0
    
    print("Selektujte opciju:")
    printModularMenu("mainMenu")
    
    print('Q.Izlaz iz sistema')
    result = input("Unesite broj zeljene akcije: ")
    return result




_uiMenus = {
    1 : { #bibliotekar
        "mainMenu": {
            1: {
                "text":"Unos i izmena podataka o Knjigama",
                "onSelect": "modifyUser"
            },
            2:{
                "text":"Unos podataka za Bibliotekara i Korisnika",
                "onSelect": "modifyUser"
            },
            3:{
                "text":"Izmena podataka trenutno prijavljenog Bibliotekara",
                "onSelect": "modifyUser"
            },
            4:{
                "text":"Zaduživanje i razduživanje Korisnika",
                "onSelect": "modifyUser"
            }, 
            5:{
                "text":"Rashodovanje knjiga",
                "onSelect": "modifyUser"
            }, 
            6:{
                "text":"Brisanje Korisnika",
                "onSelect": "modifyUser"
            }
        },
        "modifyUser":{
            1:{
                "text":"XD",
                "onSelect": "mainMenu"
            }
        }
    },
    2 : {
        "mainMenu": {
            1: "Pregled zaduzenih knjiga.",
            2: "Pretrazivanje knjiga.",
            3: "Izmena podataka korisnickog naloga.",
        }
    },
}


def printModularMenu(id):
    
    acclvl = activeUser.GetAccessLevel()
     
    for k,v in _uiMenus[acclvl].items():
        for _k,_v in v.items():
            print("["+str(_k)+"] "+_v["text"])





