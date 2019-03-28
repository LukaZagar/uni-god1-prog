import json
from main import _users

# Open a database file,
#   Send the file to where its called
#   Save the file when we need to  

def saveUsers():
    print("Cuvanje korisnika...")
    try:
        with open('/data/users.txt', 'w') as outfile:
            json.dump(_users,outfile)

    except:
        print("\nGreska prilikom cuvanja podataka, podatci NISU SACUVANI")
    finally:
        print("\nGotovo cuvanje korisnika")
    


# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)