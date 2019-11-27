#coding:utf-8

import matplotlib.pyplot as plt
# import math

# for n in range(-90,91,1):
#     plt.scatter(n, math.cos(n), s=1, color='red')

x_values = list(range(0,1001))
y_values = [x**2 for x in x_values]

#s为点的大小;edgecolors='none'可以删除数据点的轮廓，使其变得更加平滑;
#color或者c的值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅。还是用c比较省事，可以使用cmap
# plt.scatter(x_values, y_values, edgecolors='none', s=40, color=(0,0,0.8))
plt.scatter(x_values, y_values, edgecolors='none', s=40, c=y_values, cmap=plt.cm.Blues)

#设置图标标题并给坐标轴加上标签
plt.title("Squares Numbers", fontsize = 24, color=(0,1,0))
plt.xlabel("Value", fontsize=14, color=(0,0,1))
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=14, color=(1,0,0))

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

#plt.show()和plt.savefig不能共用，不然关闭运行程序后，才会保存图片，该图片还会一片空白
plt.show()
# plt.savefig("squeres_plot.png",bbox_inches="tight")


