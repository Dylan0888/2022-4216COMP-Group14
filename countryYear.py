import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def menuOption(year, country):

    choiceSelected = False
    choiceInput = False
    countryList = []
    datesInvalid = True
    

    while (choiceSelected == False):
        userChoice = input("""
         ------- Menu options -----------
        [1] Country vs Country
        [2] All Countries
        [3] Exit
        
        --Please select a option--
            """)

        if userChoice == "1":
            choiceSelected = True
            print("Country vs Country selected")

            while(choiceInput == False):
                countryOne = str(input("Select a country: "))
                countryTwo = str(input("Select a second country: "))

                for i in range(len(country)):
                    countryList = str(country[i]).split(", ")
                    for j in range(len(countryList)):
                        if str(countryList[j]) == countryOne:  
                            choiceInput = True
                            if str(countryList[j]) == countryTwo:  
                                choiceInput = True

                if choiceInput == False:
                    print("Invalid input, please try again")    
                elif choiceInput == True:
                    choiceTwo = input("""
                     Would you like the data between two specific dates or all time?

                    [1] Two date
                    [2] All Time
        
                    --Please select a option--
                    """)
                    if (choiceTwo == "1"):
                        while (datesInvalid == True):
                            dateOne = int(input("Select the first date: "))
                            dateTwo = int(input("Select the second date: "))

                            if dateTwo < dateOne:
                                print("Second date must be more recent than the first, e.g. 1930-1940")
                                datesInvalid == True
                            if (dateOne >= 1874) and (dateTwo <= 2019):
                                datesInvalid = False
                            else: 
                                print("dates must be between 1874 and 2019, please try again")   
                        if datesInvalid == False:
                            createGraphOne(year, country, dateOne, dateTwo)

                    elif(choiceTwo == "2"):
                        print("havent done this yet")                 
        elif userChoice == "2":
            choiceSelected = True
            print("All Countries selected")
  
def createGraphOne(year, country, dateOne, dateTwo):
    print("havent done this yet")




    


    
            