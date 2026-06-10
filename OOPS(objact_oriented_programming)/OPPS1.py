#================simple definition class=========================
# class MyClass:
#     pass

# obj = MyClass()
# print(obj)
# print(type(obj))

#==================class with methods===========================
# class MyName:
#     def displayname(self):
#         print("My name is sreeraj.")

# obj = MyName()
# obj.displayname()

#==============class with attributes and methods=====================
# class SmartPhone:

#     def __init__(self,ram,rom,price):
#         self.ram = ram
#         self.rom = rom
#         self.price = price

#     def display_details(self):
#         print(f"Ram :{self.ram}\nRom : {self.rom}\nPrice : {self.price}")

# iphone = SmartPhone(12,128,149999)
# iphone.display_details()
# print(iphone.ram)
# print(iphone.rom)
# print(iphone.price)


# s24 = SmartPhone(12,256,125999)
# s24.display_details()


#========================class and instance variable==================================

# class Employee:
#     company_name = "Quest Innovative Solutions"

#     def __init__(self,name,salary):#Instance reference / Instance parameter
#         self.name = name    #instance variable
#         self.salary = salary#instance variable

#     def show_details(self):
#         #accessing class variables from instance method
#         print("Comapany : ",self.company_name)

#         #accessing instance variables
#         print("Name : ",self.name)
#         print("Salary  : ",self.salary)

# emp1 = Employee("Sreeraj",15000)
# emp2 = Employee("Keerthana",25000)

# emp1.show_details()
# emp2.show_details()
# print(Employee.company_name)
# print(emp1.company_name)

# print(emp1.name)
# print(emp1.salary)

# print(Employee.name)

#----------updating class variable----------
# Employee.company_name = "QIS Accademey"

# emp1.show_details()

#----------deleting class variable-----------
# del Employee.company_name
# print(Employee.company_name)

# emp1.company_name='ABC'
# emp1.show_details()
# del emp1.company_name
# emp1.show_details()

#--------deleting instance variable-------------
# del emp1.salary
# print(emp1.salary)

# emp1.__dict__.clear()
# print(emp1.name)


#=========================constructors===================================
#1. default 
"""In a default constructor, self is the only parameter."""
# class Mobile:
#     def __init__(self):
#         self.brand = "Samsung"
#         self.price = 15000

# m1 = Mobile()
# print(m1.brand, m1.price)

#2.parameterized
# class Mobile:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

# m1 = Mobile("iPhone", 70000)
# m2 = Mobile("OnePlus", 40000)

# print(m1.brand, m1.price)
# print(m2.brand, m2.price)

##### constructor
## Constructor is a special function or method which creates objects
## Constructor is use to allocating memory space for object variables
#  __init__() special methods represent using the underscore
### 1)default,2)parameterized,3)copy




# class Bird:
#     eyes=2
#     def __init__(self):
#         print("Hello")

#     def fly(self,a):
#         self.a=a   
#         print("Fly",a)

#     def eat(self):
#         print("eating",self.a)    

# parrot=Bird()














# class Bird:
#     eyes=2


#     def __init__(self):
#         print("Hello")

#     def fly(self,a):
#         self.a=a   ## creating instance variable
#         print("Fly",a)

#     def eat(self):
#         print("eating",self.a)    


# parrot=Bird()
# print(parrot.eyes)
 
# parrot.eyes-=1
# print(parrot.eyes) 

# peacock=Bird()
# print(peacock.eyes)

# parrot.fly("parrot")
# peacock.fly("peacock")


# parrot.eat()
# peacock.eat()




#### parameterized
# class Bird:
#     eyes=2

#     def __init__(self,a):
#         print("Hello",a)   

# parrot=Bird(10)







# class Car:
#     wheels=4  

# car1=Car()
# car2=Car()

# Car.wheels=6

# print("Car 1 wheels:",car1.wheels)
# print("Car 2 wheels:",car2.wheels)








# class Dog:
#     species="Canine"   

#     def __init__(self,name):
#         self.name=name  

