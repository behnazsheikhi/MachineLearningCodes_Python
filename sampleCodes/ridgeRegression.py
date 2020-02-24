from sklearn.linear_model import Ridge
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
boston=load_boston()
ridge=Ridge(alpha=1,normalize=True)
x=boston.data
y=boston.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
ridge.fit(x_train,y_train)
ridge_pre=ridge.predict(x_test)
print(ridge_pre)