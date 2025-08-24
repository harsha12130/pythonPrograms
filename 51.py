#program to demonstrate class and object

class Student:
    #properties
    #methods
    def read(self,x,y):
        self.sid=x
        self.sname=y
    def display(self):
        print(self.sid,self.sname)


s=Student()  #s is an object in Student class
id=int(input("Enter id="))
name=input("Enter name=")
s.read(id,name)
s.display()
