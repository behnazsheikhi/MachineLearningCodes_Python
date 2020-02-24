# F lesson
# concatenating  & drop & duolicate
#  create a new dataset via combination of two or more than dataset
import numpy as np
import pandas as pd
my_source1=pd.read_csv('D:\machineLearning_video\InputTextFile\my_source1.txt')
my_source2=pd.read_csv('D:\machineLearning_video\InputTextFile\my_source2.txt')
print(my_source1)
print(my_source2)
my_concat=pd.concat([my_source1,my_source2],axis=0 ,ignore_index=True)
# print(my_concat)
# delete cloumn4 from dataset
my_concat.drop('4',axis=1,inplace=True)
# print(my_concat)
# delete duplicate data
my_concat=my_concat.drop_duplicates(inplace=True)
# reset the indexes of data
# my_concat.reset_index(drop=True,inplace=True)
smartphones=pd.read_csv('D:\machineLearning_video\InputTextFile\smartphones.txt')
print(smartphones)
# describe gives extra statistic information for numeric values
print(smartphones.describe())
# find the number of categorical values   with value_counts()
print(smartphones.OS.value_counts())
# Group by based on categorical values
cat_os=smartphones.groupby(smartphones['OS'])
print(cat_os.mean())