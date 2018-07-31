'''
Python 模块
'''

# 通常来说，同文件夹下的 py 文件可以直接 import
# 我们把下面这段代码保存到 hello.py
def print_hello():
    print('hello')

# 在 run.py 里import，然后调用 print_hello()
# 写法1：
import hello
hello.print_hello()

# 写法2：
from hello import print_hello
print_hello()


# 如果在不同的路径下面，可以在 sys.path 里手动加入你想 import 的路径
import sys
sys.path.append('/home/xxx/course')
import hello
hello.print_hello()


'''
包
一个目录，及其子目录组成一个包，可以看做是一个库。
通常在项目当中，我们采用的是包这个来组织引用关系。
并非通过不停的 sys.path.append('...') 添加引用路径来实现 import。
'''




