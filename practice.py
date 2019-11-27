#coding:utf-8

'''
import matplotlib.pyplot as plt

X_values = list(range(0,5001))
Y_value = [n**3 for n in X_values]
#plt.cm的属性：https://blog.csdn.net/baishuiniyaonulia/article/details/81416649
plt.scatter(x=X_values, y=Y_value, c=Y_value, cmap=plt.cm.OrRd, edgecolors='none', s=50)

plt.title(label="Title",fontsize=24, color=(0,1,0))
plt.xlabel(xlabel="X_label", fontsize=24, color=(0,1,0))
plt.ylabel(ylabel="Y_label", fontsize=24, color=(0,1,0))

plt.tick_params(axis='both',which='major',labelsize=14, color=(0,1,0))
plt.axis([0,5000,0,5000**3])

plt.show()
'''


'''
import matplotlib.pyplot as plt

X_value = list(range(0,1001))
Y_value = [x**2 for x in X_value]

plt.scatter(x=X_value, y=Y_value, c=Y_value, cmap=plt.cm.GnBu, linewidths=20, edgecolors='none', s=80)
plt.title(label='Isometric Chart', fontsize=24, color=(1,0,0))
plt.xlabel(xlabel='X-Axis', fontsize=20, color=(0,1,0))
plt.ylabel(ylabel='Y-Axis', fontsize=20, color=(0,0,1))
plt.tick_params(axis='both', which='major',labelsize=15, color=(1,0,0))

plt.axis([0,1000,0,1000000])

plt.show()
# plt.savefig('E:\天阳宏业\math\plt.png')
'''



'''
import math
import matplotlib.pyplot as plt

X_values = list(range(-1000,1000))
Y_value = [math.sin(n/100) for n in X_values]
#plt.cm的属性：https://blog.csdn.net/baishuiniyaonulia/article/details/81416649
plt.scatter(x=X_values, y=Y_value, c=Y_value, cmap=plt.cm.OrRd, edgecolors='none', s=50)

plt.title(label="Title",fontsize=24, color=(0,1,0))
plt.xlabel(xlabel="X_label", fontsize=24, color=(0,1,0))
plt.ylabel(ylabel="Y_label", fontsize=24, color=(0,1,0))

plt.tick_params(axis='both',which='major',labelsize=14, color=(0,1,0))
# plt.axis([0,5000,0,5000**3])

plt.show()
'''



