'''
# 下面这段代码可以打印：
class FinancialInstrument(object):  # object是所有类的基类
    pass # pass是空语句，占位符

fi = FinancialInstrument()  # 实例化

print(type(fi)) # <type 'instance'> instance是实例
print()

print(fi) # <__main__.FinancialInstrument object at 0x0000020A4E9F8E80> object at 0x0000020A4E9F8E80是对象的内存地址
print()

print(fi.__str__()) # .__str__()是默认的打印输出，如果没有定义，则调用object的__str__()方法
print()

fi.price = 100 # .price是属性，如果没有定义，则自动创建
print(fi.price) # .price是属性，如果没有定义，则返回None
'''

# ------------------- #
# 关于__init__：

class FinancialInstrument(object): # object作用是让类继承object类
    author = 'Zhang' # .author是类属性，如果没有定义，则返回None
    def __init__(self, symbol, price): # __init__()是构造函数，用于初始化对象,self是对象本身
        self.symbol = symbol
        self.price = price
'''
print(FinancialInstrument.author) # .author是类属性，如果没有定义，则返回None
# 输出：Zhang
print()

aapl = FinancialInstrument('AAPL', 100) # aapl是对象
print(aapl.symbol) # .symbol是对象属性，如果没有定义，则返回None
# 输出：AAPL
print()

print(aapl.author) # .author是类属性，如果没有定义，则返回None
# 输出：Zhang
# ‼️aapl.author 和 FinancialInstrument.author 是同一个属性，因为它们指向同一个内存地址
print()


# 👇 更改实例属性
aapl.price = 105 # .price是属性，如果没有定义，则自动创建
print(aapl.price) # .price是对象属性，如果没有定义，则返回None
# 输出：105
print()

print(FinancialInstrument.author) # .author是类属性，如果没有定义，则返回None
# 输出：Zhang
print()
'''

# ------------------- #

# 在类定义中引入封装（意思是将属性和方法封装在类中，使其对外不可见（AI））：
'''
class FinancialInstrument(FinancialInstrument):  # 继承了FinancialInstrument前一版本的类
                                # FinancialInstrument是父类，FinancialInstrument是子类
                                # 父类和子类的名称相同是因为子类继承了父类的所有属性和方法
    def get_price(self):        # .get_price()是方法，如果没有定义，则返回None
        return self.price       # .price是对象属性，如果没有定义，则返回None
    def set_price(self, price):    # .set_price()是方法，如果没有定义，则返回None
        self.price = price
        # self.__price = price      # .__price是私有属性，只能在类内部访问
    
fi = FinancialInstrument('AAPL', 100)   # fi是实例
print(fi.get_price())   # 输出：100
print()

fi.set_price(105)       # 将fi.price的值设置为105
print(fi.get_price())   # 输出：105
print()

print(fi.price)     # 输出：105
'''

# 私有实例属性：  # 私有属性只能在类内部访问，不能在类外部访问  
# 私有属性（在类外部）以双下划线开头
# 私有属性在类内部以单下划线开头


class FinancialInstrument(object):
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.__price = price
    def get_price(self):  # get_price的作用是获取私有属性__price的值
        return self.__price
    def set_price(self, price): # set_price的作用是设置私有属性__price的值
        self.__price = price

fi = FinancialInstrument('AAPL', 100)
print(fi.get_price())    # 输出：100
print()

print(fi.__price) 
# 输出：AttributeError: 'FinancialInstrument' object has no attribute '__price',
# ‼️ 因为__price是私有属性，只能在类内部访问
print()

print(fi._FinancialInstrument__price)
# 输出：100
# ‼️ 因为__price是私有属性，只能在类内部访问，但是可以通过类名._类名__属性名来访问
print()

fi._FinancialInstrument__price = 105
print(fi.get_price())
# 输出：105
# __price是私有属性，只能在类内部访问，但是可以通过类名._类名__属性名来访问
print()

fi.set_price(100) # 将fi.__price的值设置为100
print(fi.get_price())
# 输出：100
print()


# ------------------- #
# PortfolioPosition类 以_FinancialInstrument类 的一个实例作为属性：

# 👇这段关于“计算头寸价值”的代码没整明白，没修改对，以后再说吧
# 最后有DS对这段代码的修改

class PortfolioPosition(object):
    def __init__(self, financial_instrument, position_size): 
                    # financial_instrument 意思是金融工具，即具体的投资标的，position_size 意思是头寸规模，即持有该资产的数量
        self.position = financial_instrument
        self.position_size = position_size
    def get_position_size(self): # get_position_size的作用是获取头寸规模
        return self.__position_size
    def update_position_size(self, position_size):  # update_position_size的作用是更新头寸规模
        self.__position_size = position_size
    def get_position_value(self): # get_position_value的作用是计算头寸价值
        return self.__position_size * self.position.get_price()
    
