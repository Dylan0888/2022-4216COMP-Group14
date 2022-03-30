
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
            multiGraph (year, cast)
        
        else:
            print("Please select a valid input!")

# ---- Loads graph for single selected actor ---- # 
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
    #print ("The actor was found in the following: \n ")
    appereanceYear.sort()
    #print (appereanceYear, " and ",actorAppearances)
    #print (getImdb, "\n")
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

# ---- Loads Graph for double actor comparison ---- # 
def multiGraph(year, cast):
    
    # ---- Arrays used to store the data from the 'movies_initial.csv' for graph use ---- # 
    # a1 = Actor 1
    a1AppereanceYear = []
    a1ActorAppearances = []
    a1ActorList = []
    # a2 = Actor 2
    a2AppereanceYear = []
    a2ActorAppearances = []
    a2ActorList = []

    # ---- Loops to find the first actor in the data ---- # 
    a1Found = False
    while (a1Found != True):
        a1 = input("Please enter your first actors full name: ")
        for i in range(len(cast)):
            a1ActorList = str(cast[i]).split(", ")
            for j in range(len(a1ActorList)):                
                if a1ActorList[j] == str(a1): # if actor was found it will then find all the times their name appears 
                    a1Found = True  
                    if len(a1AppereanceYear) != 0:
                        if year[i] in a1AppereanceYear: # when the actor is found the dates are stored in the array 

                            for k in range(len(a1AppereanceYear)):
                                if int(a1AppereanceYear[k]) == int(year[i]):
                                    a1ActorAppearances[k] = int(a1ActorAppearances[k]) + 1 # if the same year is present then it will add one to that year    
                        else:
                            a1AppereanceYear.append(year[i])
                            a1ActorAppearances.append(int(1))
                               
                    else:
                        # if the year does not exist in the array then it will add it 
                        a1AppereanceYear.append(year[i])
                        a1ActorAppearances.append(int(1))
        # Validation for the user entered actor 
        if a1Found == False:
            print("Actor was not found, please enter another actor. \n")   
        elif a1Found == True:
            print("Actor Found")  
                    
    # ---- Users Enters second actor and scans through database ---- # 
    a2Found = False 
    while (a2Found != True):
            a2 = input("Please enter your second actors full name: ")
            for i in range(len(cast)):
                a2ActorList = str(cast[i]).split(", ")
                for j in range(len(a2ActorList)):                
                    if a2ActorList[j] == str(a2): # if actor was found it will then find all the times their name appears 
                        a2Found = True  
                        if len(a2AppereanceYear) != 0:
                            if year[i] in a2AppereanceYear: # when the actor is found the dates are stored in the array 

                                for k in range(len(a2AppereanceYear)):
                                    if int(a2AppereanceYear[k]) == int(year[i]):
                                            a2ActorAppearances[k] = int(a2ActorAppearances[k]) + 1 # if the same year is present then it will add one to that year    
                            else:
                                a2AppereanceYear.append(year[i])
                                a2ActorAppearances.append(int(1))
                                    
                        else:
                                # if the year does not exist in the array then it will add it 
                            a2AppereanceYear.append(year[i])
                            a2ActorAppearances.append(int(1))
                # Validation for the user entered actor 
            if a2Found == False:
                print("Actor was not found, please enter another actor. \n")   
            elif a2Found == True:
                print("Actor two Found")  
                 


    print("Loading multiple graphs....")

    fig, axs = plt.subplots(1,2, sharey=True)

    #-----Out of graph design-------#
    axs[0].set_title(a1, fontsize=16) # sets the title of the graph with the actors name so the graphs can be distinguished from each other #
    axs[0].set_xlabel("years", fontsize=10)
    axs[0].set_ylabel("Total of movies", fontsize=12)
    axs[0].plot(a1AppereanceYear, a1ActorAppearances, 'gD:')
    axs[0].tick_params(axis='x', labelrotation = 90) # Rotates the axis data to fit all on the graph 
    
    axs[1].set_title(a2, fontsize=16)
    axs[1].set_xlabel("years", fontsize=10)
    axs[1].plot(a2AppereanceYear, a2ActorAppearances, 'mD:')
    axs[1].tick_params(axis='x', labelrotation = 90) # Rotates the axis data to fit all on the graph 
    
    plt.ylim([0, 10]) # sets the scale on the y axis 
    plt.tight_layout()
    plt.show()