# dog1=Dog("Jangoo")
# dog2=Dog("Bruno")

# dog1.species="German Shepherd"

# print("Dog1:",dog1.name,"-",dog1.species)
# print("Dog2:",dog2.name,"-",dog2.species)







# class HousePlan:
#     def __init__(self, cement, stone, sand, water):
#         self.cement = cement
#         self.stone = stone
#         self.sand = sand
#         self.water = water

#     def protection(self):
#         print("This house is strong and well-protected because it’s built using:")
#         print(f"Cement: {self.cement} bags, Stone: {self.stone} kg, Sand: {self.sand} kg, Water: {self.water} liters.")

#     def parking_car(self):
#         print("The house has a parking area for cars.")

#     def cook(self):
#         print("Cooking can be done in the modern kitchen.")

# # Creating an object
# kochi = HousePlan(cement=50, stone=200, sand=150, water=100)

# # Calling the methods
# kochi.protection()
# kochi.parking_car()
# kochi.cook()


# kollam = HousePlan(cement=100, stone=300, sand=250, water=200)     
# kollam.protection()
# kollam.parking_car()
# kollam.cook()  








# class shop:
#     shopname="Abcd"
#     owner="das"
#     def __init__(self,id,name,salary):  #constructor with 3 arg
#         self.emp_id=id
#         self.emp_name=name
#         self.emp_salary=salary
# obj1=shop(101,"Arun",50000) 
# obj2=shop(102,"Anu",25000)  






# class shop:
#     shopname="Abcd"
#     owner="das"
#     def __init__(obj1,id,name,salary):  
#         obj1.emp_id=id
#         obj1.emp_name=name
#         obj1.emp_salary=salary
# obj1=shop(101,"Arun",50000) 






# class Student:
#     school_name="Gthss"

#     def __init__(self,name,roll_no,age):
#         self.name=name
#         self.roll_no=roll_no
#         self.age=age

#     def display(self):
#         print(f"Name:{self.name}")  
#         print(f"Roll no:{self.roll_no}")
#         print(f"Age:{self.age}")
#         print(f"School name:{Student.school_name}")

# s1=Student("Arun",101,24)
# s1.display()









# class Student:
#     def __init__(self,name,subjects):
#         self.name=name
#         self.subjects=subjects  

#     def display(self):
#         print(f"Name:{self.name}")
#         print(f"Subjects:{self.subjects}")    

# s1=Student("Arun",["Maths","Biology","Chemistry"])
# s2=Student("Gokul",["Physics","CS"])
# s1.display()
# print("____________")
# s2.display()
##### default argument

# class MyClass:
#     def __init__(self,value=0):  
#         self.data=value

# obj1=MyClass(100)
# print("obj1.data:",obj1.data)

# obj2=MyClass()
# print("obj2.data:",obj2.data)





# class Calculator:
#     def __init__(self,a=0,b=0):
#         self.a=a
#         self.b=b

#     def add(self):
#         return self.a+self.b

#     def multiply(self):
#         return self.a*self.b

# calc1=Calculator(10,20)
# print("sum:",calc1.add())
# print("product:",calc1.multiply())

# print("---------------------------------")

# calc2=Calculator(5)  
# print("sum:",calc2.add())
# print("product:",calc2.multiply())

# # print("---------------------------------")

# calc3=Calculator()    
# print("sum:",calc3.add())
# print("product:",calc3.multiply())



###########Method with parameters

# class Student:
#     def __init__(self,name):
#         self.name=name

#     def greet(self,message):
#         print("Message from :",self.name)
#         print(message)

# s1 = Student("Anu")
# s1.greet("Good morning!")









# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def add_marks(self,mark1,mark2):
#         total=mark1+mark2
#         print(f"{self.name}'s total marks:{total}")

# s1=Student("Arun",18)
# s1.add_marks(45,50)

        






#### copy const
# it is a constructor that creates an object using another object of the same class
# a copy constructor is not built-in like in languages such as C++ —
# but you can create one manually to make a copy of an existing object.




# class MyClass:
#     def __init__(self,value):
#         self.data=value

