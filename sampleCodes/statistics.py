# E lesson
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
# data via a csv file
smartphones=pd.read_csv("D://smartphones.txt")
# my_array=np.array([["galaxys8","andriod64",64,4,1490,'samsung',5.8],["galaxyA50","andriod64",128,4,1400,'google',5.8],["A&","andriod64",256,4,1490,'kia',5.8],["nokia","andriod64",32,10,1560,'samsung',6]])
# smartphones=pd.DataFrame(my_array,index=['0','1','2','3'],columns=['Name','OS','Capacity','RAM','Weight','Company','Inch'])
# show the count of each Ram
print(smartphones.Ram.value_counts())
count=smartphones.Ram.value_counts()
# see different category of Ram
category=count.index
print(category)
# Bar Plot in bar plot on the x we have different category of our value for different category and their value use bar plots
plt.bar(category,count)
# title of x
plt.xlabel("Ram")
# title of y
plt.ylabel("Ram")
plt.xticks([1,2,3,4])
plt.xticks([1,2,3])
plt.show()
# ECDF توزیع تجمعی داده ها را نمایش می دهد    داده ها به چه صورت توزیع شده اند
def ECDF(data):
    n=len(data)
    x=np.sort(data)
    # if the count of data is n,divide them into n help the number be between  0 to n
    y=np.arange(1,n+1)/n
    return x,y,n
x,y,n=ECDF(smartphones.inch)
# x is the sorted data in inch column
print(smartphones.inch)
print(x)
print(n)
print(y)
#  for draw a ECDF we use of scatter   s for the size of point
plt.figure(figsize=(11,8))
plt.scatter(x,y,s=80)
plt.margins(0.05)
plt.xlabel('inch',fontsize=15)
plt.ylabel('ECDF',fontsize=15)
plt.show()
#  mean of data میانه
np.mean(smartphones.inch)
# median میانگین
np.median(smartphones.inch)
# # برای نمایش Q1 , Q2 , Q3
np.percentile(smartphones.inch,[25,50,75])
print(np.percentile(smartphones.inch,[25,50,75]))
# variance and standard deviation   دادها چقدر در اطراف میانگین پراکنده شده اند  باید فاصله هر داده را با مقدار میانگین محاسبه و به توان دو می سونیم و تقسیم به تعداد دادها
# standard deviation   اانجراف معیار می شود جدر واریانس
# variance
# np.var(smartphones.Ram)
print(np.var(smartphones.Ram))
# مسانگسنaverage
np.mean(smartphones.Ram)
# # انجراف معیار که جدر واریانس هست
np.std(smartphones.Ram)
# # calculate variance in a handy way --> (value - average of whole numbers) **2 --> average of ((value - average of whole numbers) **2)
diff=smartphones.Ram-(np.mean(smartphones.Ram))
diff_sq=diff**2
var=np.mean(diff_sq)
print(var)
# covariance  for finding the changes of two values compared to each other -->
#  how to calculate covariance --> find the differences of each data with average number and multiple with each other then divide them into n (the total number)
# (x-xm)(y-ym)/n      relation between two parameter of x and y     if co is + they have direct relation and if it is - the are opposit
np.cov(smartphones.inch,smartphones.Weight)
print(np.cov(smartphones.inch,smartphones.Weight))