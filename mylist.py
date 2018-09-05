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