#     # Copy constructor
#     def __init__(self,other):
#         self.data=other.data

# obj1=MyClass(42)

# obj2=MyClass(obj1)

# print("obj1.data:",obj1.data)
# print("obj2.data:",obj2.data)








# class MyClass:
#     def __init__(self,value):
#         if isinstance(value,MyClass):
#             self.data=value.data
#         else:  
#             self.data=value
           
# obj1=MyClass(42)
# obj2=MyClass(obj1)

# print("obj1.data:",obj1.data)
# print("obj2.data:",obj2.data)



#==================distructors===========================
# class Student:
#     def __init__(self, name):
#         self.name = name
#         print("Object created")

#     def __del__(self):
#         print("Object destroyed")

# s = Student("Rahul")


# class FileHandler:
#     def __init__(self, filename):
#         self.file = open(filename, "w")
#         print("File opened")

#     def write_data(self, data):
#         self.file.write(data)

#     def __del__(self):
#         self.file.close()
#         print("File closed using destructor")


# # Create object
# f = FileHandler("demo.txt")
# f.write_data("Hello Python")

# # Object deleted
# del f



#=============accessing attributes============================
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# s1 = Student("Rahul", 20)
# s2 = Student("Anu", 18)

# #--------getatttr------------

# print(getattr(s1,'name',))
# # print(getattr(s1,'School')) #Error
# print(getattr(s1,'School','Quest')) 

# #--------hasattr-----------
# print(hasattr(s1,'name'))
# print(hasattr(s1,'school'))


# #--------setattr----------------
# setattr(s1,'age',21)
# print(s1.age)
# setattr(s1, 'grade', 'A')
# print(s1.grade)

# #--------delattr----------------
# delattr(s1, 'grade')

# print(hasattr(s1, 'grade'))  # False

# # delattr(s1,"school") #Error



#===========================inheritance==================================
# class Parent:
#     def __init__(self):
#         print("Parent constructor")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child constructor")

# c = Child()


#single inheritance

# class Vehicle:
#     def fuel_type(self):
#         print("Most vehicles use petrol or diesel")

# class Car(Vehicle):
#     def wheels(self):
#         print("A car has 4 Wheels.")


# c = Car()
# c.fuel_type()  # inherited from Vehicle
# c.wheels()     # defined in Car


# #2.-----------multilevel inheritance------------------------
# class Vehicle:
#     def fuel_type(self):
#         print("Most vehicles use petrol or diesel.")

# class Car(Vehicle):
#     def wheels(self):
#         print("A car has 4 wheels.")

#     def fuel_type(self):
#         return super().fuel_type()

# class ElectricCar(Car):
#     def battery_type(self):
#         print("Electric cars use lithium-ion batteries.")


# ec = ElectricCar()
# ec.fuel_type()    # from Vehicle
# ec.wheels()       # from Car
# ec.battery_type() # from ElectricCar


# #-----------------multiple inheritance--------------
# class SportsPerson:
#     team = 'Barcelona'
#     def action(self):
#         print("Plays football")

# class Musician:
#     band = 'thaikudam'
#     def action(self):
#         print("Plays guitar")

# class Student( Musician ,SportsPerson):
#     def study(self):
#         print("Studies in college")

# sanika = Student()

# print(sanika.team)
# print(sanika.band)
# sanika.study()
# sanika.action()
# print(Student.mro())










# sanika.study()
# sanika.action()
# print(Student.mro())
# s = Student()
# s.action()
# s.study()
# print(Student.mro())

#---------------super()------------------
# class Vehicle:
#     def start(self):
#         print("Engine started")

# class Car(Vehicle):
#     def start(self):
#         super().start()     # parent behavior
#         print("Car is ready to drive")

# c = Car()
# c.start()

# class Account:
#     def __init__(self, balance):
#         self.balance = balance

# class SavingsAccount(Account):
#     def __init__(self, balance, interest):
#         super().__init__(balance)   #  reuse parent logic
#         self.interest = interest

