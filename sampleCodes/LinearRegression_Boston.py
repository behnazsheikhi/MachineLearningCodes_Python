# lesson H
# boston is a dataset of house price and their features
from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# create object of boston dataset
boston=load_boston()
# we want to create a dataFrame --> first gibe data then choose the name of columns
boston_df=pd.DataFrame(boston.data,columns=boston.feature_names)
# add another index to the dataFrame
boston_df['price']=boston.target
print(boston_df)
# print(boston.DESC())
x=boston.data
# print('x',x)
y=boston.target
# print('y',y)
#,
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
reg=LinearRegression()
reg.fit(x_train,y_train)
y_pre=reg.predict(x_test)
#  we want to know how real price (y_test) and predict price (y_train) are close or for from each other
plt.scatter(y_test,y_pre)
plt.xlabel("price")
plt.ylabel("predictedprice")
# plt.show()
# MSE
#  to find how it is accurate or not we can use Mean Square Error method (MSE) : to evaluating the model
#  میانگین تفاوت مقادیر واقعی و پیش بینی شده را حساب میکنیم
# import sklearn.metrics as m
# mse=m.mean_square_error(y_test,y_pre )
# or
# from sklearn.metrics import mean_square_error
# mse=mean_square_error(y_test,y_pre)
import sklearn.metrics as metrics
mse=metrics.mean_squared_error(y_test,y_pre)
print(mse)
# اگر از مقدار mse جذر بگیریم مقدار rmse بدست می آیدو هر چقدر به صفر نزدیکتر باشد بهتر است
# هر چه تعداد feature ها بیشتر باشد تخمین هزینه ها دقیق تر است
new_x= boston.data[:,[1,2]]
new_y=boston.target
new_x_trian,new_x_test,new_y_trian,new_y_test=train_test_split(new_x,new_y,test_size=0.3,random_state=42)
new_reg=LinearRegression()
new_reg.fit(new_x_trian,new_y_trian)
new_y_pre=new_reg.predict(new_x_test)
new_mse=metrics.mean_squared_error(new_y_test,new_y_pre)
print(new_mse)
