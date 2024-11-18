import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

x = sns.get_dataset_names()
# print(x)
# x = sns.load_dataset("penguins")
# print(x)

# y= x["sex"].value_counts().plot(kind='bar')
# plt.show()
# z = x[(x["sex"] == 'Female') & (x["island"] == "Biscoe")].value_counts().plot(kind='bar')
# plt.show()
penguins = sns.load_dataset("penguins")
print(sns.get_dataset_names())
sns.boxplot(x="sex",y="body_mass_g",data="z")
plt.yticks(np.linspace(2500,7000,20))
plt.show()
sns.boxplot(x="species",y="body_mass_g",data="penguins")
plt.yticks(np.linspace(2500,7000,20))
plt.show()

sns.boxplot(x="island",y="body_mass_g",data="penguins")