# fi = FinancialInstrument('AAPL', 100) # fi是实例

pp = PortfolioPosition(fi, 10)

print(pp.get_position_size()) # 
print()

print(pp.get_position_value())
print()

print(pp.position.get_price())
print()

pp.position.set_price(105)
print(pp.get_position_value())

'''
👆这段代码我看不懂他的金融计算层面的意义，帮我解释:
DS：
这段代码实现了一个投资组合头寸(PortfolioPosition)的基本功能，让我从金融计算的角度来解释：

核心概念解释
1. 投资组合头寸 (Portfolio Position)
【头寸：指投资者持有的某种金融资产的数量和方向】
头寸的意思是，投资者持有的某种金融资产的数量和方向。在这个例子中，头寸指的是持有AAPL股票的数量和方向。

头寸规模：持有该资产的数量（这里是10股）

金融工具：具体的投资标的（这里是AAPL股票）

2. 代码中的金融计算逻辑

# 创建金融工具实例：AAPL股票，价格100元
fi = FinancialInstrument('AAPL', 100)

# 创建头寸：持有10股AAPL
pp = PortfolioPosition(fi, 10)

计算过程：

# 获取头寸规模：10股
print(pp.get_position_size())  # 输出：10

# 计算头寸价值：10股 × 100元/股 = 1000元
print(pp.get_position_value())  # 输出：1000.0

# 获取当前股价
print(pp.position.get_price())  # 输出：100

# 股价涨到105元
pp.position.set_price(105)

# 重新计算头寸价值：10股 × 105元/股 = 1050元
print(pp.get_position_value())  # 输出：1050.0

3. 金融意义
头寸价值计算：

text
头寸价值 = 头寸规模 × 标的资产价格 

#‼️ 👆这个公式是金融计算中的基本公式，用于计算头寸的价值。
# 头寸规模是指投资者持有的某种金融资产的数量，标的资产价格是指该金融资产的价格。
# 例如，如果投资者持有10股AAPL股票，每股价格为100元，那么头寸价值就是1000元。

盈亏计算：

初始价值：1000元

新价值：1050元

盈利：50元（涨幅5%）

4. 实际应用场景
这种结构常用于：

投资组合管理：跟踪每个持仓的价值

风险监控：实时计算头寸暴露

盈亏计算：监控投资表现

资产配置：根据头寸价值调整仓位

5. 风险管理角度
头寸规模：决定风险暴露程度

价格变动：影响头寸价值和盈亏

集中度风险：单个头寸占组合比重

这是一个简化的投资组合管理模型，实际系统中还会包含更多功能如止损、杠杆、风险管理等。
'''

# DS对代码的修改：

class PortfolioPosition(object):   # PortfolioPosition 意思是投资组合头寸
    def __init__(self, financial_instrument, position_size):
        # financial_instrument 意思是金融工具，即具体的投资标的
        # position_size 意思是头寸规模，即持有该资产的数量
        self.position = financial_instrument
        self.__position_size = position_size  # 修复：使用双下划线属性
    
    def get_position_size(self):  # get_position_size的作用是获取头寸规模
        return self.__position_size
    
    def update_position_size(self, position_size):  # update_position_size的作用是更新头寸规模
        self.__position_size = position_size
    
    def get_position_value(self):  # get_position_value的作用是计算头寸价值
        return self.__position_size * self.position.get_price()

# 假设有一个FinancialInstrument类（需要先定义）
class FinancialInstrument:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.__price = price
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price

# 创建金融工具实例：AAPL股票，价格100元
fi = FinancialInstrument('AAPL', 100)

# 创建投资组合头寸：持有10股AAPL
pp = PortfolioPosition(fi, 10)

print("头寸规模:", pp.get_position_size())  # 获取头寸规模
# 输出：10
print()

print("头寸价值:", pp.get_position_value())  # 计算头寸价值
# 输出：1000.0
print()

print("当前股价:", pp.position.get_price())  # 获取当前股价
# 输出：100
print()

# 更新股价到105元
pp.position.set_price(105)
print("更新后的头寸价值:", pp.get_position_value())  # 重新计算头寸价值
# 输出：1050.0

# 演示更新头寸规模
print("\n--- 更新头寸规模演示 ---")
pp.update_position_size(15)  # 从10股增加到15股
print("新的头寸规模:", pp.get_position_size())
# 输出：15
print()
print("新的头寸价值:", pp.get_position_value())
# 输出：1575.0