#-----------------Hierarchical Inheritance--------------------
# class Shape:
#     def color(self):
#         print("All shapes have a color.")

# class Circle(Shape):
#     def area(self, r):
#         print("Circle area:", 3.14*r**2)

# class Rectangle(Shape):
#     def area(self, l, b):
#         print("Rectangle area:", l*b)

#     def test(self):
#         pass

# c2 = Circle()
# c2.area(3)

# r3 = Rectangle()
# r3.area(5,2)

# c2.color()
# r3.color()









# c = Circle()
# r = Rectangle()
# c.color()          # from Shape
# c.area(5)           # Circle method
# r.color()           # from Shape
# r.area(4, 6)        # Rectangle method


#--------------hybrid inheritance---------------------------
# Base class
# class Vehicle:
#     def fuel_type(self):
#         print("Vehicles use some fuel type.")

# # Level 1
# class Car(Vehicle):
#     def wheels(self):
#         print("Car has 4 wheels.")

# class Motorcycle(Vehicle):
#     def wheels(self):
#         print("Motorcycle has 2 wheels.")

# # Level 2 (Hybrid)
# class ElectricCar(Car):
#     def battery(self):
#         print("Electric Car uses lithium battery.")

# class ElectricMotorcycle(Motorcycle):
#     def battery(self): 
#         print("Electric Motorcycle uses lithium battery.")

# ec = ElectricCar()
# em = ElectricMotorcycle()

# ec.fuel_type()
# ec.wheels()
# ec.battery()

# em.fuel_type()
# em.wheels()
# em.battery()

# #====================polymorphism==============================
# # class Dog:
# #     def sound(self):
# #         return "Bark"

# # class Cat:
# #     def sound(self):
# #         return "Meow"

# # class Cow:
# #     def sound(self):
# #         return "Moo"


# # animals = [Dog(), Cat(), Cow()]
# # for animal in animals:
# #     print(animal.sound())




# #real world example
# # class Payment:
# #     def pay(self, amount):
# #         print("Processing payment...")

# # class CreditCard(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using Credit Card")

# class UPI(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using UPI")

# class Cash(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using Cash")


# payments = [
#     CreditCard(),
#     UPI(),
#     Cash()
# ]

# for p in payments:
#     p.pay(500)


#-----------operator overloading-----------------
# class Book:
#     def __init__(self, pages):
#         self.pages = pages

#     def __add__(self, other):
#         return self.pages + other.pages

# b1 = Book(100)
# b2 = Book(150)

# total_pages = b1 + b2
# print(total_pages)


# class Student:
#     def __init__(self, marks):
#         self.marks = marks

#     def __eq__(self, other):
#         return self.marks == other.marks

# s1 = Student(80)
# s2 = Student(80)
# s3 = Student(90)

# print(s1 == s2)
# print(s1 == s3)


#-------------method overloading---------------------------
# class Test:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c
# t = Test()
# t.add(1, 2)


# class Calculator:
#     def add(self, *numbers):
#         total = 0
#         for n in numbers:
#             total += n
#         return total
# calc = Calculator()
# print(calc.add(1, 2))
# print(calc.add(1, 2, 3))
# print(calc.add(1, 2, 3, 4))


# -----------method overriding------------------
# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")


# class Bike(Vehicle):
#     def start(self):
#         super().start()
#         print("Self Start")
# b = Bike()
# print(b.start())


# class Vehicle:
#     def start(self):
#         print("Vehicle engine started")

# class Car(Vehicle):
#     def start(self):
#         super().start()     # parent method
#         print("Car is ready to drive")


#------------constructor overloading------------------------
"""Python does NOT support constructor overloading directly"""
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks



#==================encapsulation===================================
class BankAccount:
    bank_name = "Safe Bank"       # Public: accessible everywhere

    def __init__(self, account_no, balance):
        self._account_no = account_no   # Protected: accessible in class and subclasses
        self.__balance = balance        # Private: accessible only inside class

    # Public method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Insufficient balance.")

    # Public method to access private variable
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount< 0:
            return "invalid value"
        else:
            self.__balance = amount
            return f"New balance : {self.__balance}"
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount< 0:
            return "invalid value"
        else:
            self.__balance = amount
            return f"New balance : {self.__balance}"


