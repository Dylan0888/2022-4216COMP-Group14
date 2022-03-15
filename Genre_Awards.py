#imports
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

#Genre menu options
def genreMenu():
    print("-------( Select a genre )-----------")
    print("[1] Action")
    print("[2] Adventure")
    print("[3] Animation")
    print("[4] Biography")
    print("[5] Comdey")
    print("[6] Crime")
    print("[7] Documentary")
    print("[8] Drama")
    print("[9] Family")
    print("[10] Fantasy")
    print("[11] Film-Noir")
    print("[12] History")
    print("[13] Horror")
    print("[14] Music/Musical")
    print("[15] Mystery")
    print("[16] Romance")
    print("[17] Sci-fi")
    print("[18] Sport")
    print("[19] Thriller")
    print("[20] War")
    print("[21] Western")
    print("[0] Exit")

#Asking user for input
genreMenu()
option = int(input("Enter genre choice: "))

while option != 0:
    if option == 1:
        #Action stuff goes here
        
        x = ['1990', '1991', '1992', '1993', '1993', '1994', '1995']
        awards = 0, 1, 2, 3, 4, 5, 6

        x_pos = [i for i, _ in enumerate(x)]

        plt.bar(x_pos, awards, colour = 'green')
        plt.xlabel("Year")
        plt.ylabel("No. of Awards")
        plt.title("No. of Awards for Action 1990-1995")
        
        plt.xticts(x_pos, x)
        plt.show()

        print("Action Genre")
    elif option == 2:
        #Adventure stuff goes here
        print("Adventure genre")
    elif option == 3:
        #Animation stuff goes here
        print("Animation genre")
    elif option == 4:
        #Biography stuff goes here
        print("Biography genre")   
    elif option == 5:
        #Comdey stuff goes here
        print("Comdey genre")
    elif option == 6:
        #Crime stuff goes here
        print("Crime genre")
    elif option == 7:
        #Documentary stuff goes here
        print("Documentary genre") 
    elif option == 8:
        #Drama stuff goes here
        print("Drama genre")
    elif option == 9:
        #Family stuff goes here
        print("Family genre")
    elif option == 10:
        #Fantasy stuff goes here
        print("Fantasy genre") 
    elif option == 11:
        #Film-Noir stuff goes here
        print("Film-Noir genre")
    elif option == 12:
        #History stuff goes here
        print("History genre")
    elif option == 13:
        #Horror stuff goes here
        print("Horror genre")   
    elif option == 14:
        #Music/Musical stuff goes here
        print("Music/Musical genre")
    elif option == 15:
        #Mystery stuff goes here
        print("Mystery genre")
    elif option == 16:
        #Romance stuff goes here
        print("Romance genre") 
    elif option == 17:
        #Sci-fi stuff goes here
        print("Sci-fi genre")
    elif option == 18:
        #Sport stuff goes here
        print("Sport genre")
    elif option == 19:
        #Thriller stuff goes here
        print("Thriller genre") 
    elif option == 20:
        #War stuff goes here
        print("War genre")
    elif option == 21:
        #Western stuff goes here
        print("Western genre") 
    else:
        print("Invalid option")    

    print()
    genreMenu()  
    option = int(input("Enter genre choice: ")) 
