# Imports
from concurrent.futures.process import _threads_wakeups
import csv
from array import *
import pandas as pd
from tkinter import *
import math

# Import files of Everyone 
import moviesCountries as mc  # Mackenzie's File
import countryYear as cvc # reeces pieces file
import Actors_Movies as am # Dylans file

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

def filterCategory(category, option):
    newCategory = []
# Options:
# betweenYears - remove ¿½ character and replace with -
# oneYear - if multiple years shown, only show first
# 
# 
# 
# 

    if option == "betweenYears":
        for i in range(len(category)):
            # remove ¿½ character and replace with -
            if "¿½" in category[i]:
                # takes only the first option 
                category[i].replace("¿½", "-")
    elif option == "oneYear":
        for i in range(len(category)):
            # remove ¿½ character and replace with -
            if "¿½" in category[i]:
                # takes only the first option 
                newCategory = category[i].split("¿½")
                category[i] = newCategory[0]
            if "�" in category[i]:
                newCategory = category[i].split("�")
                category[i] = int(newCategory[0])
    return category

def loadMultiCategory(catOne, catTwo, catThree, useCatThree):
    # Input a category name, loads specified category into an array and returns it.
    # If input category is not valid, -1 will be returned
    validCat = False
    data = pd.read_csv("movies_initial.csv")
    # Array of categories from Excel Spreadsheet
    availableCat = ["imdbID", "title", "year", "rating", "runtime", "genre", "released", "director", "writer", "cast", "metacritic", "imdbRating", "imdbVotes", "poster", "plot", "fullplot", "language", "country", "awards", "lastupdated", "type"]

    if(availableCat.index(catOne) >= 0 and availableCat.index(catOne) <= 20):
        if(availableCat.index(catTwo) >= 0 and availableCat.index(catTwo) <= 20):
            if(useCatThree == True):
                if(availableCat.index(catThree) >= 0 and availableCat.index(catThree) <= 20):
                    # all categories valid - using all three
                    validCat = True
            elif(useCatThree == False):
                # all categories valid - only using two
                validCat = True
        else:
            validCat = False
    else:
        validCat = False

    if(validCat):
        # category valid
        rawDataOne = data[catOne]
        rawDataTwo = data[catTwo]
        rawDataThree = data[catThree]
        for i in range(len(rawDataOne)):
            #print(rawDataOne[i])
            try:
                if(not(rawDataOne[i] or str(rawDataOne[i]).strip())):

                    #its empty
                    rawDataOne.pop(i)
                    rawDataTwo.pop(i)
                    if(useCatThree):
                        rawDataThree.pop(i)
            except:
                rawDataOne.pop(i)
                rawDataTwo.pop(i)
                if(useCatThree):
                    rawDataThree.pop(i)
        for i in range(len(rawDataTwo)):
            #print(rawDataTwo[i])
            try:
                if(not(rawDataTwo[i] or str(rawDataTwo[i]).strip())):
                    #its empty
                    rawDataOne.pop(i)
                    rawDataTwo.pop(i)
                    if(useCatThree):
                        rawDataThree.pop(i)
            except:
                rawDataOne.pop(i)
                rawDataTwo.pop(i)
                if(useCatThree):
                    rawDataThree.pop(i)
        if(useCatThree):
            for i in range(len(rawDataThree)):
                try:
                    if(not(rawDataThree[i] or str(rawDataThree[i]).strip())):
                        #its empty
                        rawDataOne.pop(i)
                        rawDataTwo.pop(i)
                        rawDataThree.pop(i)
                except:
                    rawDataOne.pop(i)
                    rawDataTwo.pop(i)
                    rawDataThree.pop(i)



        return rawDataOne, rawDataTwo, rawDataThree


    else:
        # category invalid
        print("[ERROR] Specified Category is not a Valid Option!")
        return -1
    


