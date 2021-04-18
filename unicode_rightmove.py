#这个函数可以得到32位int溢出结果，因为python的int一旦超过宽度就会自动转为long，永远不会溢出，有的结果却需要溢出的int作为参数继续参与运算
def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val
#无符号右移
import ctypes
def unsigned_right_shitf(n,i):
    # 数字小于0，则转为32位无符号uint
    if n<0:
        n = ctypes.c_uint32(n).value
    # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
    if i<0:
        return -int_overflow(n << abs(i))
    #print(n)
    return int_overflow(n >> i)

'''ret = unsigned_right_shitf(-1,20)
print(ret)'''
