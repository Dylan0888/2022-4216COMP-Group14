"""

Movies - Countries (between two years)
By Mackenzie Whitehead

Main Graph Idea: 
A heatmap of countries showing the amount of movies released per country in a certain time frame

Steps:
    - Asks lower limit year
    - Asks upper limit year
    - Generates Heatmap of movies per countries between the two given dates

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
imageFile = "Resources\\WorldMap.png"
coordsFile = "Resources\\MapCoords.csv"
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

    with open(coordsFile, newline='') as movieFile:
        spamreader = csv.reader(movieFile, delimiter= ',')
        for row in spamreader:
            print("[FILE] Reading row Number ", row)
            rowToAdd = row[0] + ","+ row[1] + "," + row[2] + "," + "0"
            coordsArray.append(rowToAdd) # row with default amount 0
            # coordsArray format:
            # country, x, y, amount

            rowCounter = rowCounter + 1
    print("[FILE] Successfully Loaded all File Coordinates! (",rowCounter, " Entries )")


def plotOnMap():

    # Plot Options
    data = image.imread(imageFile)
    plt.title("Movies per Country")
    plt.xlim(0, 1200)
    plt.ylim(645, 0)
    splitArray = []

    # add Data Points
    print("[PLOT] Plotting Data, Please Wait...")
    print("Length is ", len(coordsArray))
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
        addPoint(float(splitArray[1]),float(splitArray[2]),"purple", sizeFormula(splitArray[3])) # plots the point on the graph (see addPoint function)
        print("[PLOT] Plotted Country data for ", splitArray[0], "!")

    print("[PLOT] Finished Plotting Data, Displaying Map...")
    plt.imshow(data)
    plt.show()

def addPoint(x, y, colour, size):
    #This functions takes the coordinates of a datapoint with the size and colour and plots it onto the graph
    plt.plot(x, y, 'bo-', color=colour, ms=size, alpha=0.5)


def sizeFormula(amtMovies):
    # This is a Fomula used to calculate the Marker size for datapoints depending on the amount of movies from the country
    print(amtMovies)
    size= int(amtMovies)*float(0.008)
    return int(size)

def colourFormula(colour):
    """
     TODO add a formula to make dots different colours
     Purple - small
     Red - Medium
     Blue - Large
     also make max dot size 100 or something
    """