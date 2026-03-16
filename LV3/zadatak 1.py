import pandas as pd
import numpy as np

data = pd.read_csv("LV3/data_C02_emission.csv")

#task A
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


#task B
print("\nAutomobili sa najvecom potrošnjom goriva u gradu:")
print(data.nlargest(3,"Fuel Consumption City (L/100km)")[["Make", "Model", "Fuel Consumption City (L/100km)"]])

print("\nAutomobili sa najmanjom potrošnjom goriva u gradu:")
print(data.nsmallest(3,"Fuel Consumption City (L/100km)")[["Make", "Model", "Fuel Consumption City (L/100km)"]])

#task C
specific_engine_size = data[(data["Engine Size (L)"] >= 2.5) & (data["Engine Size (L)"] <= 3.5)]
print("\nVozila sa veličinom motora između 2.5L i 3.5L:", len(specific_engine_size))
print("\nProsječna CO2 emisija:", round(specific_engine_size["CO2 Emissions (g/km)"].mean(), 2))

#task D
print("\nBroj Audi mjerenja:")
print(data.groupby("Make").size()["Audi"])
print("\nProsječna C02 emisija Audi vozila:")
print(round(data[data["Cylinders"] == 4].groupby("Make")["CO2 Emissions (g/km)"].mean()["Audi"], 2))

#task E
print("\nBroj vozila prema broju cilindara:")
print(data.groupby("Cylinders").size())
print("\nProsječna CO2 potrošnja prema broju cilindara:")
print(round(data.groupby("Cylinders")["CO2 Emissions (g/km)"].mean(), 2))

#task F
print("\nProsječna gradska potrošnja za dizel i benzin:")
print(round(data.groupby("Fuel Type")["Fuel Consumption City (L/100km)"].mean()[["X", "D"]], 2))
print("\nMedijan:")
print(data.groupby("Fuel Type")["Fuel Consumption City (L/100km)"].median()[["X", "D"]])


#task G
print("\nVozilo sa 4 cilinda i dizelskim motorom sa najvećom gradskom potrošnjom:")
print(data[(data["Cylinders"] == 4) & (data["Fuel Type"] == "D")].nlargest(1, "Fuel Consumption City (L/100km)"))

#task H
print("\nBroj vozila sa ručnim mjenjačem:")
print(data.groupby("Transmission").size()[["M5", "M6", "M7"]].sum())

#task I
print("\nKorelacija:")
print(data.corr(numeric_only=True))

