# lesson H
# regression is the gategory of supervise learning and it means the target valyes are not کسسته but they are پیوسته and
# it divides into two catehory
# 1.Linear Regression in the kind of regression we try to fit a line into our data y=ax+b ,y-->target ,x--> the only feature ,a-->modal parameter ,b-->parameter
#  and b and b are the parameter to draw best line and use then to describe and predict properly
# we can use Error Function to estimate the optimal line
# فاصله ی عموپی هر داده تا خطی که درنظرگرفته شده است را محاسبه می کنیمکه به آن residual گفته می شود در واقع هر داده سعی میکنهکه این فاصله را کتر کمتر کنه
# وقتی میخایم این ها را جمع کنیم داده هایی که بالای خط قرار گرفتن مثبت هستن و داده های پایین خط منفی عملاْ یکدیگر را خنثی میکنند پس از توان دوم آنها استفاده میکنیم
# ordinary least squares(OLS): minimize sum of square residuals to building the model ---> it is error function
# Linear regression for higher dimentions   = ax+ax+b
# when our dataset has n feature we must identify n ضریب and one constnt to fit to linear regression
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
# create points with scatter
x=np.arange(1,10)
y=np.array([28,25,26,31,32,29,30,35,36])
plt.scatter(x,y)
# plt.show()
# for draw a line we must enter x,y into linear regression methods which are similar to dataset
#  each sample is on the row and each column is a mesuable feature
# داده ها را به شکل ستونی دربیاریم
x=x.reshape(-1,1)
y=y.reshape(-1,1)
# print(x)
# print(y)
# create model --->linear model    2. fit data into model   3. want machine to predict new data
reg=LinearRegression()
reg.fit(x,y)
print(reg)
yhat=reg.predict(x)
#  کشیدن نفطه هاداده ها
plt.scatter(x,y)
#  کشیدن linear براساس پیش بینی
plt.plot(x,yhat)
plt.show()
