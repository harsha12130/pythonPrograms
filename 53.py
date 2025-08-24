#program to demonstrate parameterized constructor

class Student:
    def __init__(self,x,y):
        self.sid=x
        self.sname=y
    def display(self):
        print(self.sid,self.sname)

id=31771
name="Nikhil"
s1=Student(id,name)  #s1 is an object in Student class
s1.display()  
s2=Student(4654,"Surya")   #s2 is an object in Student class
s2.display()  
