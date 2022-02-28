"""

Movies - Countries (between two years)
By Mackenzie Whitehead

Main Graph Idea: 
A heatmap of countries showing the amount of movies released per country in a certain time frame

Steps:
    - Asks lower limit year
    - Asks upper limit year
    - Generates Heatmap of movies per countries between the two given dates

"""

# Imports



# Global Variables



# Functions

def createGraph(movieTitle, country):
    print("[SUB-FILE] Successfully Passed Full Array into Sub File!")
    for i in range (len(movieTitle)):
        print(i, ": ", movieTitle[i], " - ", country[i])