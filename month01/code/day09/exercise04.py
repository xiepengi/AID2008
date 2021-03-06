"""
    函数参数
        实参参数
            命名关键字形参
"""


# 命名关键字形参:
# 作用: 要求必须是关键字实参
# 写法1: 星号元组形参后面的位置形参是命名关键字形参
def func01(*args, p1, p2):
    print(args)
    print(p1)
    print(p2)


func01(1, 2, 3, p1=4, p2=5)
func01(p1=4, p2=5)
# func01(1, 2)


# 写法2: 星号后面的位置形参是命名关键字
# 注意: 星号不是参数, 只在修饰后面的参数是命名关键字形参
def func02(*, p1, p2=0):
    print(p1)
    print(p2)


# func02(1, 2)
func02(p1=1, p2=2)
print(1, 2, 3, 4, 5)
