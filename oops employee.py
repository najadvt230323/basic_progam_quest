class employe:
    def details(self,name,age,salary,year):
        self.n=name
        self.a=age
        self.s=salary
        self.y=year
    def disply(self):
        print("name : ",self.n)
        print("age : ",self.a)
        print("old salary : ",self.s)
        print("experience in this company : ",self.y)
        print("new salary : ",self.ns)
    def increment(self,p):
        self.ns=self.s+(self.s*p/100)


name=input("enter the name : ")
age=int(input("enter the age : "))
sal=int(input("enter themcurrent salary : "))
exp=int(input("enter experience in this company : "))
emp=employe()
emp.details(name,age,sal,exp)
if exp<=3:
    emp.increment(10)
elif exp<=5:
    emp.increment(20)
elif exp<=8:
    emp.increment(30)
elif exp<=10:
    emp.increment(40)
else:
    emp.increment(50)

emp.disply()


