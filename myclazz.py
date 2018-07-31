'''
用关键字 class 去定义一个类，如果没有指定父类，默认继承 object
'''

class Human(object):
    pass


'''
类属性
这个属性是和类绑定的，并不是和实例绑定的。
'''
class Human(object):
    speak = True


'''
实例属性
'''
class Human(object):
    def __init__(self, name):
        self.name = name

human_a = Human('alan')


'''
类方法
可以看成是一种类属性，而传入的第一个参数是 self，表示调用这个类方法的实例。
'''
class Human(object):
    def __init__(self, name):
        self.name = name
    def walk(self):
        print(self.name + ' is walking')
human_a = Human('alan')
human_a.walk()


'''
访问控制
从上面的例子来看，name 这个实例属性，可以被外部随意的更改。
如果不想让外部直接访问到，则在名字前加两个下划线 __name
这样从外部就无法访问了。

如果想要访问，可以加上 set() get() 的接口
'''
class Human(object):
    def __init__(self, name):
        self.__name = name
    def walk(self):
        print(self.__name + "is walking")
    def get_name(self):
        return self.__name
    def set_name(self, name):
        if len(name) <= 10:
            self.__name = name

human_a = Human('alan')
print(human_a.get_name())

human_a.set_name('bob')
print(human_a.get_name())


'''
继承
'''
class Man(Human):
    def __init__(self, name, has_wife):
        super(Man, self).__init__(name)
        self.__has_wife = has_wife
    def smoke(self):
        print('A man maybe smoke')
    def drink(self):
        print('A man maybe drink')

man = Man('tom', False)
man.smoke()
man.drink()

class Woman(Human):
    def __init__(self, name, has_husband):
        super(Woman, self).__init__(name)
        self.__has_husband = has_husband
    def shopping(self):
        print('A woman always go shopping')
    def make_up(self):
        print('A woman always make up')

woman = Woman('anna', False)
woman.shopping()
woman.make_up()