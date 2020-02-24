# F lesson
# preprocessing پیش پردازش اطلاعات
# اطلاعات را آماده میکنیم تا برای پردازش استفاده کنیمتا به استفاده از الگوریتم های ماشین لرنینگ از آنها استفاده می کنیم به مرحله آماده سازی داده ها preprocessing میگویند
# scikit learn       این پکیجی هست که الگوریتم های machine learning هم در آن قرار دارد
# simple and efficient tools data mining and data analysis
import numpy as np
import pandas as pd
# preprocessing is in scikit learn pachage(sklearn)
from sklearn import preprocessing
# Datasets         به مجموعه داده هایی که می خواهیم برای عملیات machine learning‌استفاده کنیم  dataset گفته می شود
# dataset ها با یک نظم مشخصی بوجود می آیند یعنی همیشه نمونه ها روی سطرهای آن و پارمترهایی که برای هر نمونه اندازه گیری شده روی ستون ها می آید.
# به نمونه ها sample - observation
#  یا بعد می گوییم به پارامترها feature
country=pd.read_csv('D://c_data.txt',encoding='ansi',header=0)
# rename the header
country=country.rename(columns={'CountryName':'Name','CountryCode':'Code','Populationgrowth':'pop_growth','Totalpopulation':'pop','Area':'Area'})
# inplace=True replace the old dataFrame with new one
country.drop('Code',axis=1,inplace=True)
# set name of the country to index
country.rename(index=country.Name,inplace=True)
country.drop("Name",axis=1,inplace=True)
print(country)
# the number of information
print(country.shape)
# give whole information about Dataset
print(country.info())
# give whole the statistic information about the data set such as mean میانگین, std انحراف معیار ,min کمترین مقدار ,
# ْْQ1,Q2 میانه ,Q3 and max    ---> describe method use for numeric value
print(country.describe())
max_pop=country['pop'].max()
#  را جدا کن حال از اون ستون اونی را جدا کن که مقدارش برابر با max_pop هست .ابتدا ستون country pop
print(country['pop'][country['pop']==max_pop])
# delete one value from row axis=0 means data is in the row
# country.drop('World',axis=0,inplace=True)
# Missing Value    Not a Number داده هایی مه عدد نیستن و نمی تواند برای تحلیل dataset مورد استفاده قرار بگیرن
print(country)
# machine consider values such ? or 0  a value because they are character so becareful about missing value
#  to find the null value   --> if there is value it shows False else: True
print(country.isnull())
# nan means misvalue and computer cam undestand sone of the value in dataset is null
country.replace('?',np.nan,inplace=True)
# delete the whole row or column of dataset that consists of nan(missing value) value  --> axis=0 or axis=1
country.dropna(axis=0)
# another approach is to fill the lissing value which is not a correct way because it will change other result
country.fillna(0)
# use a dictionary for each feature to fill them if they are nan
country.fillna({'pop_growth':0,'pop':10000,'Area':50000})
# use the value of another row
country.fillna(method='ffill')
# use the sklearn package to fill them via mean
from sklearn.impute import SimpleImputer
# when define a variable and put in infront of a class we create an abject
# use the mean value to fill the missing values
imp=SimpleImputer(missing_values=np.nan,strategy='mean')
# enter the dataset into imp object  our data only fitted to the modal
imp.fit(country)
# give me the transformed data
new_dataset=imp.transform(country)
print(new_dataset)
print(new_dataset.mean())
