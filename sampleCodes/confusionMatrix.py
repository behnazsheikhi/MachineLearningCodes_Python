# Lesson I
# برای شناسایی دقت یک مدل ما از روش train و test استفاده کردیم اما بررسی تخمین دقت یک مدل بستگی خیلی زیادی به داده هایی که به ماشین داده ایم دارد
# مثلا اگر نمونه ای 99٪ از داده ها را با وضعیت درست به مات بدهیم که تنها ۱٪ غلط است در این حالت ماشین ۹۹٪ مواقع صحیح میگوید و این نشان دهنده ی یادگیری خوبی برای ماشین نیست
# یکی از روش های بررسی دقت روش Confusion matrix(ماتریس درهم ریختگی) است
#  در ستون های این ماتریس مقادیر پیش بینی شده و در سطرهای آن مقادیر واقعی گذاشته می شود.
# Accuracy                                       # Precision  tp/tp+fP                               # Precision
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,classification_report
bcd=datasets.load_breast_cancer()
x=bcd.data
y=bcd.target
# print(x.shape)
# print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
knn=KNeighborsClassifier(n_neighbors=8)
knn.fit(x_train,y_train)
y_pre=knn.predict(x_test)
# print(confusion_matrix(y_test,y_pre,[0,1]))
# print(classification_report(y_test,y_pre))
# Logistic  Regression   برخلاف اسمش یک الگوریتم دیگر classification هست و برای طبقه بندی های باینری مورد استفاده قرار میگیرد.
# و نه مسایل رگرسیون Logistic  Regression یک classification‌ خطی را برای ما انجام میده و خروجی های آن احتمال انتخاب شدن اون برچسب مورد نظر است
#ایمیل است مثلا احتمال اسپم یا غیر اسپم بودن ایمیل - در واقع p یاprobability که خروجی این تابع است اگر بزرگتر از 0.5 باشد در این صورت ایمیل برچسب اسپم میگیرددر واقع p احتمال اسپم بودن
# این حد نیم را همیشه به صورت default این مقدار می تواند بین 0 تا 1 باشد و با اون منحنی ای را بوجود بیاریم که به آن ROC کفته می شود
from sklearn.linear_model import LogisticRegression
log=LogisticRegression()
log.fit(x_train,y_train)
y_pre=log.predict(x_test)
cm=confusion_matrix(y_test,y_pre,[0,1])
# print(cm)
#شبیه knn عمل کرد LogisticRegression در خروجی می بینیم مدل
#confusion_matrix نرمالسازی
from sklearn.preprocessing import normalize
import pandas as pd
cm=normalize(cm,norm='l1',axis=1)
cm_df=pd.DataFrame(cm,columns=bcd.target_names,index=bcd.target_names)
# print(cm_df)
# ROC  CURVE
# TPR = true positive / true positive + false negative ---> recall (sensitivity)
# FPR= false positive / false positive + true negative
#  ROC یک روش نمایشی برای بررسی عملکرد یک calssifier باینری هست که اگر p بین 0 تا 1 باشد امکان ترسیم آون وجود دارد
from sklearn.metrics import roc_curve
y_pre_prod=log.predict_proba(x_test)[:,1]
fpr,tpr,ther
print(y_pre_prod)
# roc_curve(y_test,y_pre_prod)
