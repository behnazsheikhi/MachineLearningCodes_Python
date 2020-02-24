# F lesson
# Dupplicates   داد های تکراری  -- علت پاک کردن آنها ایجاد یک DataFrame با دقت بالاس , پس باید مقادیر تکراری حذف شوند تا داده های آماری استخراج شده قابل ستناد باشن.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
data=pd.read_csv('D://Duplicates.txt',encoding='ansi',header=0)
print(data.duplicated())
# delete Duplicated value in dataFrame
print(data.drop_duplicates())
#  delete Duplicated value via indexes of each value
print(data.drop_duplicates(['Columns2']))
