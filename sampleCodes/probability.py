# E lesson
# probability احتمال
# we can calcualte the pobability of  things via calculating others
import numpy as np
import random as r
# generate three number between 0 to 1  ---> test which has two option like coin شیر or خط named
# Pseudo number generator تولید اعداد شبخ تصادفی به دلیل اینکه داریم از یک الگوریتم استفاده میکنه
np.random.seed(42)
rand_num=np.random.random(3)
win= rand_num>0.5
print(win)
print(rand_num[win])
num_trial=100000
rand_num=np.random.random(size=num_trial)
win=rand_num>0.5
num_win=np.sum(win)
print(num_win/num_trial)
# random walk
import random as r
import numpy as np
for i in range(100):
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