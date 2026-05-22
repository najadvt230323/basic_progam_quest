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

# 2.multilaval Inheritance
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
nexa.horn()                                # output : horn......
nexa.start()                               # output : vehicle can start
# ------------------------------------------------------------------------------

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
nexa.brik()                              # output : vehicle can start
                                                    # horn......
                                                    # brik......

# -------------------------------------------------------------------------------


# 3.multpil Inheritance
# ----------------------------
class A:
    a="aaaaaaaa"
    def aa(self):
        print("11111")
    def action(self):
        print("wroking class A")


class B:
    b="bbbbbbbbb"
    def bb(self):
        print("222222") 
    def action(self):
        print("wroking class b")

class C(A,B):
    c="cccccccc"
    def cc(self):
        print("33333")

richu=C()
print(richu.a)                    # output : aaaaaaaa
print(richu.b)                    # output : bbbbbbbbb
print(richu.c)                    # output : cccccccc
richu.aa()                        # output : 11111
richu.bb()                        # output : 222222
richu.cc()                        # output : 33333 
richu.action()                    # output : wroking class A
print(C.mro())                    # output : [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

# ---------------------------------------------------------------------------------------

# 4.Hierarchial Inheritance
# -------------------------------
print()
class shape:
    def color(self):
        print("all shapes have a color.")

class circle(shape):
    def area(self,r):
        print(f"circle area : {round(3.14*r*2,3)}")
class rectangle(shape):
    def area(self,l,b):
        print(f"circle area : {b*l}")
    
c=circle()
c.area(5)                    # output : circle area : 31.4

d=rectangle()
d.area(5,6)                  # output : circle area : 30

# ---------------------------------------------------------------------------------------

# 5.Hybrid Inheritance
# -------------------------------
print()
class vehicle:
    def fuel(self):
        print("vehicles use some fuval type")

# leval 1
class car(vehicle):
    def wkeels(slef):
        print("car has 4 wheels.")
class bick(vehicle):
    def wkeels(slef):
        print("bick has 2 wheels.")

# leval 2
class elect_car(car):
    def battery(self):
        print("electric car uses lithium battety.")

class elect_bick(car):
    def battery(self):
        print("electric bick uses lithium battety.")

ec=elect_car()
em=elect_car()

ec.battery()                                  # output : electric car uses lithium battety.
ec.fuel()                                     # output : vehicles use some fuval type
ec.wkeels()                                   # output : car has 4 wheels.

em.battery()                                  # output : electric car uses lithium battety.
em.fuel()                                     # output : vehicles use some fuval type
em.wkeels()                                   # output : car has 4 wheels.

# ----------------------------------------------------------------------------------------------------

# qu: bulid a food delivary app using multiple inheritance
print()
class Hotel:
    hotel_name="kubaba manthi"
    def hotel_items(self):
        print("1.kubaba sp manthi\n2.kubaba normal manthi")
    def pyment(self):
        print("1.cash\n2.g-pay")
class User:
    user_name="richu"
    def order(self):
        print("one kubaba sp manthi")
class Delivery:
    delivery_name="shabin"
    def location(self):
        print("kunnamagalam")
class App(Hotel,User,Delivery):
    app_name="suggi"
    def food(self):
        print("order food")

richu=App()

print(richu.app_name)                     # output : suggi
print(richu.hotel_name)                   # output : kubaba manthi
print(richu.delivery_name)                # output : shabin
print(richu.user_name)                    # output : richu

        
richu.hotel_items()                       # output :1.kubaba sp manthi
                                                  # 2.kubaba normal manthi 
richu.pyment()                            # output : 1.cash
                                                   # 2.g-pay
richu.order()                             # output : one kubaba sp manthi
richu.location()                          # output : kunnamagalam
richu.food()                              # output : order food

# ---------------------------------------------------------------------------------------------------
print()
class A:
    def aa(self):
        print("class A")
    class B:
        def bb(self):
            print("class B")

a=A()
# b=b()               # nNameError: name 'b' is not defined. Did you mean: 'B'?
a.aa()                # output : class A
a.B().bb()            # output : class B
d=A().B()
e=d.bb()              # output : class B




    


