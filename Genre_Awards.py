#imports
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

#Genre menu options
def genreMenu():
    print("-------( Select a genre )-----------")
    print("[1] Action")
    print("[2] Adult")
    print("[3] Adventure")
    print("[4] Animation")
    print("[5] Biography")
    print("[6] Comedy")
    print("[7] Crime")
    print("[8] Documentary")
    print("[9] Drama")
    print("[10] Family")
    print("[11] Fantasy")
    print("[12] Film-Noir")
    print("[13] History")
    print("[14] Horror")
    print("[15] Music/Musical")
    print("[16] Mystery")
    print("[17] Romance")
    print("[18] Sci-fi")
    print("[19] Sport")
    print("[20] Thriller")
    print("[21] War")
    print("[22] Western")
    print("[0] Exit")

#Asking user for input
    option = int(input("Enter genre choice: ")) 

    while option != 0:
        if option == 1:
            #Action stuff goes here


            print("Action Genre")
            return 'Action'

        elif option == 2:
            #Adventure stuff goes here
            print("Adult genre")
            return 'Adult'

        elif option == 3:
            #Adventure stuff goes here
            print("Adventure genre")
            return 'Adventure'

        elif option == 4:
            #Animation stuff goes here
            print("Animation genre")
            return 'Animation'

        elif option == 5:
            #Biography stuff goes here
            print("Biography genre")  
            return 'Biography'

        elif option == 6:
            #Comdey stuff goes here
            print("Comedy genre")
            return 'Comedy'

        elif option == 7:
            #Crime stuff goes here
            print("Crime genre")
            return 'Crime'

        elif option == 8:
            #Documentary stuff goes here
            print("Documentary genre") 
            return 'Documentary'

        elif option == 9:
            #Drama stuff goes here
            print("Drama genre")
            return 'Drama'

        elif option == 10:
            #Family stuff goes here
            print("Family genre")
            return 'Family'

        elif option == 11:
            #Fantasy stuff goes here
            print("Fantasy genre") 
            return 'Fantasy'

        elif option == 12:
            #Film-Noir stuff goes here
            print("Film-Noir genre")
            return 'Film-Noir'

        elif option == 13:
            #History stuff goes here
            print("History genre")
            return 'History'

        elif option == 14:
            #Horror stuff goes here
            print("Horror genre")   
            return 'Horror'

        elif option == 15:
            #Music/Musical stuff goes here
            print("Music/Musical genre")
            return 'Music/Musical'

        elif option == 16:
            #Mystery stuff goes here
            print("Mystery genre")
            return 'Mystery'

        elif option == 17:
            #Romance stuff goes here
            print("Romance genre") 
            return 'Romance'

        elif option == 18:
            #Sci-fi stuff goes here
            print("Sci-fi genre")
            return 'Sci-fi'

        elif option == 19:
            #Sport stuff goes here
            print("Sport genre")
            return 'Sport'

        elif option == 20:
            #Thriller stuff goes here
            print("Thriller genre") 
            return 'Thriller'

        elif option == 21:
            #War stuff goes here
            print("War genre")
            return 'War'

        elif option == 22:
            #Western stuff goes here
            print("Western genre")
            return 'Western'

             
        else:
            print("Invalid option")    

            return 'null'



def createGraph(year, genre, awards):
    splitArray=[]


    chosenGenre = genreMenu()
    plt.title(chosenGenre)
    plt.xlim(1850, 2020)
    plt.ylim(0, 10)
    plt.xlabel('year')
    plt.ylabel('awards')
    print("yeet 1")
    for j in range (len(genre)): # validates to ensure genre = chosen genre by user
        if genre[j] == chosenGenre:
            for i in range (len(awards)): # checks if the movie has an award
                awardsString = str(awards[i])
               
                if awardsString.count("win") > 0 : 
                    print("found awards")
                    splitArray = awards[i].split(" ")
                
                    print(year[i], splitArray[0])

                    if splitArray[0] is int:
                        plt.plot(year[i], splitArray[0]) # plorts movie by year and awards
                

#if awards array contains "win" gonna split the string into an array and take postion 0
    
    plt.show()