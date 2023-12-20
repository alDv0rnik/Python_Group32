"""
Define two classes A and B with parameters a and b respectively.
Define class C inherited from both classes.
Try to call parent attributes from child classes
"""


class A:
    def __init__(self):
        self.a = 10


class B:
    def __init__(self):
        self.b = 20


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)


a = A()
b = B()
c = C()

print(c.a)
print(c.b)
