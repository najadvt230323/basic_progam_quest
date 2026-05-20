# Inheritance
# ----------------------
# 1. single Inheritance
# ------------------------------
class Animal:

    def eat(self):
        print("eating.......")

    def sleep(self):
        print("sleeping.......")
    
class Dog(Animal):
    def run(self):
        print("running........")

arjun=Dog()
arjun.eat()                             #output : eating.......
arjun.sleep()                           #output : sleeping.......
arjun.run()                             #output : running........

# ----------------------------------------------------------
print()
class person:
    def __init__(self,name,age):
        print("calling parent constructor.....")
        self.name=name
        self.age=age

class student(person):
    def st_details(self, st_id, course, trainer):
        print("calling chide constructor.....")
        self.st_id=st_id
        self.course=course
        self.trainer=trainer

richu=student("richu","pyton")                      #output : calling parent constructor.....

# ---------------------------------------------------------------------------------------------

print()
class person:
    def __init__(self,name,age):
        print("calling parent constructor.....")
        self.name=name
        self.age=age
    def details(self):
        print(f"name : {self.name} \nage : {self.age}")

class student(person):
    def __init__(self, st_id, course, trainer):
        print("calling chide constructor.....")
        self.st_id=st_id
        self.course=course
        self.trainer=trainer

# richu=student("richu","pyton")                #TypeError: student.__init__() missing 1 required positional argument: 'trainer'
richu=student("richu","pyton","sreeraj")        # #output : calling chide constructor.....
       
# ------------------------------------------------------------------------------------------------------
print()
class person:
    def __init__(self,name,age):
        print("calling parent constructor.....")
        self.name=name
        self.age=age
    def details(self):
        print(f"name : {self.name} \nage : {self.age}")

class student(person):
    def __init__(self, name, age, st_id, course, trainer):
        super().__init__(name, age)
        print("calling chide constructor.....")
        self.st_id=st_id
        self.course=course
        self.trainer=trainer
    # def details(self):
    #     print(f"name : {self.name} \nage : {self.age} \nst_id : {self.st_id} \ncourse : {self.course} \ntrainer : {self.trainer}")
    def details(self):
        super().details()
        print(f"name : {self.name} \nage : {self.age} \nst_id : {self.st_id} \ncourse : {self.course} \ntrainer : {self.trainer}")

richu=student("richu",23,102,"python","sreeraj")
# richu.details()                        # output : name : richu 
#                                                 # age : 23 
#                                                 # st_id : 102 
#                                                 # course : python 
#                                                 # trainer : sreeraj

richu.details()                        # output : name : richu 
                                                # age : 23 
                                                # name : richu 
                                                # age : 23
                                                # st_id : 102 
                                                # course : python 
                                                # trainer : sreeraj

# -----------------------------------------------------------------------------------------

# 2.multpil Inheritance
# ----------------------------

print()
class Vehicle:
    def start(self):
        print("vehicle can start")

class car(Vehicle):
    def horn(self):
        print("horn......")
    
class Ev(car):
   def brik(self):
        print("brik......")

nexa =Ev()
nexa.horn()
nexa.start
# ------------------------------------------------------------------

print()
class Vehicle:
    def brik(self):
        print("vehicle can start")

class car(Vehicle):
    def brik(self):
        super().brik()
        print("horn......")
    
class Ev(car):
    def brik(self):
        super().brik()
        print("brik......")

nexa =Ev()
nexa.brik()
# --------------------------------------------------------------






