# F lesson
# crosstab or crosstabulation
import pandas as pd
smartphones=pd.read_csv('D:\machineLearning_video\InputTextFile\smartphones.txt')
# create table based on input features (OS,Capacity)
pd.crosstab(smartphones.OS,smartphones.Capacity)
print(pd.crosstab(smartphones.OS,smartphones.Capacity))
# Pivot table
print(smartphones)
# pivot table based on index and columns create a table and put the values in that table (Ram)
#  this is obvious some of the values are NaN
new_pivot=pd.pivot_table(smartphones,index='Name',columns='Company',values='Ram')
print(new_pivot)