acc = BankAccount(101, 5000)

print(acc.balance)

acc.balance = 9000

print(acc.balance)










# print(acc.get_balance())
# acc.set_balance(8000)
# print(acc.get_balance())

# print(acc.get_balance())
# print(acc.set_balance(2500))

# print(acc.balance)
# acc.balance = 90000
# print(acc.balance)





# class Test(BankAccount):
#     def __init__(self, account_no, balance):
#         super().__init__(account_no, balance)

#     def balance(self):
#         print(self.__balance)


# t = Test(101, 5000)
# print(t.balance())








# # acc._account_no = 202
# # print(acc._account_no)
# # print(acc.get_balance())
# # print(acc.set_balance(-25000))

# print(acc.balance)
# acc.balance = 8000
# print(acc.balance)

# Access public variable
# print(BankAccount.bank_name)  

# Access protected variable (not recommended but possible)
# print(acc._account_no)         

# # Access private variable (will cause error)
# print(acc.__balance)         #  AttributeError

# # Use public methods 0000000000
# acc.deposit(2000)
# acc.withdraw(1500)
# print("Balance:", acc.get_balance())



#==============================abstraction===============================
from abc import ABC, abstractmethod

# class Shape(ABC):
    
#     @abstractmethod
#     def area(self):
#         pass      # hidden / not implemented here


# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
    
#     def area(self):
#         return 3.14 * self.r **2


# c = Circle(5)
# print(c.area())

from abc import ABC, abstractmethod

class SmartPhone(ABC):

    @abstractmethod
    def call(self):
        pass
    
    @abstractmethod
    def message(self):
        pass
    
    @abstractmethod
    def internet(self):
        pass


class Iphone(SmartPhone):
    def __init__(self, price):
        self.price = price

    def call(self):
        print("Calling.....")

    def message(self):
        print("Messenging....")

    def internet(self):
        return super().internet()

xseries = Iphone(562352)
# xseries.call()
# xseries.message()
        
        






#------------------------------Partial Abstraction---------------------------------
# """Abstract class with normal + abstract methods"""
# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

#     def sleep(self):
#         print("Sleeping...")   # already implemented


# class Dog(Animal):
#     def sound(self):
#         print("Bark")


# d = Dog()
# d.sound()
# d.sleep()


# #------------------------------Complete Abstraction---------------------------
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass


# class Car(Vehicle):
#     def start(self):
#         print("Car started")

#     def stop(self):
#         print("Car stopped")


# c = Car()
# c.start()
# c.stop()


#------------------real life example---------------------------------
# from abc import ABC, abstractmethod

# class ATM(ABC):

#     @abstractmethod
#     def withdraw(self):
#         pass


# class SBI_ATM(ATM):
#     def withdraw(self):
#         print("Money Withdrawn Successfully")


# atm = SBI_ATM()
# atm.withdraw()


# from bankclass import BankAccount

# ac = BankAccount(102,300)
# print(ac._account_no)
# print(ac._BankAccount__balance)




# class College:
#     college_name = 'Srinivas' #attribute

#     def placement(self):
#         print("200% placement assist")

#     def management(self):
#         print("Best one in india")



# c3 = College() #c3 - object
# d3 = College()

# """access attributes using object"""
# print(c3.college_name)
# print(d3.college_name)

# c3.placement()
# c3.management()

# d3.placement()
# d3.management()




# class Father:
#     def __init__(self, name, job):
#         self.name = name
#         self.job = job

#     def Job(self):
#         print({self.job})

# class Mother:
#     def __init__(self, m_name, dishes):
#         self.m_name = m_name
#         self.dishes = dishes

#     def special_dishes(self):
#         print({self.dishes})

# class Child(Father, Mother):
#     def __init__(self, name, job,m_name,dishes):
#         super().__init__(name, job)
#         super().__init__(m_name, dishes)

