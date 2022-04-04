#IMPORTS
from unicodedata import numeric
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

#FIRST MENU
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
        
        --Please select a option--
            """)

        if userChoice == "1":
            choiceSelected = True
            print("Country vs Country selected")

            #USER INPUT COUNTRIES
            while(choiceInput == False):
                countryOne = str(input("Select a country: "))
                countryTwo = str(input("Select a second country: "))

                #FINSING COUNTRIES IN DATASET FOR VALIDATION
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

                    #USER MENU FOR DATE CHOICE
                    choiceTwo = input("""
                     Would you like the data between two specific dates or all time?

                    [1] Two date
                    [2] All Time
        
                    --Please select a option--
                    """)
                    if (choiceTwo == "1"):
                        while (datesInvalid == True):

                            #USER INOUT FOR DATES WANTED
                            dateOne = int(input("Select the first date: "))
                            dateTwo = int(input("Select the second date: "))

                            #VALIDATION FOR DATES
                            if dateTwo < dateOne:
                                print("Second date must be more recent than the first, e.g. 1930-1940")
                                datesInvalid == True
                            if (dateOne >= 1874) and (dateTwo <= 2019):
                                datesInvalid = False
                            else: 
                                print("dates must be between 1874 and 2019, please try again")   
                                datesInvalid = True
                        if datesInvalid == False:
                            #LOADS GRAPH
                            print("Loading graph, please wait")
                            createGraphOne(year, country, dateOne, dateTwo, countryOne, countryTwo)

                    elif(choiceTwo == "2"):
                        #LOADS GRAPH
                        print("Loading graph, please wait")  
                        createGraphTwo(year, country, countryOne, countryTwo)

        elif userChoice == "2":
            choiceSelected = True
            #LOADS GRAPH 
            print("Loading graph, please wait")
            createGraphThree(country)

  
def createGraphOne(year, country, dateOne, dateTwo, countryOne, countryTwo):
    countCountryOne = 0  
    countCountryTwo = 0

    #FINDS COUNTRIES AND COUNTS BETWEEN YEARS
    for i in range(len(country)): 
        countryList = str(country[i]).split(", ")
        if year[i].isnumeric():
            if (int(year[i]) > dateOne) and (int(year[i]) < dateTwo):
                for j in range(len(countryList)):
                    if countryOne == str(countryList[j]) :
                        countCountryOne+=1
                    if countryTwo == str(countryList[j]) :
                        countCountryTwo+=1
    
    #GRAPH 
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

    #FINDS COUNTRIES AND COUNTS BETWEEN YEARS
    for i in range(len(country)): 
        countryList = str(country[i]).split(", ")
        if year[i].isnumeric():
            if (int(year[i]) > 1874) and (int(year[i]) < 2019):
                for j in range(len(countryList)):
                    if countryOne == str(countryList[j]) :
                        countCountryOne+=1
                    if countryTwo == str(countryList[j]) :
                        countCountryTwo+=1
    
    #GRAPH
    labels = countryOne, countryTwo
    sizes = countCountryOne, countCountryTwo
    explode = (0.1,0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
    ax1.set_title(countryOne+  " vs " + countryTwo, fontsize=14)
    ax1.set_xlabel("Date: 1874 - 2019", fontsize=12)
    plt.legend(sizes)
    plt.show()

def createGraphThree(country):
    #COUNTRIES LIST
    countries = ['USA', 'France', 'UK', 'Spain', 'Australia', 'Denmark', 'Russia', 'Italy', 'Sweden', 'Germany', 'Hungary', 'Soviet Union', 'Finland', 'Austria', 'Norway', 'Japan', 'Czechoslovakia', 'Netherlands', 'Portugal', 'Brazil', 'Canada', 'Mexico', 'nan', 'Switzerland', 'China', 'West Germany', 'India', 'East Germany', 'Egypt', 'Morocco', 'Poland', 'Romania', 'Greece', 'Hong Kong', 'Cuba', 'Ireland', 'Venezuela', 'Yugoslavia', 'Bulgaria', 'Philippines', 'Croatia', 'South Africa', 'Belgium', 'Argentina', 'Israel', 'Monaco', 'Algeria', 'Taiwan', 'Senegal', 'Bolivia', 'South Korea', 'Mauritania', 'Turkey', 'Liechtenstein', 'Iceland', 'Iran', 'Estonia', 'Luxembourg', 'Peru', 'Tunisia', 'Chile', 'Cameroon', 'Syria', 'Angola', 'Jamaica', 'Bangladesh', 'Panama', 'Ethiopia', 'Zimbabwe', 'Lebanon', 'Libya', 'Kuwait', "C�te d'Ivoire", 'New Zealand', 'Singapore', 'Botswana', 'Malta', 'Puerto Rico', 'Burkina Faso', 'Martinique', 'North Korea', 'Colombia', 'Albania', 'Palestine', 'Zaire', 'Mali', 'Ghana', 'Indonesia', 'Namibia', 'Vietnam', 'Papua New Guinea', 'Armenia', 'Kazakhstan', 'Uruguay', 'Federal Republic of Yugoslavia', 'Czech Republic', 'Slovenia', 'Guinea', 'Lithuania', 'Republic of Macedonia', 'Dominican Republic', 'Bosnia and Herzegovina', 'Slovakia', 'Georgia', 'Ukraine', 'Aruba', 'Cyprus', 'Tajikistan', 'Latvia', 'Kyrgyzstan', 'Uzbekistan', 'Pakistan', 'Bhutan', 'Faroe Islands', 'Nepal', 'Thailand', 'Malaysia', 'Haiti', 'Barbados', 'Gabon', 'Serbia', 'Jordan', 'Chad', 'Serbia and Montenegro', 'Kenya', 'United Arab Emirates', 'Afghanistan', 'Cambodia', 'Isle Of Man', 'Mongolia', 'Bahrain', 'Bahamas', 'Ecuador', 'Rwanda', 'Sri Lanka', 'Iraq', 'Paraguay', 'Costa Rica', 'Macao', 'Saudi Arabia', 'Qatar', 'Trinidad and Tobago', 'Liberia', 'Tanzania', 'El Salvador', 'Belarus', 'Nigeria', 'Guatemala', 'Grenada', 'The Democratic Republic Of Congo', 
'Moldova', 'American Samoa', 'Uganda', 'Samoa', 'Somalia', 'Bermuda', 'Madagascar', 'Laos', 'Micronesia', 'Montenegro', 'Honduras', 'Nicaragua', 'Greenland', 'Congo', 'Reunion', 'Korea', 'Brunei', 'Burma', 'Swaziland', 'Kosovo', 'Suriname', 'Vanuatu']
    countriesAwards = []
    
    x = Counter(country)
    for i in range(len(countries)):
        
        #PUTS COUNTRIES INTO ARRAY
        countriesAwards.append(x[countries[i]])

    #COUNTRIS FOR GRAPH DISPLAY
    countryLabels = (countries[0], countries[1], countries[2], countries[3], countries[4],countries[5], countries[6], countries[7], countries[8], countries[9], countries[10], countries[11], countries[12], countries[13], countries[14], 'OTHER')
    countrySizes = (countriesAwards[0], countriesAwards[1], countriesAwards[2], countriesAwards[3], countriesAwards[4],countriesAwards[5], countriesAwards[6], countriesAwards[7], countriesAwards[8], countriesAwards[9], countriesAwards[10], countriesAwards[11], countriesAwards[12], countriesAwards[13], countriesAwards[14], 16459)

    #GRAPH
    labels = list(countryLabels)
    sizes = list(countrySizes)
    explode = (0.1,0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode = None, labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
    ax1.set_title("All countries, All time", fontsize=14)
    ax1.set_xlabel("Date: 1874 - 2019", fontsize=12)
    plt.legend(sizes)
    plt.show()


   


    


    
            