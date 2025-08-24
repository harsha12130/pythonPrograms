#program to demonstrate Method Resolution Order(MRO)

class A:
    def display1(self):
        print("In class A Display method")

class B(A):
   
    def display2(self):
        print("In class B Display method")

class C(A):
    def display3(self):
        print("In class C Display method")

class D(B,C):
    def display4(self):
        print("In class D Display method")

print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
