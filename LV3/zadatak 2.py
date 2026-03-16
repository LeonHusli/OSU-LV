import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("LV3/data_C02_emission.csv")

print("\nBroj mjerenja:", len(data))
print(data.info())

print("\nNepuna mjerenja:")
print(data.isnull().sum())
data = data.dropna()

print("\nDupla mjerenja:")
print(data.duplicated().sum())
data = data.drop_duplicates()

data = data.reset_index(drop= True)

for col in data.select_dtypes(include="object").columns:
    data[col] = data[col].astype("category")
print(data.info())

#task A
plt.figure()
data["CO2 Emissions (g/km)"].plot(kind="hist", grid=True)
plt.show()

#task B
fuelType = data["Fuel Type"].unique()
print(fuelType)
colors = ["red", "green", "blue", "purple"]
colormap = dict(zip(fuelType, colors))

for fuel in fuelType:
    temp = data[data["Fuel Type"] == fuel]
    plt.scatter(
        temp["Fuel Consumption City (L/100km)"],
        temp["CO2 Emissions (g/km)"],
        color = colormap[fuel],
        label = fuel,
        marker="."
    )

plt.xlabel("Fuel Consumption City (L/100km)")
plt.ylabel("CO2 Emissions (g/km)")
plt.legend()
plt.show()

#task C
temp = [data[data["Fuel Type"] == fuel]["Fuel Consumption Hwy (L/100km)"] for fuel in fuelType]
plt.boxplot(temp, label= fuelType)
plt.xlabel("Fuel Type")
plt.xticks([1,2,3,4], labels=fuelType)
plt.ylabel("Fuel Consumption Hwy (L/100km)")
plt.show()

#task D
temp = data.groupby("Fuel Type").size()
plt.figure()
temp.plot(kind="bar")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Vehicles")
plt.show()

#task E
temp = data.groupby("Cylinders")["CO2 Emissions (g/km)"].mean()
plt.figure()
temp.plot(kind="bar")
plt.xlabel("Cylinders")
plt.ylabel("CO2 Emissions (g/km)")
plt.show()