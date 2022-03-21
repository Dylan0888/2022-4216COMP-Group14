
# --- Imports ---#
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def menuOptions(year, cast, imdbRating):
    # Users choice will lead to a spacific graph being shown
    userSelection = False 
    while (userSelection != True):
        userChoice = input("""
            Would you like to visulise a single actor and their roles or compare two actors?

            ------ Options ------
        \t 1. Single Actor
        \t 2. Multiple Actors 
            ---------------------
            """)

        if userChoice == "1":
            userSelection = True
            singGraph(year, cast, imdbRating)
            
        elif userChoice == "2":
            userSelection = True
            multiGraph ()
        
        else:
            print("Please select a valid input!")


# scans through file and gets the actors and imdb ratings 
#def getSelected():
 #   actor = pd.read_csv("movies_initial.csv")
  #  compareActors = actor["cast"]
    #print(compareActors) # tests the outputs 



#Loads graph for single selected actor 
def singGraph(year, cast, imdbRating):
    chosenActor = input("Please enter your actor of choice:")
    appYear = [] #Actor Appereances per year 
    movieAppearances = []
    
    print("Compering your choice to the records... ")
    
    actor = pd.read_csv("movies_initial.csv")
    compareActors = actor["cast"]

    for i in range (len(cast)):
        if cast[i] == chosenActor:
            for l in range (len(year)):
                appYear = year
                movieAppearances.count 
                
    
    
    
    
    
    
    
    
    
    print("Loading graph...")
    #------------Example graph data--------#
    #years = [1,2,3,4,5,6]
    #movieAppearances = [1,2,3,4,5,6] 
    imdbRatings = [2, 3.5, 4, 9, 10.2, 11]

    fig, ax = plt.subplots()
    ax.plot(appYear, movieAppearances, 'go--', label="Movies") #Green Plot

    #-----Out of graph design-------#
    fig.suptitle("Annual movie appearances", fontsize=18)
    ax.set_title("Actor: "+ chosenActor, fontsize=14)
    ax.set_xlabel("Years", fontsize=12)
    ax.set_ylabel("Amount of movies", fontsize=12, color='g')
    ax.plot(appYear, imdbRatings, 'ro--', label="Rating") #Red Plot #

    #---Used to add second axis lable on the right of the graph---#
    ax1 = ax.twinx()
    ax1.set_ylabel("IMDB rating Average", fontsize=12 , color='r')

    ax.legend()#adds axis lables on the graph
   
    ax.grid(True) # Shows grid design for easier viewing 
    plt.show()

def multiGraph():
    actor1 = input("Please enter your first actor:")
    actor2 = input("Please enter your second actor:")
    
    print("Loading multiple graphs....")

    actorOneYears = [1,2,3,4,5,6]
    actorTwoYears = [8,9,10,11,12,13]
    movieAppearances = [1,2,3,4,5,6]

    fig, axs = plt.subplots(1,2, sharey=True)

    #-----Out of graph design-------#
    axs[0].set_title(actor1, fontsize=16)
    axs[1].set_title(actor2, fontsize=16)
    axs[0].set_xlabel("years", fontsize=12)
    axs[1].set_xlabel("years", fontsize=12)
    axs[0].set_ylabel("Total of movies", fontsize=12)

    axs[0].plot(actorOneYears, movieAppearances, 'gD:')
    axs[1].plot(actorTwoYears, movieAppearances, 'mD:')

    plt.tight_layout()
    plt.show()


