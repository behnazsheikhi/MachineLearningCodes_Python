# D video
# seaborn for draw statistic diagram  it is based on matplotlib and for its installation matplotlip must be installed
import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#  strip plot is the kind of diahram which can be drawn via one variable
# plot the distribution of variables for each category as individual data point
my_array=np.array([["galaxys8","andriod64",64,4,1490,'samsung',5.8],["galaxyA50","andriod64",128,4,1400,'google',5.8],["A&","andriod64",256,4,1490,'kia',5.8],["nokia","andriod64",32,10,1560,'samsung',6]])
smartphones=pd.DataFrame(my_array,index=['0','1','2','3'],columns=['Name','OS','Capacity','RAM','Weight','Company','Inch'])
print(smartphones)
# jitter show the distrinution of the data
sb.stripplot(x='OS',y='Capacity',data=smartphones,size=10,jitter=True)
plt.show()
# swarm plot  is the same as stripplot bit it doesn not show any overlab
plt.figure(figsize=(13,8))
# # hue mean based on the selected object choose a color and put guid on diagram
sb.swarmplot(x='OS',y='Capacity',data=smartphones,size=15,hue= 'Company')
plt.show()
# box plot  Q1 is the place where  is bigger than of 25% of data   Q2 میانه  is the between my data   Q3 is bigger than 75% of my data
# q1 form the average to the small one  1 2 3 5 6 10 12  we must find this values min q1 q2 q3 max
# for accurate result we must have loads of data
sb.boxplot(x='Company',y='RAM',data=smartphones)
plt.show()
# JointPlot   visualise a bivariate distribution and we can see the histogram data on vertical and horizontal
sb.jointplot(x='Capacity',y='RAM',data=smartphones,kind='scatter')
plt.show()
# pair plot we can take the whole information of our data and their histogram
sb.pairplot(smartphones,hue="Name",palette='hls')
# sb.pairplot(smartphones,hue="Name",palette='hls',plot_kws={'s'=80})
plt.show()
# for extra information  https://seaborn.pydata.org/toturial.html#
# plotly is a package for interactive diagram