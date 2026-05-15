class Student:
    def exam(self):
        print("exam conducted on 11-05-26")
    def study(self,name):
        self.n=name
        print(f"hi {self.n}")

print(type(Student))

richu=Student()
print(type(richu))
print(id(richu))

shabin=Student()
print(type(shabin))
print(id(shabin))

print()
richu.exam()
richu.study("najad")
# --------------------------------------------------
class Student1 :
    school="quest"

richu=Student1()
najad=Student1()

print(Student1.school)
print(Student1().school)
print(richu.school)
print(najad.school)

print()
Student1.school="quest inovashion"
print(Student1.school)
print(richu.school)
print(najad.school)

print()
richu.school="kunnamagalam hss"
print(Student1.school)
print(richu.school)
print(najad.school)

print()
del richu.school
print(Student1.school)
print(richu.school)
print(najad.school)


print()
richu.school="kunnamagalam hss"
del Student1.school
# print(Student1.school)           # AttributeError: type object 'Student1' has no attribute 'school'
print(richu.school)                # kunnamagalam hss
# print(najad.school)                # AttributeError: 'Student1' object has no attribute 'school'

print()
Student1.school = "quest"
print(Student1.school)
print(richu.school)
print(najad.school)

# ---------------------------------------------------------------

print()
class Student2 :
    school="quest"
    def __init__(self):
        print("hi self")

richu=Student2()
najad=Student2()

# -------------------------------------------------------------------

print()
class Student3 :
    school="quest"
    def __init__(self,roll_no,name,age):
        print("hi Student3 class")
        self.a=roll_no
        self.b=name
        self.c=age
    def details(self):
        print()
        print(self.a)
        print(self.b)
        print(self.c)
        

# richu=Student3()                  #ypeError: Student3.__init__() missing 3 required positional arguments: 'roll_no', 'name', and 'age'
najad=Student3(5,"najad",25)
richu=Student3(name="richu",age=25,roll_no=10)

print()
print(najad.a,"  ",najad.b,"  ",najad.c)
print(richu.a,"  ",richu.b,"  ",richu.c)
print()
najad.details()
richu.details()

# -------------------------------------------------------

print()
class Employee:
    company="quest"
    branch="calicut"
    def __init__(self,a,b,c,d):
        self.emp_id=a
        self.emp_name=b
        self.emp_salary=c
        self.emp_email=d
    def details(self):
        print(f"emp_id : {self.emp_id}\nemp_name : {self.emp_name}\nemp_salary : {self.emp_salary}\nemp_email : {self.emp_email}")
        print()
    def update(self):
        if self.emp_salary>10000 :
            self.emp_salary=self.emp_salary+self.emp_salary*0.15
    def resin(self):
        self.company = "filpkart"
        self.branch = "kochi"
        self.emp_id = 101
        self.emp_salary=150000


richu=Employee(10,"richu",15000,"richu.com")
print(richu.company,"   ",richu.branch)
richu.details()
najad=Employee(15,"najad",350000,"najad.com")
najad.details()

najad.update()
najad.details()

najad.resin()
print(najad.company)
print(najad.branch)
najad.details()

# ----------------------------------------------------------------------------
      






