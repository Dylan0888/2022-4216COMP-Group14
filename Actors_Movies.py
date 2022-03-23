
# ---- Imports ---- #
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ---- User Menu ---- #
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

#Loads graph for single selected actor 
def singGraph(year, cast, imdbRating):
   
    # ---- Variables for the loop to store data in ---- # 
    appereanceYear = [] 
    actorAppearances = []
    actorList = []
    getImdb = []
    actorFound = False 

    # ensures the user entered an actor that is in the data base 
    while (actorFound != True):
        chosenActor = input("Please enter your actors full name: ")
        for i in range(len(cast)):
            actorList = str(cast[i]).split(", ")
            for j in range(len(actorList)):                
                if actorList[j] == str(chosenActor): # if actor was found it will then find all the times their name appears 
                    actorFound = True  
                    if len(appereanceYear) != 0:
                        if year[i] in appereanceYear: # when the actor is found the dates are stored in the array 

                            for k in range(len(appereanceYear)):
                                if int(appereanceYear[k]) == int(year[i]):
                                    actorAppearances[k] = int(actorAppearances[k]) + 1 # if the same year is present then it will add one to that year    
                        else:
                            appereanceYear.append(year[i])
                            actorAppearances.append(int(1))
                            getImdb.append(imdbRating[i])    
                    else:
                        # if the year does not exist in the array then it will add it 
                        appereanceYear.append(year[i])
                        actorAppearances.append(int(1))
        # Validation for the user entered actor 
        if actorFound == False:
            print("Actor was not found, please enter another actor. \n")   
        elif actorFound == True:
            print("Actor Found")   
                   
    # ------ Prints none graphed data out for the user ----- #
    print ("The actor was found in the following: \n ")
    appereanceYear.sort()
    print (appereanceYear, " and ",actorAppearances)
    print (getImdb, "\n")
    print("Loading graph...")

    # ---- Graph Design ---- #
    fig, ax = plt.subplots()
    ax.plot(appereanceYear, actorAppearances, 'go--', label="Movies") #Green Plot
    fig.suptitle("Annual movie appearances", fontsize=18)
    ax.set_title("Actor: "+ chosenActor, fontsize=14)
    ax.set_xlabel("Years", fontsize=12)
    ax.set_ylabel("Amount of movies", fontsize=12, color='g')
    ax.plot(getImdb, 'ro--', label="Rating") #Red Plot 
    ax.set_yticks(range(1, 11, 1))

    #---Used to add second axis lable on the right of the graph---#
    ax1 = ax.twinx()
    ax1.set_ylabel("IMDB rating Average", fontsize=12 , color='r')
    ax1.set_yticks(range(1, 11, 1))

    # ---- design of graph ---- # 
    plt.xlim([1, 10])
    ax.legend()#adds axis lables on the graph
    ax.grid(True) # Shows grid design for easier viewing 
    ax1.grid(False)
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


