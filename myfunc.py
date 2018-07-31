# 无参数
def print_hello():
    print('hello')
print_hello()

# 带参数
def print_str(s):
    print(s)
    return(s*2)
print_str('biubiu')
print(print_str('oops'))

# 带默认参数
def print_default(s='default_value'):
    print(s)
print_default()
print_default('haha')

# 不定长参数
def print_args(s, *arg):
    print(s)
    for a in arg:
        print(a)
    return
print_args('hello')
print_args('hello', 'world', '1')

# 参数次序可变
def print_two(a, b):
    print(a + ", " + b)
print_two(a='a', b='b')
print_two(b='b', a='a')