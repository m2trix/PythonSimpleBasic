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

game.pop(1)
print(game)

# 改
game[2] = "bbb"
print(game)

# 查
print(game[0])
print(game[1])
print(game[2])