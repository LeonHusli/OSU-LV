import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(r"LV2\data.csv", delimiter=",", skiprows=1) #we skip 1st row as it is a header row
print("Number of tested people: ", len(data))

height = data[:,1]
mass = data[:,2]

every50height = height[::50]
every50mass = mass[::50]

maleHeight = [row[1] for row in data if row[0] == 1.0]
femaleHeight = [row[1] for row in data if row[0] == 0.0]

print("Minimum height: ", min(height))
print("Maximum height: ", max(height))
print("Average height: ", round(sum(height)/len(height), 2))

print("Minimum male height: ", min(maleHeight))
print("Maximum male height: ", max(maleHeight))
print("Average male height: ", round(sum(maleHeight)/len(maleHeight), 2))

print("Minimum female height: ", min(femaleHeight))
print("Maximum female height: ", max(femaleHeight))
print("Average female height: ", round(sum(femaleHeight)/len(femaleHeight), 2))

plt.scatter(height, mass, marker=".")
plt.scatter(every50height, every50mass, marker=".")
plt.xlabel("Height(cm)")
plt.ylabel("Mass(kg)")
plt.show()