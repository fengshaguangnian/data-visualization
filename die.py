#coding:utf-8#

#coding:utf-8

import matplotlib.pyplot as plt
import pygame
import sys
import tkinter
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk()
rw.fill_walk()

#绘制绘图窗口的尺寸 https://blog.csdn.net/m0_37362454/article/details/81511427
#dpi为输出分辨率，每英寸长度上的点数，点数越大，图片分辨率越大？？
fig1 = plt.figure(dpi=128, figsize=(12,6),facecolor=(0,0.8,0),edgecolor=(1,0,0))
# plt.axes([200,0,500,500])
# ax1 = plt.Axes(fig1, [0.1,0.1,0.8,0.8])
#https://www.zhihu.com/question/51745620
ax1 = plt.axes([0.1,0.1,0.8,0.8])
fig1.add_axes(ax1)

points = list(range(rw.num_points))

#点
plt.scatter(x=rw.x_values, y=rw.y_values, s=1, c=points, cmap=plt.cm.Oranges, edgecolors= 'none')
#线
# plt.plot(rw.x_values, rw.y_values, linewidth=5, c=(0.5,0.5,0.8))
plt.scatter(x=0, y=0, s=50, c='red')
plt.scatter(x=rw.x_values[-1], y=rw.y_values[-1], s=50, c='green')
plt.title('color',fontsize='24', color=(0,1,0))
plt.xlabel(xlabel='X-axis', fontsize=20, color=(1,0,0))
plt.ylabel(ylabel='Y-axis', fontsize=20, color=(0,0,1))
plt.tick_params(axis='both',color=(1,0,0),labelsize=10)

plt.show()

