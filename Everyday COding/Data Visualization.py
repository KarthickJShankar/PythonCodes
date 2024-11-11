import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#print(sns.get_dataset_names()) #To get system defined data sets.

# pd.set_option("display.max_columns",500) #once we run this line any data frame will show up to 500 columns withou hiding
# data = sns.load_dataset("taxis") #To load a data set
# print(data)

sns.set_style(("darkgrid"))
plt.figure(figsize=(10,6),facecolor="lightgreen",linewidth=2)
x = [1,2,3]
y=[12,23,25]

#ScatterPlot
plt.scatter(x,y,color="red",s=100)
plt.plot(x,y,linestyle="dotted")
plt.xlabel("supply",size=20)
plt.ylabel("Demand",size=20)
plt.title("Supple vs Demand",size=22)
plt.xticks(x)
plt.yticks(y)
plt.xlim(0,5)
plt.ylim(7,30)
for i,j in zip(x,y):
    plt.text(x=i,y=j+1,s=f"({i},{j})",color="red",size=12)
plt.savefig("../plot.png",dpi=300,)
plt.show()

