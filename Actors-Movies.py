# shows menu, asks to enter actor 
# can present one actor or asks to disaply multple acotrs to compare to each oterh 
# Opt 1: enter acotor ---- shows a unqiue graph to the acotr 
# opt 2: Allows multiple acotrs to be entered to compare 

# option 1 shows data in function plots 
# option 2 shows data in multi bar plot 

singleChoice = False
multiChoice = False 

# Users choice will lead to a spacific graph being shown 
while (singleChoice != True or multiChoice != True):
    userChoice = input("""
        ------------------
   
        Would you like to analyse one actor and the movies they've been in per year or multiple?
    
        ------ Options ------
    \t 1. Single Actor
    \t 2. Multiple Actors 
        
        """)

    if userChoice == "1":
        singleChoice = True
        print(singleChoice)

    elif userChoice == "2":
        print("22222")
        multiChoice = True
    else:
        print("Please select a valid input!")


if singleChoice == True:
        print("outputting single graph ")
        #
        #
        #
        #
elif multiChoice == True:
    print("running code for multiple actors")
