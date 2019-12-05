#coding:utf-8

from die import Die
import pygal
'''绘制直方图'''

die = Die()

results = []
for roll_num in range(1,1000,1):
    '''将每次随机投掷的点数存入列表中'''
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1,die.num_sides+1):
    '''将骰子的每个面被投掷出的频率记录在列表中'''
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'Result'
hist.y_title = 'Frequency Of Result'

hist.add('D6',frequencies)
#生成了svg图像后，可以在本地路径中查找，然后用web浏览器打开该svg图像
hist.render_to_file('die.visual.svg')
