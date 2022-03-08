# shows menu, asks to enter actor 
# can present one actor or asks to disaply multple acotrs to compare to each oterh 
# Opt 1: enter acotor ---- shows a unqiue graph to the acotr 
# opt 2: Allows multiple acotrs to be entered to compare 

# option 1 shows data in function plots 
# option 2 shows data in multi bar plot 

# Imports
import matplotlib.pyplot as plt
import numpy as np


#Global Vaiables 
userSelection = False

#Loads graph for single selected actor 
def singGraph ():
    print("Loading graph...")

    years = [1,2,3,4,5,6]
    movieAppearances = [10,11,12,14,15,16]

    fig, ax = plt.subplots()
    ax.plot(years, movieAppearances, 'go--')

    #-----Out of graph design-------#
    ax.set_title("Annual actor appearances", fontsize=16)
    ax.set_xlabel("Years", fontsize=12)
    ax.set_ylabel("Amount of movies", fontsize=12)

    plt.show()



def multiGraph ():
    print("Loading multiple graphs....")


# Users choice will lead to a spacific graph being shown 
while (userSelection != True):
    userChoice = input("""
        Would you like to visulise a single actor and their roles or multiple actors?

        ------ Options ------
    \t 1. Single Actor
    \t 2. Multiple Actors 
        ---------------------
        """)

    if userChoice == "1":
        userSelection = True
        singGraph()
        
        

    elif userChoice == "2":
        userSelection = True
        multiGraph ()
    
    else:
        print("Please select a valid input!")







