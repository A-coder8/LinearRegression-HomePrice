# import a immportant librarys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score

# call a Linear Regression in Linear model
model = linear_model.LinearRegression()

# read a csv File
csv_file = pd.read_csv("~/myproject/machine Learing/Regression/house_price.csv")

# create a DataFrame
df = pd.DataFrame(csv_file)

# train and test split
train_test = np.random.rand(len(df)) < 0.8
train = df[train_test]
test = df[~train_test]
print(len(train.values))
print(len(test.values))

# create and train model
train_x = train[["area","room","age","floor","parking","elevator","warehouse","location_score"]]
train_y = train[["price"]]
model.fit(train_x, train_y)

# test model
test_x = test[["area","room","age","floor","parking","elevator","warehouse","location_score"]]
test_y = test[["price"]]
test_y_ = model.predict(test_x)

# R2 score
score = r2_score(test_y, test_y_)
print(score)

# test a model with your Data
len_n = len(["area","room","age","floor","parking","elevator","warehouse","location_score"])
prediction_array = np.array([[int(input(f"Enter a {df.columns[i]}:")) for i in range(8)]])
prediction = model.predict(prediction_array)
print("model answer is:", prediction[0][0])

# matplotlib
area_range = np.linspace(df["area"].min(), df["area"].max(), 100)

plot_data = pd.DataFrame({
    "area": area_range,
    "room": df["room"].mean(),
    "age": df["age"].mean(),
    "floor": df["floor"].mean(),
    "parking": df["parking"].mean(),
    "elevator": df["elevator"].mean(),
    "warehouse": df["warehouse"].mean(),
    "location_score": df["location_score"].mean()
})

predicted_price = model.predict(plot_data)

plt.scatter(df["area"], df["price"], color="blue", label="Real Data")
plt.plot(area_range, predicted_price, color="red", label="Prediction")

plt.xlabel("Area")
plt.ylabel("Price")
plt.title("House Price Prediction")
plt.legend()
plt.show()
