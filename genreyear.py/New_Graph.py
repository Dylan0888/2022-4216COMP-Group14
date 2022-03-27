#graph
from dateutil.parser import parse 

# Import Data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
df = pd.read_excel(r"C:\Users\bradl\Downloads\coursework\movies.xlsx", 'movies_initial')

x = list(['year'])
y = list(['genre'])


plt.ylabel('$ Number of movies $')
plt.xlabel('$Year$')
plt.yticks(fontsize=12, alpha=.7)
plt.grid(axis='y', alpha=.3)
plt.ylim(100,5000)
plt.xlim(1887, 2016)



plt.figure(figsize=(10,10))
plt.style.use('fivethirtyeight')
plt.title("Movie genre vs year of release (1874 - 2016)", fontsize=18)

plt.gca().spines["top"].set_alpha(0.0)    
plt.gca().spines["bottom"].set_alpha(0.5)
plt.gca().spines["right"].set_alpha(0.0)    
plt.gca().spines["left"].set_alpha(0.5)   
# plt.legend(loc='upper right', ncol=2, fontsize=12)
plt.show()