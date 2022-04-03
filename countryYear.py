from unicodedata import numeric
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
        [2] All Countries, All Time
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
                                datesInvalid = True
                        if datesInvalid == False:
                            print("Loading graph, please wait")
                            createGraphOne(year, country, dateOne, dateTwo, countryOne, countryTwo)

                    elif(choiceTwo == "2"):
                        print("Loading graph, please wait")  
                        createGraphTwo(year, country, countryOne, countryTwo)

        elif userChoice == "2":
            choiceSelected = True
            print("Loading graph, please wait")
            createGraphThree(year, country)

        elif userChoice == "3":
            choiceSelected = True
            print("Exit selcted, returning to main menu")
            print("havent done this yet")
  
def createGraphOne(year, country, dateOne, dateTwo, countryOne, countryTwo):
    countCountryOne = 0  
    countCountryTwo = 0

    for i in range(len(country)): 
        countryList = str(country[i]).split(", ")
        if year[i].isnumeric():
            if (int(year[i]) > dateOne) and (int(year[i]) < dateTwo):
                for j in range(len(countryList)):
                    if countryOne == str(countryList[j]) :
                        countCountryOne+=1
                    if countryTwo == str(countryList[j]) :
                        countCountryTwo+=1
    

    labels = countryOne, countryTwo
    sizes = countCountryOne, countCountryTwo
    explode = (0.1,0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
    ax1.set_title(countryOne+  " vs " + countryTwo, fontsize=14)
    ax1.set_xlabel("Date: " + str(dateOne) + "-" + str(dateTwo), fontsize=12)
    plt.legend(sizes)
    plt.show()
    
def createGraphTwo(year, country, countryOne, countryTwo):
    countCountryOne = 0  
    countCountryTwo = 0

    for i in range(len(country)): 
        countryList = str(country[i]).split(", ")
        if year[i].isnumeric():
            if (int(year[i]) > 1874) and (int(year[i]) < 2019):
                for j in range(len(countryList)):
                    if countryOne == str(countryList[j]) :
                        countCountryOne+=1
                    if countryTwo == str(countryList[j]) :
                        countCountryTwo+=1
    
    labels = countryOne, countryTwo
    sizes = countCountryOne, countCountryTwo
    explode = (0.1,0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
    ax1.set_title(countryOne+  " vs " + countryTwo, fontsize=14)
    ax1.set_xlabel("Date: 1874 - 2019", fontsize=12)
    plt.legend(sizes)
    plt.show()

def createGraphThree(year, country):
    
    labels = countryList
    sizes = df
    explode = (0.1,0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode = None, labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
    ax1.set_title("All countries, All time", fontsize=14)
    ax1.set_xlabel("Date: 1874 - 2019", fontsize=12)
    plt.legend(sizes)
    plt.show()


   


    


    
            