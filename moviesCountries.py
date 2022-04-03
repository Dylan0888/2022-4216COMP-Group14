"""

Movies - Countries (between two years)
By Mackenzie Whitehead

Main Graph Idea: 
A heatmap of countries showing the amount of movies released per country in a certain time frame

Steps:
    - Asks lower limit year
    - Asks upper limit year
    - Generates Heatmap of movies per countries between the two given dates
    - Change from coordinates to long lat method.

Extra:
    - Hover Over/ Click plotted points for more information



"""

# conda create -n geo-env -c conda-forge geopandas

# Imports
from matplotlib import image
from matplotlib import pyplot as plt
import numpy as np
import csv
from array import *
import pandas as pd


# Global Variables

# Temp for testing

#imageFile = "Resources\\WorldMap.png"
imageFile = "Resources\\world-map.jpg"
coordsFile = "Resources\\countryCoords.csv"
coordsArray = []
dataArray= []

# Functions

def mainOptions(movieTitle, country, year):
    yearOne = 0
    yearTwo = 0
    menuFlag = False
    yearsValid = False


    while(menuFlag== False):
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
            createGraphMulti(movieTitle, country, year, 1874, 2016)
            menuFlag = True
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
                createGraphMulti(movieTitle, country, year, yearOne, yearTwo)
            menuFlag = True
        elif(userOption == "3"):
            # Return to Main Menu
            menuFlag = True


def createGraph(movieTitle, country):
    loadMapCoordinates()

    # Temp Variables 
    countryMatch = False
    matchCounter = 0
    tempArray = []
    print("[SUB-FILE] Successfully Passed Full Array into Sub File!")
    for i in range (len(movieTitle)):
        #print(i, ": ", movieTitle[i], " - ", country[i])
        for j in range (len(coordsArray)):
            countryMatch = False
            splitArray = coordsArray[j].split(",")
         #   print("Testing Match: " + splitArray[0] + " and " + country[i])
            if splitArray[0] == country[i]:
                amtCounter = int(splitArray[3]) + 1
                #print("Adding 1 to country" + country[i])
                coordsArray[j] = splitArray[0] + "," + splitArray[1] + "," + splitArray[2] + "," + str(amtCounter)
    #Once Finished, a Graph will be Plotted...
    plotOnMap(1874, 2016)


def createGraphMulti(movieTitle, country, year, yearOne, yearTwo):
    loadMapCoordinates()

    print("[DATA] Loading all Countries onto Map...")
    # Temp Variables 
    countryMatch = False
    matchCounter = 0
    tempArray = []
    for i in range (len(movieTitle)):
        #print(i, ": ", movieTitle[i], " - ", country[i])
        for j in range (len(coordsArray)):
            countryMatch = False
            splitArray = coordsArray[j].split(",")
         #   print("Testing Match: " + splitArray[0] + " and " + country[i])
            if splitArray[0] == country[i]:

                # add some checks for year
                if year[i].isnumeric():
                    if (int(year[i]) >= yearOne) and (int(year[i]) <= yearTwo):

                        amtCounter = int(splitArray[3]) + 1
                        #print("Adding 1 to country" + country[i])
                        coordsArray[j] = splitArray[0] + "," + splitArray[1] + "," + splitArray[2] + "," + str(amtCounter)
    #Once Finished, a Graph will be Plotted...
    plotOnMap(yearOne, yearTwo)
    print("[DATA] Map Successfully Created!")

def loadMapCoordinates():
    # Function reads in the coordinates from the coordinates file (found in the resources folder)
    print("[FILE] Loading Coordinates File! Please Wait...")
    rowCounter = 0

    # coords file format: country_code,latitude,longitude,country

    with open(coordsFile, newline='') as movieFile:
        spamreader = csv.reader(movieFile, delimiter= ',')
        for row in spamreader:
            #print("[FILE] Reading row Number ", row)
            rowToAdd = row[3] + ","+ row[2] + "," + row[1] + "," + "0"
            coordsArray.append(rowToAdd) # row with default amount 0

            if row[3] == "United Kingdom":
                rowToAdd = "UK" + ","+ row[2] + "," + row[1] + "," + "0"
                coordsArray.append(rowToAdd)
            if row[3] == "United States":
                rowToAdd = "USA" + ","+ row[2] + "," + row[1] + "," + "0"  
                coordsArray.append(rowToAdd)
            if row[3] == "Soviet Union":
                rowToAdd = "Russia" + ","+ row[2] + "," + row[1] + "," + "0" 
                coordsArray.append(rowToAdd)
            # coordsArray format:
            # country, x, y, amount

            rowCounter = rowCounter + 1
    print("[FILE] Successfully Loaded all File Coordinates! (",rowCounter, " Entries )")


