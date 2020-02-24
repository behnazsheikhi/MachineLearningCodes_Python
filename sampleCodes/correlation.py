# E lesson
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
# data via a csv file
smartphones=pd.read_csv("D://smartphones.txt")
plt.scatter(smartphones.inch,smartphones.Weight,s=80)
plt.xlabel('inch')
plt.ylabel('weight')
plt.show()
# to draw a line for your data on diagram measure differences between line and points and use that one which has the smallest differences for all points
#  if there is positive correlation among points fit line has Positive gradient and value would be between 0 and 1
#  if there is negative correlation among points fit line has negative gradient and value would be between -1 and 0
#  if there is not any correlation among points fit line has zero gradient and value would be 0
#  if the value of correlation is near to 1 in positive correlation it shows data has more correlation
#  how to calculate correlation
# 1 parametric methods
# paarson correlation if the values are numerical variable and there is a linear related between them  and normally distributed we can use pearson correlation
# it is a functional methods to show the relation between to values
# covariance/(std of x)(std of y)    --> std is انحراف معیار   the vale is between -1 to 1
#
# scipy pachage used for scientific and technical comuting  برای محاسبات علمی و بسط داده شده از انکانات پایه ای numpy و بهینه سازی جبرخظی
#  it contains modules for
#  از پکیج scipy , زیر پکیج status و pearsonr را import میکنیم
from scipy.stats import pearsonr
pearsonr_coefficent,_=pearsonr(smartphones.inch,smartphones.Weight)
print(pearsonr_coefficent)
# another way to caculate the pearson is pandas
num_var=smartphones.drop(['Name','OS',"Capacity","Ram","Company"],axis=1)
print(num_var)
corr=num_var.corr()
print(corr)
# another way is the heatmap diagram on seaborn pachage   show the numeric value with the color
# vmin is the least correlation and vmax is the maximun correlation it is sutable when we have loads of number
sb.heatmap(corr,xticklabels=corr.columns,yticklabels=corr.columns,vmin=-1,vmax=1)
plt.show()
# Nonparametric Methods
# spearman rank correlation   find correlation between the ordinal variable ordinal variables are type of variable which have specific value such as Ram of smartphones
# 1.for ordinal variable (categorical numeric) 2.Non normally distributed 3. No linear related
print(smartphones)
#
# Chi-Square test   to know the variables are independent or not
# totally it is for estimating a hypothesis
# NULL Hypotesis or Alternative Hypotesis
# فرض صفر یک عبارت منفی است مثلاً درایفت پاسخی در قبال سوال ما که تغییری رو رخ نمیدهد اتفای رخ نداده خیری نیست
# اول صحت ایمیل اسم نیست را بررسی میکنیم
# Null and alternative Hypotesis are opposit
# we always think we can reject null hypothesis or not when the value is under 0.05 we can reject the null hypo
# احتمال به اشتباه تشخصی دادن رو محاسبه میکند احتمال اشتباه کردن وقتی از 0.05 بیشتر میشود فرض صفر درست است و اگر کوچکتر از 0.05 باشد  pvalue
# extra information khanacademy
# degree of freedom (row-1)*(column-1)    درجه ازادی بین دو متغیر
# ضریب اهمیت یا الفا که بخش انتهایی نمودار هستش که معمولا مقدارش 5% است
# به بخش انتهایی نمودار rejection region میگویند با کمک ناحیه مردودی نتیجه تست chi رو پیدا کنیم که اگر نتیجه در این بخش قرار بگیرد null hypothesis رد خواهد شد
# اگر نتایج تست chisquare در این بخش قرار بگیرد می توانیم null hypothsis را رد کنیم
# for chisuare we need the critical value of rejection region to undestand whether the result of chisquare is into it or not
# based on two values of degree of freedom and p value(alpha) we can get information about critical value
# chisquare = sum( (o-e)**2/e))
#  for calculate the value of chisquare
from scipy.stats import chi2_contingency
#  to create an observed table it is important to know for chisquare we must use categorical number if the data are numeric we must divide them
#  into several categories
table=pd.crosstab(smartphones.Capacity,smartphones.Ram)
print(table)
# the result of chi2_contingency is chi2,p_value,dof,expected    and rejection region is the hit in dof and p_value(alpha)
#  we must compare chisquare to rejection region value
chi2,p_value,dof,expected=chi2_contingency(table.values)
print(chi2)
