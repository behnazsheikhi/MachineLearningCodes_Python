# lesson H
#  در هر دو مساله طبقه بندی و رگرسیون اطلاعات را به دو دسته test , train تقسیم می کنیم
# CrossValidation (K-Fold Cross Valodation)
# to optimize the result,we can use cross validation technique
# اطلاعات را به چند بخش تقسیم می کنیم (k fold) بخش اول را برای تست نگه میداریم و باقی بخش ها را برای مرحله  train‌استفاده میکنیم
# test data   others Training data
#  در کل مراحل اون اون بخش را نگه می داریم باقی را برای Fit کردن استفاده میکنیم تا آخرین مرحله
#  k بخش داریم , K بار train , test میکنیم و هر بار تستی که گرفتیم با دفعه قبل فرق داشته  --> k تجربه آموزش متفاوت
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import numpy as np
boston=load_boston()
reg=LinearRegression()
x=boston.data
# print('x',x)
y=boston.target
# print('y',y)
cv_scores=cross_val_score(reg,x,y,cv=5 )
print(cv_scores)
#  calculate the average of cv_scores
np.mean(cv_scores)
print(np.mean(cv_scores))
# در رگرسیون خطی ما بدنبال کمینه کردن تابع خطا هستیم و باید ضرایبی انتخاب می شد که خطی را ترسیم کند که کمترین میران خطا را داشته باشد
# model هم باید ساده و سرراست باشد و از پیچیدگی های اضافی هم جلوگیری شود
# یکی از روش هایی که از پیچیدگی مدل جلوگیری میکند Regularization Regression است
#  Regularization Regression با اضافه کردن یک جمله جدید به تابع هزینه قبلی یک تابع جدید ایجاد میکند
# cost function=OLS + Regularization Regression (penalty) که باعث فیلتر شده داده می شود
#  باعث می شود که ضرایب ویژگی ها مقادیر کوچکتری داشته باشند
# Regularization Regression --> 1. ridge Regression در پکیج sklearn  --> 2. Lasso Regression
# ridge Regression مقدار توان دو ضرایب را در فرمول میزارد ضرب در عدد آلفا که می تواند منجر به OverFitting یا underFitting شود
# Lasso Regressionمقدار قدرمطلق ضرایب را در فرمول میزارد و  باعث می شود ویژگی هایی که تاثیر کم دارن حدف شوند
# آلفا شبیه به k هست