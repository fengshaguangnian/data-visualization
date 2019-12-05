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



import pymysql

#计算两个6面筛子投掷之和及结果的出现次数，并将结果放在mysql库
results = []
for para1 in range(1,7):
    for para2 in range(1,7):
        sum = para1 + para2
        results.append(sum)
print(results)

dict = {}
results_set = set(results)
for para in results_set:
    dict[para] = results.count(para)
print(dict)

db = pymysql.connect("localhost","root","123456","data1")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS DICE")
sql = """CREATE TABLE DICE (
         Number  CHAR(20) NOT NULL,
         Count  CHAR(20) )"""
cursor.execute(sql)

for number,count in dict.items():
    number_str = str(number)
    count_str = str(count)
    sql2 = "INSERT INTO DICE (Number,Count) VALUES('%s','%s')"%(number_str,count_str)
    try:
        cursor.execute(sql2)
        db.commit()
        print("插入成功")
    except:
        db.rollback()
        print("插入失败")
