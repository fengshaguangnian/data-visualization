#coding:utf-8

from die import Die
import pygal
'''绘制直方图'''

die1 = Die(num_sides=6)
die2 = Die(num_sides=8)
die3 = Die(num_sides=10)

results = []
for roll_num in range(1,1000,1):
    '''将每次随机投掷的总点数存入列表中'''
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(3,max_result+1):
    '''将多个骰子被投掷出的结果的频率记录在列表中'''
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling three D6 1000 times."
# hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_labels = list(n for n in range(3,die1.num_sides+die2.num_sides+die3.num_sides+1))
hist.x_title = 'Result'
hist.y_title = 'Frequency Of Result'

hist.add('D6+D8+D10',frequencies)
#生成了svg图像后，可以在本地路径中查找，然后用web浏览器打开该svg图像
hist.render_to_file('die.visual.svg')
