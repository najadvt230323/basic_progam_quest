class student:
    name="anu"
    age=25
    marks=89

s1=student()
print(s1.name)
print(s1.age)
print(s1.marks)

class student1:
    def details(self,name,age,marks):
        self.n=name
        self.a=age
        self.m=marks
    def display(self):
        print("name : ",self.n)
        print("age : ",self.a)
        print("marks : ",self.m)

name=input("enter th name : ")
age=int(input("enter th age : "))
marks=int(input("enter th marks : "))

std=student1()
std.details(name,age,marks)
std.display()