def filterBetweenYears(yearOne, yearTwo, yearsCat, catTwo, catThree, useCatThree):
    # useCatThree should be a boolean value that decides wether the third category will be used (if unused put "none" for catThree)
    # Return meanings: 
    # - "-1" an error occured
    beforeCount = len(yearsCat)
    newYearsArray = []
    newArrayTwo = []
    newArrayThree = []
    sorted = False
    counter = 0
    i = 0

    while(sorted == False):
        if(True):
            if(int(yearsCat[i]) >= yearOne) and (int(yearsCat[i]) <= yearTwo):
                #print("removing ", yearsCat[i])
                newYearsArray.append(yearsCat[i])
                newArrayTwo.append(catTwo[i])
                counter=counter+1
                if(useCatThree):
                    newArrayThree.append(catThree[i])
                counter=counter+1
                i=i+1
            else:
                i=i+1
        else:
            #print("removing ", yearsCat[i])
            i=i+1
        if(i >=len(yearsCat)):
            sorted=True

    print("[FILTER] Successfully Filtered Data: Removed ", beforeCount-len(yearsCat), " Row(s)!")
    #print(len(yearsCat), len(catTwo), len(catThree))
    return newYearsArray, newArrayTwo, newArrayThree


# Main Code

while(menuFlag== False):
        
    print("""
    -----------( Main Menu )-----------
    \t  -+- Menu Options: -+-
    \t 1. Graph 1 - Movies Per Country
    \t 2. Graph 2 - Actors an Movies Per Year
    \t 3. Graph 3 - Countries vs Countires
    \t 4. Graph 4 - Something 
    \t 5. Quit
    -----------------------------------
    """)

    userOption = input("Pick an Option: ") # Asks User to pick a menu Option

    if(userOption == "1"):
        # Mackenzie Function
        #mc.createGraph(loadCategory("title"), loadCategory("country"))
        #mc.mainOptions(loadCategory("title"), loadCategory("country"), filterCategory(loadCategory("year"), "oneYear"))
        yearOne = 0
        yearTwo = 0
        menuFlag2 = False
        yearsValid = False


        while(menuFlag2== False):
            print("""
            -------( Movie Countries Options )-------
            \t  -+- Menu Options: -+-
            \t 1. Show All Movies / Country
            \t 2. Movies / Country between two Years
            \t 3. Return to Main Menu
            -----------------------------------------
            """)

            userOption = input("Pick an Option: ") # Asks User to pick a menu Option

            if(userOption == "1"):
                # Movies Per Country with set dates
                movTitle, movCount, movYear = loadMultiCategory("title", "country", "year", True)
                movYearFil = filterCategory(movYear, "oneYear")
                movYearnew, movTitlenew, movCountnew = filterBetweenYears(1874, 2016, movYearFil, movTitle, movCount, True)
                mc.createGraphMulti(movTitlenew, movCountnew, movYearnew, 1874, 2016)
                menuFlag2 = True
            elif(userOption == "2"):
                # Movies Per Country between Dates

                while(yearsValid== False):
                    yearOne = int(input("Choose the First Year to show Movies Between: "))
                    yearTwo = int(input("Choose the Second Year to show Movies Between: "))

                    if yearTwo < yearOne:
                        print("[ERROR] The Years Must be Input in Chronological Order!")
                        yearsValid = False
                    if (yearOne >= 1874) and (yearTwo <= 2016):
                        yearsValid = True
                        break
                    else:
                        yearsValid = False
                        print("[ERROR] The Years Must be between 1874 and 2016!")

                if yearsValid == True:
                    movTitle, movCount, movYear = loadMultiCategory("title", "country", "year", True)
                    movYearFil = filterCategory(movYear, "oneYear")
                    movYearnew, movTitlenew, movCountnew = filterBetweenYears(yearOne, yearTwo, movYearFil, movTitle, movCount, True)

                    mc.createGraphMulti(movTitlenew, movCountnew, movYearnew, yearOne, yearTwo)
                menuFlag2 = True
            elif(userOption == "3"):
                # Return to Main Menu
                menuFlag2 = True


        menuFlag = True
    elif(userOption == "2"):
        # Dylan Function
        print("Running Option 2")
        am.menuOptions(loadCategory("year"), loadCategory("cast"), loadCategory("imdbRating"))
        menuFlag = True
    elif(userOption == "3"):
         # Reece Function 
        print("Running Option 3")
        cvc.menuOption(loadCategory("year"), loadCategory("country"))
        menuFlag = True
    elif(userOption == "4"):
        # Bradley Function
        print("Running Option 4")
        menuFlag = True  
    elif(userOption == "5"):
        # Exit Function
        print("Exiting the Program...\n ")    
        menuFlag = True 
    else: 
        print("Invalid Input! Please Pick a Menu Option (1-5).") # Validation to ensure Number is between 1 and 7