import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score

#task A
data = pd.read_csv("LV4/data_C02_emission.csv")
print(data.info())

features = [
    "Engine Size (L)",
    "Cylinders",
    "Fuel Consumption City (L/100km)",
    "Fuel Consumption Hwy (L/100km)",
    "Fuel Consumption Comb (L/100km)",
    "Fuel Consumption Comb (mpg)"
]

X = data[features]
Y = data["CO2 Emissions (g/km)"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state=1)

#task B
plt.figure()
plt.scatter(X_train["Engine Size (L)"], Y_train, marker=".", color="blue", label="train")
plt.scatter(X_test["Engine Size (L)"], Y_test, marker=".", color="red", label="test")
plt.legend()
plt.show()

#test C
sc = StandardScaler()
X_train_n = sc.fit_transform(X_train)
X_train_n = pd.DataFrame(X_train_n, columns= X_train.columns) #making X_train_n a DataFrame

X_test_n = sc.transform(X_test)
X_test_n = pd.DataFrame(X_test_n, columns=X_test.columns)

plt.figure()
plt.hist(X_train["Engine Size (L)"], alpha=0.5, label="before scaling")
plt.hist(X_train_n["Engine Size (L)"], alpha=0.5, label="after scaling")
plt.legend()
plt.show()

#task D

linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, Y_train)
print("Koeficijenti:",linearModel.coef_)
print("Slobodan član:",linearModel.intercept_)

#task E
Y_predicted = linearModel.predict(X_test_n)

plt.figure()
plt.scatter(Y_test, Y_predicted, marker=".", color="blue")
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color="green")
plt.xlabel("Real Values")
plt.ylabel("Predicted Values")
plt.show()

#task F
MAE = mean_absolute_error(Y_test, Y_predicted)
MSE = mean_squared_error(Y_test, Y_predicted)
RMSE = root_mean_squared_error(Y_test, Y_predicted)
R2 = r2_score(Y_test, Y_predicted)
print("MAE:", MAE)
print("MSE:", MSE)
print("RMSE:", RMSE)
print("R2:", R2)
