import json

# Open a database file,
#   Send the file to where its called
#   Save the file when we need to  

def SaveDatabase():
    print("Saving...")

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)