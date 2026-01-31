# 26.slice()函数，切片，
# 返回一个切片对象，可以用于索引和切片操作，可以指定起始位置、结束位置和步长，默认步长为1，默认起始位置为0，
# 默认结束位置为列表长度，如果起始位置大于结束位置，则返回空列表。

numbers = [3, 4, 5, 6, 7, 8, 9, 10]
sliced = numbers[slice(2, 5)] # 从索引2开始，到索引5（不包括）结束，步长为1，默认步长为1，默认起始位置为0，默认结束位置为列表长度
print(sliced)
# 输出：[5, 6, 7]
#
#
# 27.ininstance()函数，判断一个对象是否是某个类的实例，返回一个布尔值。
# 语法：isinstance(object, classinfo)
# 参数：
# object：要判断的对象。
# classinfo：要判断的类或类的元组。
# 返回值：如果object是classinfo的实例，则返回True，否则返回False。
class Person:
    pass
person = Person()
print(isinstance(person, Person)) # 判断person是否是Person类的实例
# 输出：True
print(isinstance(person, str)) # 判断person是否是str类的实例
# 输出：False


# 28. callable()函数，判断一个对象是否是可调用的，返回一个布尔值。
# 语法：callable(object)
# 参数：
# object：要判断的对象。
# 返回值：如果object是可调用的，则返回True，否则返回False。
def hello():
    print("Hello, world!")
print(callable(hello)) # 判断hello是否是可调用的
# 输出：True

# 29. getattr()函数，获取一个对象的[属性值]，返回一个对象。
# 语法：getattr(object, name[, default])
# 参数：
# object：要获取属性的对象。
# name：要获取的属性名。
# default：如果属性不存在，则返回default，默认为None。
class Person:
    def __init__(self, name, age):
        self.name = name

    def say_hello(self):
        print("Hello, my name is", self.name)

person = Person("Alice", 20)
print(getattr(person, "name")) # 获取person对象的name属性值。
# 输出：Alice
print(getattr(person, "age")) # 获取person对象的age属性值，如果属性不存在，则返回None
# 输出：None
print(getattr(person, "age", 18)) # 获取person对象的age属性值，如果属性不存在，则返回18
# 输出：18
print(getattr(person, "say_hello")) # 获取person对象的say_hello方法
# 输出：<bound method Person.say_hello of <__main__.Person object at 0x000001234567890>>

# 30. setattr()函数，设置一个对象的属性值，返回一个对象。
# 语法：setattr(object, name, value)
# 参数：
# object：要设置属性的对象。
# name：要设置的属性名。
# value：要设置的属性值。
person = Person("Alice", 20)
setattr(person, "age", 30) # 设置person对象的age属性值为30
print(person.age) # 输出：30

setattr(person, "gender", "female") # 设置person对象的gender属性值为female
print(person.gender) # 输出：female

setattr(person, "say_hello", lambda: print("Hello, my name is", person.name)) # 设置person对象的say_hello方法为lambda表达式
person.say_hello() # 输出：Hello, my name is Alice

# 31. delattr()函数，删除一个对象的属性，返回一个对象。
# 语法：delattr(object, name)
# 参数：
# object：要删除属性的对象。
# name：要删除的属性名。
person = Person("Alice", 20)
delattr(person, "age") # 删除person对象的age属性
print(person.age) # 报错，因为age属性已经被删除了
