'''
Dict
python 内置的一种数据结构
无序
可更改
'''
name = {1:"aaa", 2:"bbb", 3:"ccc"}
print(name)

# 判断是否包含特定的 Key
print(5 in name)
print(1 in name)

# 增
name[8] = "xxx"
print(name)

# 删
name.pop(8)
print(name)

# 改
name[2] = "zzz"
print(name)

# 查
print(name[2])
print(name.get(5))
print(name.get(5, "default_key"))

# 获取所有 keys
print(name.keys())

# 获取所有 values
print(name.values())

# 获取所有 元素
print(name.items())