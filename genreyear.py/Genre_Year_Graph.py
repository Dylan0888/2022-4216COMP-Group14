from dateutil.parser import parse 

# Import Data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
df = pd.read_excel(r"C:\Users\bradl\Downloads\coursework\movies.xlsx", 'movies_initial')

# Prepare data
 
x = df['year']
y = df['NoOfMovies']
years = df['year'].unique()
NoOfMovies = df['NoOfMovies'].unique()

# Draw Plot
mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey', 'tab:pink', 'tab:olive', 'deeppink', 'steelblue', 'firebrick', 'mediumseagreen']      
plt.figure(figsize=(16,10), dpi= 80)

for i, y in enumerate(years):
    plt.plot('month', 'year', data=df.loc[df.year==y, :], color=mycolors[i], label=y)
    plt.text(df.loc[df.year==y, :].shape[0]-.9, df.loc[df.year==y, 'year'][-1:].values[0], y, fontsize=12, color=mycolors[i])

# Decoration
plt.ylim(50,750)
plt.xlim(-0.3, 11)
plt.ylabel('$ Number of movies $')
plt.xlabel('$Year$')
plt.yticks(fontsize=12, alpha=.7)
plt.title("Movie genre vs year of release (1874 - 2016)", fontsize=22)
plt.grid(axis='y', alpha=.3)

# Remove borders
plt.gca().spines["top"].set_alpha(0.0)    
plt.gca().spines["bottom"].set_alpha(0.5)
plt.gca().spines["right"].set_alpha(0.0)    
plt.gca().spines["left"].set_alpha(0.5)   
# plt.legend(loc='upper right', ncol=2, fontsize=12)
plt.show()