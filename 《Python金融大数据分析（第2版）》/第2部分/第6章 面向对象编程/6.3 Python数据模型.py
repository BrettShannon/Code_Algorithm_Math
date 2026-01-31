# 这一节还没搞明白，以后再说

# 特殊方法__init__(): 
# 构造函数,用于初始化类的实例,在创建对象时自动调用,可以接收任意数量的参数,但必须以self作为第一个参数,表示实例本身。

class Vector: # Vector是类名，类名首字母要大写，这是约定俗成的。
    def __init__(self, x=0, y=0, z=0): 
        self.x = x
        self.y = y
        self.z = z
# 上面这段代码定义了一个类，类名是Vector，类名首字母要大写，这是约定俗成的。

v = Vector(1, 2, 3) # 实例化一个对象，并赋值给变量v
print(v)
# 输出：<__main__.Vector object at 0x000001C7B8E9C860>，这是对象的内存地址。

print()


# 特殊方法：__repr__(): 用于返回对象的字符串表示形式，通常用于调试和日志记录。

class Vector(Vector): # Vector是类名，类名首字母要大写，这是约定俗成的。
    # class Vector(Vector):表示Vector是Vector的子类。
    def __repr__(self): 
        return 'Vector(%r, %r, %r)' % (self.x, self.y, self.z)
v = Vector(1, 2, 3) # 实例化一个对象，并赋值给变量v
print(v)
# 输出：Vector(1, 2, 3)，这是对象的字符串表示形式。

print()

#ab()和bool()的
# 特殊方法：__bool__(): 用于返回对象的布尔值，通常用于条件判断。
# 特殊方法：__abs__(): 用于返回对象的绝对值，通常用于数学运算。

class Vector(Vector): # Vector是类名，类名首字母要大写，这是约定俗成的。
    def __abs__(self): 
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __bool__(self):
        return bool(abs(self))
    
v = Vector(1, 2, -1) # 实例化一个对象，并赋值给变量v

print(abs(v))
# 输出：2.23606797749979，这是对象的绝对值。

print(bool(v))
# 输出：True，这是对象的布尔值。

print()

v = Vector() # 这行意思是实例化一个对象，并赋值给变量v，但是没有给对象赋值，所以对象的x、y、z都是0。
print(v)
# 输出：Vector(0, 0, 0)，这是对象的字符串表示形式。

print(abs(v))
# 输出：0.0，这是对象的绝对值。

print(bool(v))
# 输出：False，这是对象的布尔值。

print()

# 特殊方法：__add__(): 用于返回两个对象的和，通常用于数学运算。
# 特殊方法： __mul__(): 用于返回两个对象的乘积，通常用于数学运算。

class Vector(Vector): # Vector是类名，类名首字母要大写，这是约定俗成的。
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)
    
    def __mul__(self, scalar): # scalar是标量，即一个数。
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

v = Vector(1, 2, 3) # 实例化一个对象，并赋值给变量v1

print(v + Vector(2, 3, 4)) # 输出：Vector(3, 5, 7)，这是对象的和。

print(v * 2) # 输出：Vector(2, 4, 6)，这是对象的乘积。

print()

# 特殊方法：__getitem__(): 用于返回对象的某个元素，通常用于索引和切片操作。

class Vector(Vector): # Vector是类名，类名首字母要大写，这是约定俗成的。
    def __len__(self):
        return 3            # 返回对象的长度，即元素的个数，这里返回3，表示对象有三个元素。

    def __getitem__(self, index):
        if i in [0, -3]:
            return self.x
        elif i in [1, -2]:
            return self.y
        elif i in [2, -1]:
            return self.z
        else:
            raise IndexError('Invalid index')
# def __getitem__(self, index):表示定义了一个特殊方法，用于返回对象的某个元素，
# 通常用于索引和切片操作,index是索引值，可以是整数或切片对象,
# 这里index可以是0、1、2、-3、-2、-1，分别表示对象的第一个、第二个、第三个元素和最后一个元素。
# 如果index不是这些值，就会抛出IndexError异常。

v = Vector(1, 2, 3) # 实例化一个对象，并赋值给变量v1

print(len(v)) # 输出：3，这是对象的长度。

print(v[0]) # 输出：1，这是对象的第一个元素。

print(v[-2]) # 输出：2，这是对象的倒数第二个元素。

print(v[3]) # 输出：IndexError: Invalid index，这是对象的第四个元素，但是对象只有三个元素，所以会抛出IndexError异常。

print()

# 特殊方法： __iter__(): 用于返回对象的迭代器，通常用于循环操作。

class Vector(Vector):
    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

v = Vector(1, 2, 3) # 实例化一个对象，并赋值给变量v1

for i in range(3):
    print(v[i])
# 输出：
# 1
# 2
# 3
# 这是对象的迭代器，用于循环操作。

for coodinate in v:
    print(coordinate)
# 输出：
# 1
# 2
# 3
# 这是对象的迭代器，用于循环操作。


    