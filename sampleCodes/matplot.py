# D video
#  lesson Fourth draw diagram ترسیم داده
# use matplotlib to draw different diagram is the usefule pachage for drawing 2dimentional diagrams
import numpy as np
import matplotlib.pyplot as plt
year=[1960,1970,1980,1990,2000,2010,2020,2030,2040]
iran_pop=[1.2,1.7,1.9,2.2,3.2,4.2,5.2,6.2,7.2]
# # # line plot نمودار خطی with plot x,y -- x horizontal , y vertical plt.plot(x,y)
plt.plot(year,iran_pop)
# # for show the diagram
plt.show()
# # scatter plot نمودار نقطه ای x,y -- x horizontal , y vertical plt.scatter(x,y)
plt.scatter(year,iran_pop)
plt.show()
# Histogram plot for show the distributed data
city_name=['Tehran','Shiraz','Esfehan','Yazd','Ghazvin','Mashhad','Sari','kish','gheshm']
city_pop=[123,456,521,859,456,325,178,951,753]
# show the distribution of data and bins is the most important feature which show the number of group
# there is a rule about bins you must calculate the aquare of the group then rand them
plt.hist(city_pop,bins=4)
# use auto let the machine determine the number group
plt.hist(city_pop,bins='auto')
plt.show()
# pi chart  is another duagram to show the data and is divided into several segment
plt.pie(city_pop,labels=city_name)
plt.show()
# show the detail in diagrams and customise the diagram
plt.figure(figsize=(9,7),dpi=80)
plt.plot(year,iran_pop)
# put label on the diagram
plt.xlabel('year')
plt.ylabel('population')
# give the data of diagram
plt.xticks([1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040])
# second argument is for the time we want to show our data in another way
plt.yticks([1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2],['1M','2M','3M','4M','5M','6M','7M','8M','9M'])
# # for show the diagram
plt.show()
# draw scatter diagram   np.arrange(6) means 1,2,3,4,5,6

print(city_name)
# select size for digram if your numbers for size are big you can divide them on 1000 or other number
pop_size=np.array([123,456,521,859,456,325,178,951,753])
# use color for each location
Colors=['red','green','pink','yellow','blue','black','orange','gray','white']
plt.scatter(np.arange(9),city_pop,s=pop_size,c=Colors)
# we can set a margin around our data with margin
plt.margins(0.1)
# use title for diagram
plt.title('Iran poplulation ')
#  change the value of x with the city_name
plt.xticks([0,1,2,3,4,5,6,7,8],['Tehran', 'Shiraz', 'Esfehan', 'Yazd', 'Ghazvin', 'Mashhad', 'Sari', 'kish', 'gheshm'])
#  change the value of x with the city_name
plt.yticks([123, 456, 521, 859, 456, 325, 178, 951, 753],['1M', '4M', '5M', '8M', '4.5M', '3M', '1M', '9M', '7M'])
# we can add title for each scatter on the diagram with text
plt.text(0,123,"captal",fontsize=15)
# print(city_pop)
plt.show()
# Multiple plot
# ls line style and marker is the area i had data and mew is the size
turk_pop=[1.7,1.9,2.2,2.8,3.1,4.6,5,6.5,7.8]
plt.plot(year,iran_pop,ls='-',marker="+",mew=8)
plt.plot(year,turk_pop,ls='--',marker="+",mew=1)
# label for horizontal
plt.xlabel('year')
plt.ylabel('poplulation')
# for change and customize the value of diagram
# plt.xticks()
# plt.yticks()
plt.title('iran and turk poplulation')
# # it is a guild for each line of the diagram
plt.legend(['Iran','Turkey'],loc='best')
plt.grid()
# # put extra information on diagram and arrowprops برای فلش
plt.annotate('iran-iraq war',fontsize=15,xytext=(1980,34.5),xy=(1980,34),arrowprops=dict(facecolor='silver',width=4))
plt.show()
# subplot
# if we want to divide the map into several categori with specific diagram we use subplot(2,2,1) it is equal to row,column,the index of matrix
plt.subplot(1,2,1)
plt.plot(year,iran_pop)
plt.title("iran population")
plt.subplot(1,2,2)
plt.plot(year,turk_pop)
plt.title("turk population")
plt.show()
# seaborn for draw statistic diagram  it is based on matplotlib and for its installation matplotlip must be installed