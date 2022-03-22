
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
    
    appereanceYear = [] #Actor Appereances per year 
    actorAppearances = []
    actorList = []
    print("Compering your choice to the records... ")
    
# ask for actor 
    chosenActor = input("Please enter your actors full name: ")
# search for actor 
    for i in range(len(cast)):
        actorList = str(cast[i]).split(", ")
        for j in range(len(actorList)):
            if actorList[j] == str(chosenActor):
                print("Found Actor")
                

                if len(appereanceYear) != 0:
                    if year[i] in appereanceYear:
                        for k in range(len(appereanceYear)):
                            if int(appereanceYear[k]) == int(year[i]):
                                actorAppearances[k] = int(actorAppearances[k]) + 1
                                #print("Test 222222")
                    else:
                        appereanceYear.append(year[i])
                        actorAppearances.append(int(1))
     
                else:
                    appereanceYear.append(year[i])
                    actorAppearances.append(int(1))
                    print("Test yeaasss")
# get total amount of films theyre in
    print (appereanceYear, " and ",actorAppearances)
# show on graph












#    actor = pd.read_csv("movies_initial.csv")
 #   compareActors = actor["cast"]

 #   for i in range (len(cast)):
 #       if cast[i] == chosenActor:
 #           movieAppearances = movieAppearances + 1
 #               
 #       else:
 #           print("Sorry your actor of choice is not in the database, please enter another.")
 #           break
 #   print(movieAppearances)
    
    
    
    
    
    
    
    
    print("Loading graph...")
    #------------Example graph data--------#
    #years = [1,2,3,4,5,6]
    #movieAppearances = [1,2,3,4,5,6] 
    imdbRatings = [2, 3.5, 4, 9, 10.2, 11]

    fig, ax = plt.subplots()
    ax.plot(appereanceYear, actorAppearances, 'go--', label="Movies") #Green Plot

    #-----Out of graph design-------#
    fig.suptitle("Annual movie appearances", fontsize=18)
    ax.set_title("Actor: "+ chosenActor, fontsize=14)
    ax.set_xlabel("Years", fontsize=12)
    ax.set_ylabel("Amount of movies", fontsize=12, color='g')
    #ax.plot(appYear, imdbRatings, 'ro--', label="Rating") #Red Plot #

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


