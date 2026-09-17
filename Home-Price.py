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

# matplotlib
plt.scatter(df["area"], df["price"],  color='blue')
plt.plot(train_x, model.coef_[0][0]*train_x + model.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()