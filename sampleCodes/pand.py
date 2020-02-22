# # pandas is a library for create data structure and help to analyse the data
import pandas as pd
import numpy as np
# # create series (serie is one of the data structure it is like a list)
my_series=pd.Series([1,2,3],index=['row1','row2','row3'])
print(my_series)
# # show the value of serie
print(my_series.values)
# # show the index of serie
print(my_series.index)
# # show the value of serie via specific index
print(my_series.row2)
# # show the value of serie via specific index
print(my_series['row2'])
# # change the index of serie
my_series.index=['a','b','c']
print(my_series.index)
# ================
# create DataFrame with array (DataFrame is one of the data structure it is like a matrix)
my_array=np.array([[1,5,9,13],[8,6,22,14],[3,7,11,15],[8,8,1,16]])
print(my_array)
my_df=pd.DataFrame(my_array,index=['row1','row2','row3','row4'],columns=['col1','col2','col3','col4'])
print(my_df)
# create DataFrame with Dictionary
my_dict={'col1':[1,2,3,4],'col2':[5,6,7,8],'col3':[9,10,11,12],'col4':[13,14,15,16]}
print('my_dict:',my_dict)
my_df=pd.DataFrame(my_dict,index=['row1','row2','row3','row4'],columns=['col1','col2','col3','col4'])
print(my_df)
# # show index of dataFrame
print(my_df.index)
# # show columns of dataFrame
print(my_df.columns)
# # show values of dataFrame
print(my_df.values)
# # select the object show the all value of first row = loc used for selecting index with the label name
print(my_df.loc['row1'][:])
# # select the object show the all value of first row and column
print(my_df.loc['row1']['col1'])
# # select all the column value in row number 0   we can put the name as well as number of columns and index
print(my_df.iloc[0][:])
# # edit DataFrame and add another column to DataFrame
my_df['col5']=[4,5,9,12]
print(my_df)
# # edit DataFrame
my_df.loc[['row1','row2'],'col1']=0
print(my_df)
# # reset index and drop the row index and use index number instead
my_df.reset_index(drop=True)
print('new_index',my_df)
# # drop the column and its value and axis=1 means this must be applied on column
my_df.drop("col5",axis=1)
print(my_df)
# renaming change the label of index and columns
my_df.rename(columns={'col4':'columns4'})
print('rename',my_df)
# replace the specific value in a dictionary change the value into new one change 2 to 20!
my_df.replace({2:20})
print(my_df)
# apply function on index for example change the type of number in dataFrame to new dataType
print(my_df.col1)
# change the format of all the value in column 0 to float
my_df.col1=['{:.2f}'.format(x) for x in my_df.iloc[:,0]]
print(my_df)
# change the format of col2 to float it is other format of for loop
my_df['col2']=my_df['col2'].apply(lambda x:'{:.2f}'.format(x))
print(my_df)
#  sorting dataFrame base on label or based on the valus
#  sort index
my_df.sort_index(axis=0, ascending=False)
print(my_df)
# sor values
my_df.sort_values(by='col1',ascending=False)
print(my_df)
# useful methods in dataFrame for general information about dataframe
# head methods show number of  first row
print(my_df.head(2))
# head methods show number of  last row
print(my_df.tail(2))
# read the data of the file via specific directory
data=pd.read_csv('D://test.txt')
print(data)