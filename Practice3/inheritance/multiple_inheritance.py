class A:
    def method_a(self):
        print("Method A")
class B:
    def method_b(self):
        print("Method B")
class C(A, B):
    pass
obj = C()
obj.method_a()
obj.method_b()

# (Method Resolution Order)
class A:
    def greet(self):
        print("Hello from A")
class B:
    def greet(self):
        print("Hello from B")
class C(A, B):
    pass
obj = C()
obj.greet()

class A:
    def show(self):
        print("A")
class B:
    def show(self):
        print("B")
class C(A, B):
    def show(self):
        super().show()
        print("C")

obj = C()
obj.show()

class A:
    def __init__(self):
        print("Init A")
class B:
    def __init__(self):
        print("Init B")
class C(A, B):
    def __init__(self):
        super().__init__()
        print("Init C")

obj = C()

class A:
    def __init__(self):
        print("Init A")
        super().__init__()
class B(A):
    def __init__(self):
        print("Init B")
        super().__init__()
class C(A):
    def __init__(self):
        print("Init C")
        super().__init__()
class D(B, C):
    def __init__(self):
        print("Init D")
        super().__init__()

obj = D()
