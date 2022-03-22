#Genre Year
#Comparison of movie genres to year. By Bradley Brian


#imports 

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
#data = pd.read_csv('movies_initial.csv')

#Functions 

def genreselect():
    print('------Please Select a genre------')
print("")
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
print("[11] Film Noir")
print("[12] History")
print("[13] Horror")
print("[14] Musical")
print("[15] Mystery")
print("[16] Romance")
print("[17] Science fiction")
print("[18] Sport")
print("[19] Thriller")
print("[20] War")
print("[21] Western")

genreselect()
option = int(input("Enter the number of your genre choice: "))
print("")


if option == 1:
            print("Action")
            print('there are [5285] movies in this genre')
            print('The year with the most action movies is')
            #this is where code to calculate most popular year is going to be 
elif option == 2:
            print("Adventure")
            print('there are [] movies in this genre')
            print('The year with the most Adventure movies is')
elif option == 3:
            print("Animation")
            print('there are [] movies in this genre')
            print('The year with the most Animation movies is')
elif option == 4:
            print("Biography")
            print('there are [] movies in this genre')
            print('The year with the most Biography movies is')   
elif option == 5:
            print("Comdey")
            print('there are [] movies in this genre')
            print('The year with the most Comedy movies is')
elif option == 6:
            print("Crime")
            print('there are [] movies in this genre')
            print('The year with the most Crime movies is')
elif option == 7:
            print("Documentary")
            print('there are [] movies in this genre')
            print('The year with the most Documentary movies is') 
elif option == 8:
            print("Drama")
            print('there are [] movies in this genre')
            print('The year with the most Drama movies is')
elif option == 9:
            print("Family")
            print('there are [] movies in this genre')
            print('The year with the most Family movies is')
elif option == 10:
            print("Fantasy") 
            print('there are [] movies in this genre')
            print('The year with the most Fantasy movies is')
elif option == 11:
            print("Film Noir")
            print('there are [] movies in this genre')
            print('The year with the most Film Noir movies is')
elif option == 12:
            print("History")
            print('there are [] movies in this genre')
            print('The year with the most History movies is')
elif option == 13:
            print("Horror")   
            print('there are [] movies in this genre')
            print('The year with the most Horror movies is')
elif option == 14:
            print("Musical")
            print('there are [] movies in this genre')
            print('The year with the most Musical movies is')
elif option == 15:
            print("Mystery")
            print('there are [] movies in this genre')
            print('The year with the most Mystery movies is')
elif option == 16:
            print("Romance") 
            print('there are [] movies in this genre')
            print('The year with the most Romance movies is')
elif option == 17:
            print("Science fiction")
            print('there are [] movies in this genre')
            print('The year with the most Science Fiction movies is')
    