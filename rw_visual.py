#coding:utf-8

import matplotlib.pyplot as plt
import pygame
import sys
import tkinter
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    #绘制绘图窗口的尺寸 https://blog.csdn.net/m0_37362454/article/details/81511427
    #dpi为输出分辨率，每英寸长度上的点数，点数越大，图片分辨率越大？？
    fig1 = plt.figure(dpi=128, figsize=(12,6),facecolor=(0,0.8,0),edgecolor=(1,0,0))
    # plt.axes([200,0,500,500])
    ax1 = plt.Axes(fig1, [0.1,0.1,0.3,0.3])
    #https://www.zhihu.com/question/51745620,轴域的概念，可以控制画板上画纸的位置和大小
    ax2 = plt.axes([0.5,0.5,0.3,0.3])
    # ax3 = plt.subplot(222)
    ax1_1 = fig1.add_axes(ax1)
    ax2_1 = fig1.add_axes(ax2)
    # fig1.add_axes(ax3)

    points = list(range(rw.num_points))

    #点
    ax1_1.scatter(x=rw.x_values, y=rw.y_values, s=1, c=points, cmap=plt.cm.Oranges, edgecolors= 'none')
    ax2_1.scatter(x=rw.x_values, y=rw.y_values, s=1, c=points, cmap=plt.cm.Oranges, edgecolors= 'none')
    # plt.scatter(x=rw.x_values, y=rw.y_values, s=1, c=points, cmap=plt.cm.Oranges, edgecolors= 'none')
    #线
    # plt.plot(rw.x_values, rw.y_values, linewidth=5, c=(0.5,0.5,0.8))
    '''
    #设置起始点为红色，重点为绿色
    #下面的plt.是在只有一个图例的前提下使用的
    #可以取消注释查看效果，会默认将效果施加到最新的图例上，也就是ax2
    plt.scatter(x=0, y=0, s=50, c='red')
    plt.scatter(x=rw.x_values[-1], y=rw.y_values[-1], s=50, c='green')
    plt.title('color',fontsize='24', color=(0,1,0))
    plt.xlabel(xlabel='X-axis', fontsize=20, color=(1,0,0))
    plt.ylabel(ylabel='Y-axis', fontsize=20, color=(0,0,1))
    plt.tick_params(axis='both',color=(1,0,0),labelsize=10)
    ######## plt.axis([-500,500,-500,500])
    '''

    #https://blog.csdn.net/weixin_41789633/article/details/79826935
    # 用matplotlib设置标题、轴标签、刻度标签以及添加图例
    #针对1个画面多个图例的各元素设置,
    #根据代码来看，区别是在设置单图例的属性前加set_  ，如下所示
    ax1_1.set_title("ax1")
    ax2_1.set_title("ax2")
    ax1_1.set_xlabel(xlabel='X-axis', fontsize=20, color=(1,0,0))
    ax2_1.set_ylabel(ylabel='Y-axis', fontsize=20, color=(0,0,1))

    #下面这两行会报错，但是功能是正确的，先学习全章再对此进行修复？？？？？？？？？？？？？？？？
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.show()

    #有问题，会出另一个多余的空白框？？？？？？？？？？？？？？？？？？？？？？？？？
    #tkinter.messagebox.showinfo('提示','输入n退出程序，输入非n字符程序重新执行')
    #按下q键关闭窗口，可单独做成函数进行调用，使代码整洁
    if pygame.KEYDOWN == pygame.K_q:
        sys.exit()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break



