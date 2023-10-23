import sys
from decimal import Decimal
import ctypes
import struct

# refcount
a = 1
b = a

lst = [1, 2, 3, 4]
lst1 = lst
# print(sys.getrefcount(a))
# print(sys.getrefcount(lst))

print(id(type(a)))

print(sys.getsizeof(a))
# print(sys.getsizeof(1.0))
# print(sys.getsizeof(Decimal(2)))

print(ctypes.string_at(id(a), 28))
print(struct.unpack('LLl', ctypes.string_at(id(a), 12)))