def plotOnMap(yearOne, yearTwo):

    # Plot Options
    data = image.imread(imageFile)
    plt.title("Movies per Country (" + str(yearOne) + "-" + str(yearTwo) + ")")
   # plt.xlim(0, 1200)
   # plt.ylim(645, 0)
    plt.xlim(-180, 180) # coordinates changed to longitude latitude
    plt.ylim(-90, 90)
    plt.imshow(data, extent=(-180, 180, -90, 90))
    plt.annotate("Hello World", xy=(5, 500), xytext=(6, 550))
    plt.grid(b=None)
    splitArray = []

    # add Data Points
    print("[PLOT] Plotting Data, Please Wait...")
    for i in range (len(coordsArray)):
        print(coordsArray[i])
        splitArray = coordsArray[i].split(",")

        """
            splitArray Format:
            [0] = Country Name
            [1] = x coord
            [2] = y coord
            [3] = amount of films
        """
        addPoint(float(splitArray[1]),float(splitArray[2]), colourFormula(int(splitArray[3])), sizeFormula(splitArray[3])) # plots the point on the graph (see addPoint function)

    print("[PLOT] Finished Plotting Data, Displaying Map...")
#    plt.plot(-95.712891,37.09024, 'bo-', color='blue', ms=50, alpha=0.5) #test plot
    plt.plot(0,200, 'bo-', color='midnightblue', ms=20, alpha=0.5, label="Dark Blue: 5000+")
    plt.plot(0,200, 'bo-', color='blue', ms=20, alpha=0.5, label="Blue: 1000-5000")
    plt.plot(0,200, 'bo-', color='mediumpurple', ms=20, alpha=0.5, label="Purple: 500-1000")
    plt.plot(0,200, 'bo-', color='darkviolet', ms=20, alpha=0.5, label="Dark Violet: 400-500")
    plt.plot(0,200, 'bo-', color='violet', ms=20, alpha=0.5, label="Violet: 300-400")
    plt.plot(0,200, 'bo-', color='magenta', ms=20, alpha=0.5, label="Magenta: 200-300")
    plt.plot(0,200, 'bo-', color='crimson', ms=20, alpha=0.5, label="Crimson: 1-200")
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)
    plt.show()
#    cid = plt.canvas.mpl_connect('button_press_event', onclick)

    def onclick(event):
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
            ('double' if event.dblclick else 'single', event.button,
            event.x, event.y, event.xdata, event.ydata))
        print("Hello World")

def addPoint(x, y, colour, size):
    #This functions takes the coordinates of a datapoint with the size and colour and plots it onto the graph
    if size != 0:
        plt.plot(x, y, 'bo-', color=colour, ms=size, alpha=0.5)


def sizeFormula(amtMovies):
    # This is a Fomula used to calculate the Marker size for datapoints depending on the amount of movies from the country
    amt = int(amtMovies)
    size = 1000 # default size so if an error occurs, it can be seen on the graph
    if amt > 5000:
        size= amt*float(0.005)
    elif amt >= 1000:
        size= amt*float(0.02)
    elif amt >= 500:
        size= amt*float(0.015)
    elif amt >= 100:
        size= amt*float(0.04)
    elif amt < 100:
        if amt < 25:
            size= amt
        elif amt <= 0:
            amt = 0
        else:
            size= amt*float(0.05)
            if size <25:
                diff = size-25
                size = size + diff

    return int(size)
    #return 0.008 #- the smallest size if we use the above formula
    # idea: different colours have different size formulas

def colourFormula(amt):
    """
     TODO add a formula to make dots different colours
     Purple - small
     Red - Medium
     Blue - Large
     also make max dot size 100 or something
    """
    chosenColour = "grey" #default colour shows if error is made
    if amt >=5000:
        chosenColour = "midnightblue"
    elif amt >=1000:
        chosenColour = "blue"
    elif amt >=500:
        chosenColour = "mediumpurple"
    elif amt >=400:
        chosenColour = "darkviolet"
    elif amt >=300:
        chosenColour = "violet"
    elif amt >=200:
        chosenColour = "magenta"
    elif amt <200:
        chosenColour = "crimson"

    return chosenColour
