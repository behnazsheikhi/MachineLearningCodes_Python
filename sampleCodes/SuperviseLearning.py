# lesson G
# یادگیری ماشین آموختن توانایی تصمیم گیری به ماشین(کامپوتر-ربات یاهر وسیله ای که امکان پردازش داده دارد) بر اساس یک سری از داده ها می گویند
# علت استفاده از ماشین ها سرعت بالای پردازش است
# سه رویکرد برای یادگیری ماشین وجوددارد
#   : داده های ورودی به ماشین برچسب دار هستن مثل ایمیل اسپ یا غیر اسپم - داده های ایمیل ها هستن و خروجی اسپم یا غیر اسپم درواقع دادها براساس برچسب ها طبقه بندی می شوند.یادگیری نظارت شده
# یادگیری غیر نظارت شده:خود ماشین باید تشخیص بدهد برعکس روش قبل که ورودی برچسب دار به ماشین داده می شد.
# یادگیری تقویت شده: ماشین در یک چرخه قرارا دارد و در اون چرخه دایما داره خودش را اصلاح میکند و دایما با محیط در تعامل هستش و از طریق تشویق یا تنبیه خودش را اصلاح میکند
# مثال های یادگیری نظارت شده که در آن ورودی و خروجی مشخص و برچشب دار هست مثل ایمیل اسپم یا غیر اسپم - پیدا کردن بیماری در افراد بر اساس علایم بیماری -
#   برچسب ها می توانند مقادیر کسسته داشته باشند مثل نوع بیماری ها- اسپم یا غیر اسپم بودن به این نوع مسایل که برچسب گسسته دارن طبقه بندی می گویند (classification)
#  اگر داد ها مقادیر پیوسته داشته باشند مثل قیمت خونه ها بر اساس یک سری ویژگی ها و هدف این است که ماشین باویژگی های جدید قیمت را پیش بینی کند اینجا پیش بینی قیمت پیوسته است که باید عدد بدهد به این حالت رگرسیون می گویند(Regreesion)
#  در یادگیری ماشین اطلاعات در قالب یک جدول به ماشین داده میشود هر سطر مربوط به یک نمونه است و هر ستون ویژگی های نمونه می باشدهر سطر مربوط به یک خونه و ستون ها ویژگی های خونه
# Iris Dataset :  150 iris flower in each row --> sample   columns--> feature , attribute , dimentions ,measure that are calculate for each sample
#  result --> target
# find a appraoch base on data
#  الگوریتم های یادگیری نظارت شده:
# 1. K Nearest Neighbors (kNN) :
# dataset is in sklearn pachage
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
iris=datasets.load_iris()
# shape of dataset
print(iris.data.shape)
# name of feature
print(iris.feature_names)
# name of target
print(iris.target_names)
# detail information about dataset
print(iris.DESCR)
# data of the dataset
print(iris.data)
# define a dataframe base on iris.data
iris_def=pd.DataFrame(iris.data,columns=iris.feature_names)
print(iris_def)
# add target column to dataFrame base on iris.target
iris_def['target']=iris.target
print(iris_def)
# visual EDA  --> Explorer   data Analyser  how data are related to each other in statistic
# plotting   متدهای مربوط به رسم در این است   c-->color رنگ گذاری برچسب ها  s --> size  figsize -->
pd.plotting.scatter_matrix(iris_def,c=iris.target, figsize=[11,11],s=150)
plt.show()
# 1. K Nearest Neighbors (kNN) : هر نمونهی جدیدی که به ماشین می دهیم را بر اساس یک تعداد داده ی اطراف(کی) چک می کند به کدان گروه تعلق دارد
# تعداد داده ی اطراف k رای گیری نیکند بر اساس داده های اطرافش
# اولین مرحله train کردن ماشین یا همون fit کردن هستش
# برای رسم نمودار باید از دو تا feature استفاده کرددر اینجا تمام 150 نمونه و با استفاده از feature 2,3
x=iris.data[:,[2,3]]
y=iris.target
print(x)
# print(y)
plt.scatter(x[:,0],x[:,1],c=y)
plt.show()
# Fit
from sklearn.neighbors import KNeighborsClassifier
# create an object   x is a 150 * 4 array and y is a 150*1 array
knn=KNeighborsClassifier(n_neighbors=6,metric='minkowski',p=2)
x=iris.data
y=iris.target
# first parameter is feature and second parameter is labels and it creates a modal
knn.fit(x,y)
print(knn.fit(x,y))
# metric when we speak about the k nearest neighbor we must say about the distance of the neighbor
# to indentify the distance
#  1. Euclidean distance فاصله ی اقلیدسی بین دو نقطه خطی است که دو نقطه را به هم وصل میکند
#  2. Manhatan distance کمترین  فاصله ای که می شود بین دو نقطه را انداه گرفت فقط با دو خط افقی و عمودی روی محور x , محور غ
#  3. Minkowski distance    شکل کلی فاصله ی اقلیدسی و منهتن هستش که بر اساس lambda تیدیل به یکی از این روش ها می شود
#     if lambda=1 --> Manhatan distance   , lambda=2 --> Euclidean distance , lambda=inf --> Chebyshev distance
#     Chebyshev distance   is like the  king movement in chest games it can go to next neighbor by 1 movement
#  for more information https://lyfat.wordpress.com
#  Predict پیش بینی کردن :   استفاده از الگوریتم های ماشین لرنینگ تاامکان پیش بینی بر اساس نمونه های جدید بوجود بیاد
#  it is important to know there should not ne any missing value in the dataset
print(iris.data)
x_new=np.array([[5,3,1,0.2]])
y_new=knn.predict(x_new)
print(y_new)
# to understand whether machine prediction is true or not we can use more than half of data for training then use others data to know machine prediction is correct or not
# train and test  use  train_test_split x,y and test_size 30% of data , random_state is like seed n random
# , stratify in data for test and train assign same proportion
from sklearn.model_selection import train_test_split
# order of the variable is important first x then y first train then test
#  divide our data in two section od train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42,stratify=y)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
# use algoritm to train then predict and finally test it
# create model then fit data to the model
knn=KNeighborsClassifier(n_neighbors=28)
knn.fit(x_train,y_train)
y_predict=knn.predict(x_train)
print(y_predict)
# identify how accurate is the model  --> change the value of n_neighbors will change the result of score
#  but what is the optimal value of n_neighbors?
print(knn.score(x_test,y_test))
# Over Fitting and Under Fitting
neighbors=np.arange(1,30)
train_accuracy=np.empty(len(neighbors))
test_accuracy=np.empty(len(neighbors))
for i,k in enumerate(neighbors):
    knn_model=KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(x_train,y_train)
    train_accuracy[0]=knn_model.score(x_train,y_train)
    test_accuracy[0]=knn_model.score(x_test,y_test)
plt.plot(neighbors,train_accuracy,label="train_accuracy")
plt.plot(neighbors,test_accuracy,label="test_accuracy")
plt.legend()
plt.xlabel('number of neighbors')
plt.ylabel('Accuracy')
plt.show()
# another way to classifivate data is decision tree
# با استفاده از یک سری سوال نمونه ها را از هم تفکیک و در هر انشعابی قرار می دهدهر بار بایدیک سری سوالی ظراحی شود که dataset را به دو دسته تقسیم کند
#  تا اینکه به آخرین سزح برسد که دیگر راهی وجود ندارد
# سوالها مسیر حرکت را مشخص میکنند
# use decision tree and implement it on iris dataset with tree subpachage
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
dtc.fit(x_train,y_train)
predict_dtc=dtc.predict(x_test)
# use metrics for analyze
from sklearn import metrics
metrics.accuracy_score(y_test,predict_dtc)
print(metrics.accuracy_score(y_test,predict_dtc))
print(dtc.score(x_test,y_test))
