#coding:utf-8
#https://matplotlib.org/gallery/index.html

import matplotlib.pyplot as plt


input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
#线
plt.plot(input_values,squares,linewidth=5)
#点
# plt.scatter(input_values,squares,s=10)
# 设置图表标题，并给坐标轴加上标签
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)
plt.show()








