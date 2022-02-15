# Imports
import csv
from array import *


# Global Variables
menuFlag = False


# Global Arrays
MovieDataRaw = []


# Functions
def loadFile():
    print("[FILE] Loading all File Contents! Please Wait...")
    rowCounter = 0

    with open('movies_initial.csv', newline='') as movieFile:
        spamreader = csv.reader(movieFile, delimiter= ',')
        for row in spamreader:
            # do something with data here
            movieRow = ', '.join(row)
            MovieDataRaw.append(movieRow) # Adds Movie Data from file into the Array named 'MovieDataRaw'
#            print("Loaded Row ", rowCounter) # shows each line being red (for test purposes)
            rowCounter = rowCounter + 1
    print("[FILE] Successfully Loaded all File Contents! (",rowCounter, " Entries )")




# Main Code

loadFile() # Loads file when program is started

while(menuFlag== False):
    print("""
    -----------( Main Menu )-----------
    \t  -+- Menu Options: -+-
    \t 1. Graph 1 - Something
    \t 2. Graph 2 - Something
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

        # test 
        print(MovieDataRaw[3])

        menuFlag = True
    elif(userOption == "2"):
        # Dylan Function
        print("Running Option 2")
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