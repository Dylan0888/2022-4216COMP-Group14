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
movieTitle = ["Spiderman", "Batman", "Harry Potter"]
movieCountry = ["USA", "UK", "Spain"]
year = ["", "", ""]
#imageFile = "Resources\\WorldMap.png"
imageFile = "Resources\\world-map.jpg"
coordsFile = "Resources\\countryCoords.csv"
coordsArray = []
dataArray= []

# Functions

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
    plotOnMap()


def loadMapCoordinates():
    # Function reads in the coordinates from the coordinates file (found in the resources folder)
    print("[FILE] Loading Coordinates File! Please Wait...")
    rowCounter = 0

    # coords file format: country_code,latitude,longitude,country

    with open(coordsFile, newline='') as movieFile:
        spamreader = csv.reader(movieFile, delimiter= ',')
        for row in spamreader:
            print("[FILE] Reading row Number ", row)
            rowToAdd = row[3] + ","+ row[2] + "," + row[1] + "," + "0"
            coordsArray.append(rowToAdd) # row with default amount 0
            # coordsArray format:
            # country, x, y, amount

            rowCounter = rowCounter + 1
    print("[FILE] Successfully Loaded all File Coordinates! (",rowCounter, " Entries )")


def plotOnMap():

    # Plot Options
    data = image.imread(imageFile)
    plt.title("Movies per Country")
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
        print("[PLOT] Plotted Country data for " + splitArray[0] + "!")

    print("[PLOT] Finished Plotting Data, Displaying Map...")
#    plt.plot(-95.712891,37.09024, 'bo-', color='blue', ms=50, alpha=0.5) #test plot

    plt.show()

def addPoint(x, y, colour, size):
    #This functions takes the coordinates of a datapoint with the size and colour and plots it onto the graph
    plt.plot(x, y, 'bo-', color=colour, ms=size, alpha=0.5)


def sizeFormula(amtMovies):
    # This is a Fomula used to calculate the Marker size for datapoints depending on the amount of movies from the country
    amt = int(amtMovies)
    size = 1000 # default size so if an error occurs, it can be seen on the graph
    if amt > 5000:
        size= amt*float(0.005)
    elif amt >= 1000:
        size= amt*float(0.01)
    elif amt >= 500:
        size= amt*float(0.015)
    elif amt < 500:
        size= amt*float(0.02)

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
        chosenColour = "blue"
    elif amt >=1000:
        chosenColour = "purple"
    elif amt >=500:
        chosenColour = "red"
    elif amt <500:
        chosenColour = "orange"

    return chosenColour

