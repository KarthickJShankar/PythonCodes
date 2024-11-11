import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
#
# x = np.linspace(0,10, 100)
# print(x)
# y = np.sin(x)
# print(y)
# z= np.cos(x)
# a = np.tan(x)
#
#
# sns.set(style="darkgrid")
# plt.figure(figsize=(12, 6))
# plt.plot(x, y, color='black', linewidth=2)
# plt.plot(x, z, color='green', linewidth=2)
# plt.plot(x, a, color='blue', linewidth=2)
# plt.scatter(x,y,s=100,color="red",label="Sin")
# plt.scatter(x,z,s=100,color="green",label="Cos")
# plt.scatter(x,a,s=100,color="blue",label="Tan")
#
# plt.title('Sine Curve with Highlighted sin(30°)',size=22,color="red")
# plt.xlabel('Theta (In Radiance)',size=20)
# plt.legend(loc="best")
# plt.ylim(-2,2)
# plt.show()

plt.figure(figsize=(15, 6))
s = ["a","b","c"]
y=[100,150,330]
sns.set(style="darkgrid")
plt.bar(s, y, color='black', linewidth=2)
plt.plot(s,y, color='green', linewidth=2)

plt.title('AQI Analysis',size=22,color="red")
plt.xlabel('States',size=20)
plt.ylabel('AQI',size=20)
plt.legend(loc="best")
plt.show()