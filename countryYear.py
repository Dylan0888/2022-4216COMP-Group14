import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def menuOption(year, country):

    choiceSelected = False
    choiceInput = False

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

                if countryOne is country:
                    print("Invalid input, please try again")
                    choiceInput = False

                if countryTwo is country:
                    print("Invalid input, please try again")
                    choiceInput = False

                if countryOne and countryTwo is not country:
                    choiceInput = True
                
                else:
                    choiceInput = False
                    print("Invalid input, please try again")  

            if choiceInput == True:           
                yearMenu(year, country)
                userChoice = True


        elif userChoice == "2":
            choiceSelected = True
            print("All Countries selected")
    
def yearMenu(year, country):
    datesInvalid = True

    userChoice2 = input("""
    Would you like the data between two specifc dates or all time?

        [1] Two dates
        [2] All time
        [3] Exit
        
        --Please select a option--
            """)   

    if userChoice2 == "1":
        while(datesInvalid == True):
            dateOne = int(input("Select a date: "))
            dateTwo = int(input("Select a second date: "))

            if dateTwo < dateOne:
                print("Second date must be more recent than the first, e.g. 1930-1940")
                datesInvalid = True
            
            if (dateOne >= 1874) and (dateTwo <= 2019):
                datesInvalid = False
                
            
            else:
                datesInvalid = True 
                print("Selected dates must be between 1874 and 2019")

        if datesInvalid == False:
            cvcGraph(year, country, dateOne, dateTwo)

##IS LOADING MENU OPTION AFTER SELECTING YEARs


def cvcGraph(year, country, dateOne, dateTwo):
    
    countryYear = []
    countryList = []
    countryCount = []
    countCont = []
    countriesFound = False
    selectedCountries = menuOption(year, country)

    while (countriesFound == False):
        for j in range(len(country)):
            countryList = str(country[j]).split(", ")
            print(country[j])

            for y in range(len(countryList)):
                if str(countryList[y]) == selectedCountries:
                    countriesFound = True
                    if len(countryYear) !=0:
                        if year[j] in countryYear:
                            print("test 1")

                            for i in range(len(countryCount)):
                                if str(countryList[i]) == str(country[j]):
                                    countCont[i] = int(countCont[i]) + 1
                                    print("test 2")
                        else:
                            countryYear.append(year[j])
                            countCont.apped(int(1))

                    else:
                            countryYear.append(year[j])
                            countCont.apped(int(1)) 

        if (countriesFound) == True:
         countCont.sort()
         print("Loading graph please wait...")
         print(countCont)
            

        


