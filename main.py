# Imports
import csv
from array import *
import pandas as pd

# Import files of Everyone 
import moviesCountries as mc  # Mackenzie's File
#import Actors_Movies as optionTwo # Dylans file

# Global Variables
menuFlag = False


# Global Arrays
movieDataRaw = []


# Functions
def loadFile():
    print("[FILE] Loading all File Contents! Please Wait...")
    rowCounter = 0

    with open('movies_initial.csv', newline='') as movieFile:
        spamreader = csv.reader(movieFile, delimiter= ',')
        for row in spamreader:
            # do something with data here
#            movieRow = ', '.join(row)
            movieDataRaw.append(row) # Adds Movie Data from file into the Array named 'MovieDataRaw'
#            print("Loaded Row ", rowCounter) # shows each line being red (for test purposes)
            rowCounter = rowCounter + 1
    print("[FILE] Successfully Loaded all File Contents! (",rowCounter, " Entries )")

def newLoadFile():
    print ("[FILE] Loading Specific Category...")
    data = pd.read_csv("movies_initial.csv")
    C = data["imdbRating"]
    print(C)


def loadCategory(chosenCategory):
    # Input a category name, loads specified category into an array and returns it.
    # If input category is not valid, -1 will be returned
    validCat = False
    # Array of categories from Excel Spreadsheet
    availableCat = ["imdbID", "title", "year", "rating", "runtime", "genre", "released", "director", "writer", "cast", "metacritic", "imdbRating", "imdbVotes", "poster", "plot", "fullplot", "language", "country", "awards", "lastupdated", "type"]
    for i in range (len(availableCat)):
        if(chosenCategory == availableCat[i]):
            validCat = True
            break
    if(validCat):
        data = pd.read_csv("movies_initial.csv")
        chosenCatArray = data[chosenCategory] # Uses input Category and reads from the file.
        return chosenCatArray
    else:
        print("[ERROR] Specified Category is not a Valid Option!")
        return -1

# Main Code

loadFile() # Loads file when program is started

while(menuFlag== False):
    print("""
    -----------( Main Menu )-----------
    \t  -+- Menu Options: -+-
    \t 1. Graph 1 - Movies Per Country
    \t 2. Graph 2 - Actors an Movies Per Year
    \t 3. Graph 3 - Something
    \t 4. Graph 4 - Something
    \t 5. Graph 5 - Something
    \t 6. Graph 6 - Something 
    \t 7. Quit
    -----------------------------------
    """)

    userOption = input("Pick an Option: ") # Asks User to pick a menu Option

    if(userOption == "1"):
        # Mackenzie Function
        print("Running Option 1")
        mc.createGraph(loadCategory("title"), loadCategory("country"))
        menuFlag = True
    elif(userOption == "2"):
        # Dylan Function
        print("Running Option 2")
        #optionTwo.loadData(loadCategory("year"), loadCategory("cast"), loadCategory("imdbRating")
        menuFlag = True
    elif(userOption == "3"):
        # Reece Function
        print("Running Option 3")
        menuFlag = True
    elif(userOption == "4"):
        # Sai Function
        print("Running Option 4")
        menuFlag = True
    elif(userOption == "5"):
        # Mohammed Function 
        print("Running Option 5")
        menuFlag = True
    elif(userOption == "6"):
        # Bradley Function
        print("Running Option 6")    
        menuFlag = True 
    elif(userOption == "7"):
        # Exit Function
        print("Exiting the Program...\n ")    
        menuFlag = True 
    else: 
        print("Invalid Input! Please Pick a Menu Option (1-6).") # Validation to ensure Number is between 1 and 7