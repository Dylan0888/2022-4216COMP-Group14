#imports
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

#Genre menu options
def genreMenu(year, genre, awards):
    
    genreSelected = False

    while (genreSelected == False):
        userChoice = input("""

        ------- Select a genre -----------
        [1] Action
        [2] Adult
        [3] Adventure
        [4] Animation
        [5] Biography
        [6] Comedy
        [7] Crime
        [8] Documentary
        [9] Drama
        [10] Family
        [11] Fantasy
        [12] Film-Noir
        [13] History
        [14] Horror
        [15] Music/Musical 
        [16] Mystery 
        [17] Romance 
        [18] Sci-fi 
        [19] Sport
        [20] Thriller
        [21] War
        [22] Western
        [0] Exit
        
        --Please select a genre--
            """)

        if userChoice == "1":
            genreSelected = True
            choice = "Action"
            print("Action genre selected")

        elif userChoice == "2":
            genreSelected = True
            choice = "Adult"
            print("Adult genre selected")

        elif userChoice == "3":
            genreSelected = True
            choice = "Adventure"
            print("Adventure genre selected") 

        elif userChoice == "4":
            genreSelected = True
            choice = "Animation"
            print("Animation genre selected")

        elif userChoice == "5":
            genreSelected = True
            choice = "Biography"
            print("Biograpghy genre selected")

        elif userChoice == "6":
            genreSelected = True
            choice = "Comedy"
            print("Comedy genre selected")

        elif userChoice == "7":
            genreSelected = True
            choice = "Crime"
            print("Crime genre selected")

        elif userChoice == "8":
            genreSelected = True
            choice = "Documentary"
            print("Documentary genre selected")

        elif userChoice == "9":
            genreSelected = True
            choice = "Drama"
            print("Drama genre selected")  

        elif userChoice == "10":
            genreSelected = True
            choice = "Family"
            print("Family genre selected")  

        elif userChoice == "11":
            genreSelected = True
            choice = "Fantasy"
            print("Fantasy genre selected")

        elif userChoice == "12":
            genreSelected = True
            choice = "Film-noir"
            print("Film-Noir genre selected")

        elif userChoice == "13":
            genreSelected = True
            choice = "History"
            print("History genre selected") 

        elif userChoice == "14":
            genreSelected = True
            choice = "Horror"
            print("Horror genre selected")

        elif userChoice == "15":
            genreSelected = True
            choice = "Music/Musical"
            print("Music/Musical genre selected")

        elif userChoice == "16":
            genreSelected = True
            choice = "Mystery"
            print("Mystery genre selected")

        elif userChoice == "17":
            genreSelected = True
            choice = "Romance"
            print("Romance genre selected")

        elif userChoice == "18":
            genreSelected = True
            choice = "Sci-fi"
            print("Sci-Fi genre selected")  

        elif userChoice == "19":
            genreSelected = True
            choice = "Sport"
            print("Sport genre selected")   

        elif userChoice == "20":
            genreSelected = True
            choice = "Thriller"
            print("Thriller genre selected")

        elif userChoice == "21":
            genreSelected = True
            choice = "War"
            print("War genre selected")   

        elif userChoice == "22":
            genreSelected = True
            choice = "Western"
            print("Western genre selected") 
                

        else:
            print("Invalid input, use numbers 1 - 22")  
    
    return choice 

def createGraph(year, genre, awards):
    print("test 1") 

    genreYear = []
    findGenre = []
    genreList = []
    getAwards = []
    genreFound = False
    awardSplit = []
    awardSplitter = []
    getAwardNum = []
    
    chosenGenre = genreMenu(year, genre, awards)
    for j in range(len(genre)):
        #print(genre[j])
        genreList = str(genre[j]).split(", ")
        #print()
        #print("test")
        for y in range(len(genreList)):
            #print(chosenGenre, genreList[k])
            if str(chosenGenre) == str(genreList[y]):
                #print("test2")
                awardSplit = str(awards).split("\t")
                #print(awardSplit)
                for i in range(len(awardSplit)):
                    #print(awardSplit[i])
                    if "win." in (awardSplit[i]):
                        awardSplitter = awardSplit[i].split(" win.")
                        #print(awardSplitter)
                        getAwardNum.append(awardSplitter[0])
                        getAwards.append(year[j])
                    else:
                        getAwardNum.append("0")
    

    print(getAwards, getAwardNum)
    #print(genre)
    
    
   # while (genreFound == False):
  #      for i in range (len(genre)):
 #           genreList = str(genre[i]).split(", ")
#
       #     for j in range(len(genreList)):
      #          if genreList[j] == str(chosenGenre):
     #               genreFound == True
    #                print(genreFound)

         
            #print("test 2")
            #print(genreList[1])
        #
            #print("put it in daddy")
            #substring = chosenGenre
           # print(chosenGenre)
           # print(genreList[j])
            #print(genreList[j])
           # if substring in genreList[j]:
            #    print("here")
            #    print(genreFound)
            #    if len(genreYear) !=0:
             #       if year[i] in genreYear:
             #           for k in range(50):
             #               if "\k wins" in awards:
              #                  getAwards.append(k)
              #      else:
              #         genreYear.append(year[i])
             #           getAwards.append(awards[i])
             #   else: 
              #      genreYear.append(year[i])
            #        findGenre.append(int(1))
          #  else:
           #     print("kill me")        
    print("The years this genre has had movies made:")
    getAwards.sort()
    
    #print(genreYear, "and" , findGenre) 
    #print(getAwards, "\n")
    print("Loading grapgh...")
    fig, ax = plt.subplots()
    #ax.plot(getAwardNum, 'go--', label="Movies") 
    fig.suptitle("Awards per Genre", fontsize=18)
    ax.set_title("Genre: "+ chosenGenre, fontsize=14)
    ax.set_xlabel("Years", fontsize=12)
    ax.set_ylabel("Amount of movies", fontsize=12, color='g')
    ax.plot(getAwards, 'ro--', label="Awards") 
    ax.set_yticks(range(1, 11, 1))
    rangeYear = int(max(getAwards))-int(min(getAwards))
    plt.xlim(getAwards, getAwardNum)
    ax.legend()
    ax.grid(True)
    ax.grid(False)
    plt.show()

