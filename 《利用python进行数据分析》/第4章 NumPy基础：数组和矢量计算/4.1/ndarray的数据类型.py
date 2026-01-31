import  numpy as np

'''
arr_1 = np.array([1, 2, 3], dtype=np.float64) # float64是浮点数

arr_2 = np.array([1, 2, 3], dtype=np.int32) # int32是整数
# dtype是数据类型

print(arr_1.dtype)

print(arr_2.dtype)
'''

# 使用astype()函数转换数据类型
'''
arr = np.array([1, 2, 3, 4, 5])

print(arr.dtype)

float_arr = arr.astype(np.float64) # astype是转换数据类型

print(float_arr.dtype)
'''


'''
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])

print(arr)

arr_int = arr.astype(np.int32) # int32是整数
# 还有其他表示数据类型的符号，比如int64，float32，float64，
# bool，complex，str，object，uint8，uint16，uint32，uint64，
# int8，int16，int32，int64，float16，complex64，complex128

# 以上这些表示数据类型的符号，他们分别表示：
# float16 是16位浮点数，
# float32 是32位浮点数，
# float64 是64位浮点数，
# bool 是布尔值，
# complex 是复数，
# str 是字符串，
# object 是对象，
# uint8 是8位无符号整数，
# uint16 是16位无符号整数，
# uint32 是32位无符号整数，
# uint64 是64位无符号整数，
# int8 是8位整数，
# int16 是16位整数，
# int32 是32位整数，
# int64 是 64位整数，
# complex64 是64位复数，
# complex128 是128位复数。


print(arr_int)
print(arr_int.dtype)
'''

'''
int_array = np.arange(10)
print(int_array)
print(int_array.dtype)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)

int_array.astype(calibers.dtype) # 这行代码的作用是将int_array的数据类型转换为calibers的数据类型

print(int_array.dtype)
'''

# 用简洁的类型代码来表示dtype：
empty_unit32 = np.empty(8, dtype='u4') # u4表示uint32, np.empty是创建一个指定形状和数据类型的空数组

print(empty_unit32)