# nivin = Child('kumar', 'Engineer','Mini','Biriyani')
# print(nivin.dishes)




# from  shari import Student_data

# haifa = Student_data('haifa',5653526532,952526352652)
# print(haifa.name)
# print(haifa._adhar)
# print(haifa.__pan)


# from OOPS.test import Student

# ziya = Student()
# ziya.





# class Bank:
#     bank_name = "SBI" 

#     def __init__(self,acc_no, name,ifsc ,balance ):
#         self.__acc_no = acc_no
#         self.name = name
#         self.ifsc = ifsc
#         self._balance = balance

#     def deposite(self, amount):
#         self._balance += amount
#         print(f"{amount} credited successfully. Balance : {self._balance}")

#     def withdraw(self, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#             print(f"{amount} debited successfully, avl balance : {self._balance}")
#         else:
#             print("Insufficient balance......")

#     def getbalance(self):
#         print(f"avilable balance : {self._balance}")


# #     def __del__(self):
#         print("Constructor deleted...")


# sree = Bank(acc_no=523696896,name="Sreeraj")
# sree.getbalance()
# sree.deposite(500)
# sree.withdraw(15000)


# class Animal:
    
#     def eat(self):
#         print("Eating.....")

#     def sleep(self):
#         print("Sleeping...")


# class Dog(Animal):
#     def run(self):
#         print("Running.....")

# arjun = Dog()
# arjun.eat()
# arjun.sleep()
# arjun.run()

# dog = Animal()




# class Person:
#     def __init__(self, name, age, address):
#         print("Calling Parent constructor..... ")
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(f"Name : {self.name}\nAge : {self.age}")

#     def test(self):
#         print("Testing parent method...")

# class Student(Person):
#     def __init__(self, name, age,address, course):
#         super().__init__(name, age,address)
#         print("Calling Child constructor.....")

#     def test(self):
#         super().test()
#         print("Testing child method...")
       

# richu = Student("richu", 22,"Python")
# richu.test()




# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Developer(Person):

#     def __init__(self, name, age, salary, language):
#         super().__init__(name, age)
#         self.salary = salary
#         self.language = language


#     def get_details(self):
#         print(f"Name : {self.name}\nage : {self.age}\nsalary : {self.salary}\nlanguage : {self.language}")

# Najad = Developer(name='Najad', age= 25, salary= 25000, language= "Python")

# Najad.get_details()
# print(Najad.name)





# class Vehicle:
#     def Start(self):
#         print("Vehicle can start")

#     def Break(self):
#         print("Liner")


# class Car(Vehicle):
#     def horn(self):
#         print("Horn...")

#     def Break(self):
#         super().Break()
#         print("ABS")

# class Ev(Car):
#     def Break(self):
#         super().Break(self)

#         Vehicle.Break()
#         print("Smooth breaking with new features.")

# nexa = Ev()
# nexa.horn()
# nexa.Start()




# class Electronics:

#     def collections(self):
#         print("collection of Electronics items...")

#     class Laptop:

#         def brand(self):
#             print("HP")


# e = Electronics()

# laptop = Electronics.Laptop()
# laptop.brand()




# class Opeations:

#     def add(self,a,b):
#         return a * b

    
# o2 = Opeations()

# print(o2.add(5,2))
# # print(o2.add('sree','raj'))
# print(o2.add('sree',3))



# from abc import ABC, abstractmethod


# class FirstGenATM(ABC):

#     @abstractmethod
#     def withdraw(self):
#         pass

#     def check_balance(self):
#         pass


# class NewGenATM(FirstGenATM):
#     def withdraw(self):
#         return "can withdraw..."


# sbi = NewGenATM()


# class Animal:

#     def make_sound(self):
#         print("animal makes sound")


# class Dog:

#     def make_sound(self):
#         print("Bow Bow")

# class Cat:
#     def make_sound(self):
#         print("Meow Meow")



# def sound(animal):
#     animal.make_sound()



# a = Animal()
# d = Dog()
# c = Cat()

# sound(a)
# sound(c)
# sound(d)