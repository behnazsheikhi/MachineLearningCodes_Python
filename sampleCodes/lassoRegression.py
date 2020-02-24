# Lesson H
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
from sklearn.linear_model import Lasso
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
boston=load_boston()
lasso=Lasso(alpha=0.1,normalize=True)
x=boston.data
y=boston.target
lasso.fit(x,y)
# coed coefficient ها ضرایب ما هستن
Lasso_coeff=lasso.coef_
print(Lasso_coeff)
plt.plot(range(13),Lasso_coeff)
plt.xticks(range(13),boston.feature_names)
plt.ylabel('coefficients')
plt.show()