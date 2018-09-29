##### Python 函数基础 01 #####


# 1.1 基本函数样例
def summer(lis):
    '''
    这里是函数的说明文档，doc 的位置
    : param lis: 参数列表的说明
    : return: 返回值的说明
    '''

    total = 0
    for i in lis:
        total += i
    return total # return 几乎可以返回任意对象


# 1.2 接受返回值
def funcA():
    pass
    return 'something'
result = funcA()

def funcB():
    return 1, [2, 3], 'haha'
a, b, c = funcB() # 接受多个返回值


# 1.3 参数的传递
# i. Python 函数参数传递的是实际对象的内存地址
# ii. Python 函数参数传递的数据类型分为可变数据类型和不可变数据类型

# 1.3.1 参数传递不可变数据类型
a = 1
def funcC(a):
    print("在函数内部修改之前,变量a的内存地址为： %s" % id(a))
    # 这里的赋值动作，其实创建了一个新的对象 a
    a = 2
    print("在函数内部修改之后,变量a的内存地址为： %s" % id(a))
    print("函数内部的a为： %s" % a)

print("调用函数之前,变量a的内存地址为： %s" % id(a))
funcC(a)
print("函数外部的a为：%s" % a)
# 以上例子可以将函数 func(a) 中的 a 换为 b ，更加容易理解，其执行结果是一样的
# 一般函数内部的参数名称定义的和，函数外部的变量名称相同时一个不好的习惯！容易混淆思维，发生错误！


# 1.3.2 参数传递可变数据类型
a = [1, 2, 3]
def funcD(b):
    print("在函数内部修改之前,变量b的内存地址为： %s" % id(b))
    b.append(4)
    print("在函数内部修改之后,变量b的内存地址为： %s" % id(b))
    print("函数内部的b为： %s" % b)

print("调用函数之前,变量a的内存地址为： %s" % id(a))
funcD(a)
print("函数外部的a为：%s" % a)


# 1.4 函数的四种参数类型

# 1.4.1 位置参数

# 1.4.2 默认参数
# 默认参数必须在位置参数后面！
# 使用参数名传递参数，可以不考虑参数的位置
# 默认参数尽量指向不变的对象！
def funcE(b, a=None):
    # 注意下面的if语句
    if a is None:
        a = []
    a.append("A")
    return a

print(funcE('test'))
print(funcE('test'))
print(funcE('test'))

# 1.4.3 动态参数
#
# *args 表示接受任意数量个参数，调用时，会将实参打包为一个 Tuple 传给形参
# 如果是一个列表，会当成一个参数传入。解决方法是前面加上 *，以 func(*lis) 传入
# 如果是一个字典，func(*dict) 则是会，将所有 key 逐一传递进去
#
# **kwargs 表示接受键值对的动态参数，数量任意。
# 调用的时候，会将实际参数打包成字典。
# 直接将字典实参，传递给 **kwargs 会直接报错
# 解决的方法是 func(**dict)
# 
# 需要注意的是，*args必须出现在**kwargs之前。
# 动态参数，必须放在所有的位置参数和默认参数后面！

def funcF(a, b, c=1, *args, **kwargs):
    print('c的值是:', c)
    for arg in args:
        print(arg)

    for kwg in kwargs:
        print(kwg, kwargs[kwg])

lis = ['aaa', 'bbb', 'ccc']
dic = {
    'k1': 'v1',
    'k2': 'v2'
}

funcF(1, 2, *lis, **dic)

# 1.4.4 关键字参数
# Python 参数传递方式，虽然灵活性很大，但是风险也很大，可控性差，必须自己对参数进行过滤和判定。
# 关键字参数可以在一定程度上缓解这种矛盾
#
# 关键字参数前面需要一个特殊分隔符 * 和位置参数及默认参数分隔开来，*后面的参数被视为关键字参数。
# 在函数调用时，关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错。
# 不同于默认参数，关键字参数必须传递，但是关键字参数也可以有缺省值，这时就可以不传递了，从而简化调用。

# 示例1：
def studentA(name, age, *, sex):
    pass

studentA(name="jack", age=18, sex='male')

# 示例2：
# 如果函数定义中已经有了一个*args参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了。
def studentB(name, age=10, *args, sex, classroom, **kwargs):
    pass

studentB(name="jack", age=18, sex='male', classroom="202", k1="v1")

# 1.5 变量作用域
# Python的作用域一共有4层，分别是：
# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内建作用域
#
# 以 L –> E –> G –>B 的规则查找变量

# 示例1：
a = 1
print("函数outer调用之前全局变量a的内存地址： ", id(a))

def outer1():
    a = 2
    print("函数outer调用之时闭包外部的变量a的内存地址： ", id(a))
    def inner():
        a = 3
        print("函数inner调用之后闭包内部变量a的内存地址： ", id(a))
    inner()
    print("函数inner调用之后，闭包外部的变量a的内存地址： ", id(a))
outer1()
print("函数outer执行完毕，全局变量a的内存地址： ", id(a))

# 示例2：
a = 1
print("函数outer调用之前全局变量a的内存地址： ", id(a))
def outer2():
    a = 2
    print("函数outer调用之时闭包外部的变量a的内存地址： ", id(a))
    def inner():
        global a   # 注意这行
        a = 3
        print("函数inner调用之后闭包内部变量a的内存地址： ", id(a))
    inner()
    print("函数inner调用之后，闭包外部的变量a的内存地址： ", id(a))
outer2()
print("函数outer执行完毕，全局变量a的内存地址： ", id(a))

# 示例3：
a = 1
print("函数outer调用之前全局变量a的内存地址： ", id(a))
def outer3():
    a = 2
    print("函数outer调用之时闭包外部的变量a的内存地址： ", id(a))
    def inner():
        nonlocal a   # 注意这行
        a = 3
        print("函数inner调用之后闭包内部变量a的内存地址： ", id(a))
    inner()
    print("函数inner调用之后，闭包外部的变量a的内存地址： ", id(a))
outer3()
print("函数outer执行完毕，全局变量a的内存地址： ", id(a))
