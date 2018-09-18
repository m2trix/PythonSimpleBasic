import os          # 1

print('<[1]> time module start')        # 2

class ClassOne():
    print('<[2]> ClassOne body')            # 3

    def __init__(self):                     # 10
        print('<[3]> ClassOne.__init__')

    def __del__(self):
        print('<[4]> ClassOne.__del__')     # 101

    def method_x(self):                     # 12
        print('<[5]> ClassOne.method_x')

    class ClassTwo(object):
        print('<[6]> ClassTwo body')        # 4

        def __init__(self):
            print('<[6.1]> ClassTwo.__init__')

        def __del__(self):
            print('<[6.2]> ClassTwo.__del__')

class ClassThree():
    print('<[7]> ClassThree body')          # 5

    def __init__(self):
        print('<[7.1]> ClassThree.__init__')

    def __del__(self):
        print('<[7.2]> ClassThree.__del__')

    def method_y(self):                     # 16
        print('<[8]> ClassThree.method_y')  

class ClassFour(ClassThree):
    print('<[9]> ClassFour body')           # 6

    def __init__(self):
        print('<[9.1]> ClassFour.__init__')

    def __del__(self):
        print('<[9.2]> ClassFour.__del__')

def func():
    print("<func> function func")

'''
很多时候，模块或者说脚本会像一个标准的程序样直接运行，也就是类似python test.py这种方式，
在这种情况下, __name__ 的值将是一个特别缺省值"__main__"。

根据上面的特性，可以用if __name__ == '__main__'来判断是否是在直接运行该py文件！
如果是，那么if代码块下的语句就会被执行，如果不是，就不执行。
该方法常用于对模块进行测试和调试，区分直接运行和被导入两种情况的不同执行方式！
'''
if __name__ == '__main__':                      # 7
    print('<[11]> ClassOne tests', 30 * '.')    # 8
    one = ClassOne()                            # 9
    one.method_x()                              # 11
    print('<[12]> ClassThree tests', 30 * '.')  # 13
    three = ClassThree()                        # 14
    three.method_y()                            # 15
    print('<[13]> ClassFour tests', 30 * '.')  # 17
    four = ClassFour()
    four.method_y()

print('<[14]> evaltime module end')             # 100