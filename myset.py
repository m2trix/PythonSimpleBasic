'''
set
Python 内置数据结构
无序
可更改
set 可以视为没有 value 的 dict，只存 key
一般用做去重或者集合求交，求并等
'''

girls_1 = set(['lucy', 'lily'])
girls_2 = set(['lily', 'anna'])
print(len(girls_1))

# 求交集
print(girls_1 & girls_2)

# 求并集
print(girls_1 | girls_2)

# 增
girls_1.add('marry')
print(girls_1)

# 删
girls_1.remove('lucy')
print(girls_1)