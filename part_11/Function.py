# def greet(name):
#     print("hello",name)

# greet("najad")

# def add(a,b):
#     return a+b

# r=add(5,7)
# print(r)

def greet(name):
    print("hello",name)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divid(a,b):
    return a/b

def squrare(a):
    return pow(a,2)

def cube(a):
    return pow(a,3)

def odd(a):
    if a%2==1:
      print("odd")
    else: 
     print("even")

a=input("enter your name : ")
print("entter two numbers : ")
b=int(input())
c=int(input())
print("what math function do you need : ")
print("add( '+' ) , subtract( '-' ) , multiply( '*' ) , divid( '/' ) , squrare( '2' ) , cube( '3' ) , odd or even ( '%' ): ")
print("enter the option : ")
d=input()
greet(a)


if d=="+":
   r=add(b,c)
   print(f"add {b} , {c} : {r}")

elif d=="-":
   r=subtract(b,c)
   print(f"subtract {b} , {c} : {r}")

elif d=="*":
   r=multiply(b,c)
   print(f"multiply {b} , {c} : {r}")

elif d=="/":
   r=divid(b,c)
   print(f"divid {b} , {c} : {r}")

elif d=="2":
   r=squrare(b)
   w=squrare(c)
   print(f"squrare {b}  : {r}")
   print(f"squrare {c}  : {w}")

elif d=="3":
   r=cube(b)
   w=cube(c)
   print(f"cube {b}  : {r}")
   print(f"cube {c}  : {w}")   

elif d=="%":
   print(f"odd or even {b}  : ", end="")
   odd(b)
   print(f"odd or even {c}  : ",  end="")
   odd(c)

else:
   print("wrong choice")
   
 
 