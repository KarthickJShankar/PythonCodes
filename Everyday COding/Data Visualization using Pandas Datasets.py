import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option("display.max_columns",100)
# df = sns.load_dataset("iris")
# print(df)
# df.head(10).plot(kind="bar")
# plt.show()

# df.groupby("species")["petal_length"].median().plot(kind="bar",color="red")
# df["species"].value_counts().plot(kind="pie",autopct='%1.1f%%')
# plt.show()

df = sns.load_dataset("taxis")
df["weekday"] = df["pickup"].dt.day_name()
# df.groupby("weekday")["total"].sum().plot(kind="pie",autopct="%1.1f%%")
# plt.show()
df.groupby(["weekday","pickup_borough"])["total"].sum().sort_values(ascending=False).plot(kind="bar",color="red")
plt.show()