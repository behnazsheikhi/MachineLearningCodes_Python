import random as r
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
step=0
dice=r.randint(1,7)
# dice=np.random.randint(1,7)
if dice<3:
    step=max(0,step-1)
elif dice<3:
    step=step+1
else:
    num = r.randint(1, 7)
    step=step+num
print('dice is {} and you are in {} step'.format(dice,step))
# ------------------------------------------------------------------------------
# random walk
step = 0
# create an empty array
rand_walk=np.empty(0)
for i in range(100):
    dice=r.randint(1,7)
    # dice=np.random.randint(1,7)
    if dice<3:
        step=max(0,step-1)
    elif dice<3:
        step=step+1
    else:
        num = r.randint(1, 7)
        step=step+num
    rand_walk=np.append(rand_walk,step)
    print('dice is {} and you are in {} step'.format(dice,step))

# --------------------------------------------------------------------------

plt.step(np.arange(100),rand_walk)
plt.show()
# --------------------------------------------------------------------------
for i in range(1000):
    step = 0
    # create an empty array
    d=np.empty(0)
    for i in range(100):
        dice=r.randint(1,7)
        # dice=np.random.randint(1,7)
        if dice<3:
            step=max(0,step-1)
        elif dice<3:
            step=step+1
        else:
            num = r.randint(1, 7)
            step=step+num
        d=np.append(d,step)

plt.figure(figsize=(10,15))
sb.distplot(d)
plt.show()
# احتمال اینکه به \له ی 60 ام برسم
print(np.mean(d>60))
# normal distribution  تویع نرمال داده ها حول میانگین جمع می شود
samples=np.random.normal(0,1,size=1000)
sb.distplot(samples)
plt.show()