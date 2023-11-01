import sys

a1 = True
b1 = False

print(sys.getsizeof(a1))
print(sys.getsizeof(b1))
# print(sys.getsizeof(b1))



a = 25  # 1 == True
b = 2.5
c = "text"
d = -2
a_ = 0  # 0 == False
b_ = 0.0
c_ = ""
d_ = None

print(bool(a))

print(bool(b))

print(bool(c))

print(bool(d))

print(bool(a_))

print(bool(b_))

print(bool(c_))
print(bool(d_))


print({True: "a", 1: "b", 1.0: "c"})
