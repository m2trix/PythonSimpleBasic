#!/usr/bin/python
#-*- coding: UTF-8 -*-

game = ["111", "222", "333"]
print(game)

print(len(game))

# 增
game.append("444")
print(game)

game.insert(3, "aaa")
print(game)

# 删
game.pop()
print(game)

lis = ["a", "b", "c"]
del lis[0]
lis.remove("b")
lis.pop()


game.pop(1)
print(game)

# 改
game[2] = "bbb"
print(game)

# 查
print(game[0])
print(game[1])
print(game[2])

# 组合两个列表
[1, 2, 3] + [4, 5, 6]

# 列表的乘法
['Hi!'] * 4

# 判断元素是否存在于列表中
3 in [1, 2, 3]

# 迭代列表中的每个元素
for x in [1, 2, 3]: print x

# 切片
# list[start:end]
'''
start代表起点索引，end代表结束点索引。省略start表示以0开始，省略end表示到列表的结尾。注意，区间是左闭右开的！
也就是说[1:4]会截取列表的索引为1/2/3的3个元素，不会截取索引为4的元素。
分片不会修改原有的列表，可以将结果保存到新的变量，因此切片也是一种安全操作，常被用来复制一个列表，例如newlist = lis[:]。

如果提供的是负整数下标，则从列表的最后开始往头部查找。例如-1表示最后一个元素，-3表示倒数第三个元素。
切片过程中还可以设置步长，以第二个冒号分割，例如list[3:9:2]，表示每隔多少距离取一个元素。

>>> a = [1,2,3,4,5,6,7,8,9,10]
>>> a[3:6]
[4, 5, 6]
>>> a[:7]
[1, 2, 3, 4, 5, 6, 7]
>>> a[2:]
[3, 4, 5, 6, 7, 8, 9, 10]
>>> s = a[:]
>>> s
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> s.remove(4)
>>> s
[1, 2, 3, 5, 6, 7, 8, 9, 10]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[-1]
10
>>> a[-3]
8
>>> a[-5:]
[6, 7, 8, 9, 10]
>>> a[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> a[1:8:2]
[2, 4, 6, 8]
>>> a[1:8:-2]
[]
>>> a[-8::-2]
[3, 1]
>>> a[-8::2]
[3, 5, 7, 9]
'''
