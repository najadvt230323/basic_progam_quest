def greet():
    print("hello welcome programmers.......")

def greet1(name):
    print(f"hello welcome {name}.......")

def greet2(a,b,c):
    print(f"hello welcome {a}.......")
    print(f"hello welcome {b}.......")
    print(f"hello welcome {c}.......")
    return(a,b,c)

def add(a,b):
    return(a+b)

type(greet)
greet()
greet1("najad")
greet2("najad","richu","shabin")

a=add(25,24)
print(add(50,25))  # output - 75
print(a)           # output - 49

print(greet2("najad","richu","shabin"))    #hello welcome najad.......                                        
                                            #hello welcome richu.......
                                            #hello welcome shabin.......
                                            #('najad', 'richu', 'shabin')

b=greet2("najad","richu","shabin")
print(b)                                #('najad', 'richu', 'shabin')
print(type(b))                          ##<class 'tuple'>
print()

def u(a):
    return a.upper()

def l(a : str):
    return a.upper()

def v(a : str) -> str:
    return a.upper()

# a=input("enter a string :")
# print(u(a))
# print(l(a))
# print(v(a))

def details(n : str , age : int , phon : list):
    return(n,age,phon)

# positional arguments

print(details("najad",25,[9562020207,924973016]))

# key wored arguments
print(details(age=26,n="najad",phon=9562020207))

# default arguments

def add1(a=0,b=0,c=0):
    return a+b+c

print(add1(10,20,30))
print(add1(10,20))
print(add1(10,))
print(add1())
# ----------------------------

print()
def add2(a=0,b=0,c=0):
    return a+b+c

print(add(10,20))
# ----------------------------

# arbitrary arguments (variable length positional arguments)

def add3(*args):
    print(args)
    s=0
    for i in args:
        s=s+i
    return s

print(add3(10,20,30,40,50,60,70,80,90))
print(add3(10,20,30,40))
print(add3(10,20,30))
print(add3(10,20))

# key wored arbitrary arguments (variable length positional arguments)

def details(**kwargs):
    print(kwargs)
details(name="najad",age="25")
details(name="richu",age="25",phon=9562020207)
details(name="aju",age="28",phon=9249730116,place="calicut")
# details(name="aju",age="28",phon=9249730116,place="calicut",Cose)       #SyntaxError: positional argument follows keyword argument
# details(name="aju",age="28",phon=9249730116,place="calicut",Cose=)      #SyntaxError: expected argument value expression
# details(name="aju",age="28",phon=9249730116,place="calicut",a)          #SyntaxError: positional argument follows keyword argument
# ----------------------------------------------------------------------------------------------

def even(*args : tuple):
    a=[]
    for i in args:
        if i%2==0:
            a.append(i)
    return a
print(even(1,2,3,4,5,6,7,8,9,10,11,12,13,14))


def details1(*args,**kwargs):
    print(kwargs)
    print(args)
details1(name="aju",age="28",phon=9249730116,place="calicut")
details1(1,2,3,name="aju",age="28",phon=9249730116,place="calicut")  

def details1(a,b,*args,**kwargs):
    print(a)                      # output -  1
    print(b)                      # output -  2
    print(kwargs)                 # output -  {'name': 'aju', 'age': '28', 'phon': 9249730116, 'place': 'calicut'}
    print(args)                   # output -  (3,)
details1(1,2,3,name="aju",age="28",phon=9249730116,place="calicut") 


# ways to pass valu to a function
# -------------------------------------
# 1.pass by Value
# -------------------------
# -> tha function get acopy of tha data .if tha function changes that copy,
#    tha original variable outside tha function stays tha same

def modify(a:int)-> int:
    print(a)               #output - 5
    a=25
    print(a)               #output - 25
    return(a)
b=5
print(modify(b))           #output - 25
print(b)                   #output - 5


# 2 pass by Referenc
# -----------------------
# -> tha function gets a referenc (a pointer) to tha original data. if tha function 
#     modify
      
def modify1(a:list)-> list:
    print(a)               #output - [10, 20, 30]
    a.append(40)
    print(a)               #output - [10, 20, 30, 40]
    return(a)
b=[10,20,30]
print(modify1(b))           #output - [10, 20, 30, 40]
print(b)                   #output - [10, 20, 30, 40]
print()

def modify2(a:tuple)-> tuple:
    print(a)               #output - (10, 20, 30)
    a=list(a)
    a.append(40)
    print(a)               #output - [10, 20, 30, 40]
    a=tuple(a)
    print(a)               #output - (10, 20, 30, 40)
    return(a)
b=(10,20,30)
print(modify2(b))           #output - (10, 20, 30, 40)
print(b)                   #output - (10, 20, 30)
print()

print()
def modify3():
    global b
    print(b)               #output - (10, 20, 30, 40, 50)
    b=list(b)
    b.append(60)
    print(b)               #output - [10, 20, 30, 40,50, 60]
    return b

b=(10,20,30,40,50)
print(modify3())           #output - [10, 20, 30, 40,50, 60]
print(b)                   #output - [10, 20, 30, 40, 50, 60]

#recvorsive function
# -----------------------

print()
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
    
print()
def rev(n : str):
    if len(n)==1:
        return n[0]
    return rev(n[1:])+n[0]
print(rev("najad vt"))

print()
def rev1(n : str):
    if len(n)==1:
        return n[0]
    return n[-1] + rev1(n[:-1])
print(rev1("najad vt"))

# lambda function
# --------------------

print()
l=lambda a:a**2
print(l)
print(type(l))
print(l(10))

print()
l1=lambda a,b,c:a+b+c
print(l1(10,20,30))

print()
l1=lambda a=0,b=0,c=0:a+b+c
print(l1(10,20,30))
print(l1(10,20))
print(l1(10))

print()
l1=lambda a,b,c:[a**2,b**2,c**2]
print(l1(10,20,30))

print()
l1=lambda a:"ood" if a%2==1 else "evan"
print(l1(10))

# a=input("enter a string : ")
# l2=lambda a:len(a)
# print(f"length of string : {l2(a)}")

# print()
# l3=lambda a,b:a if a>b else "eqal" if a==b else b
# (print("enter a 2 intger number : "))
# a=int(input())
# b=int(input())
# print(l3(a,b))

# print()
# l3=lambda a,b,c:a if a>b and a>c else b if b>a and b>c else c
# (print("enter a 3 intger number : "))
# a=int(input())
# b=int(input())
# c=int(input())
# print(l3(a,b,c))

print()
l3=lambda a:"multipel of 5" if a%5==0 and not a%3==0 else "multipel of 3" if not a%5==0 and a%3==0 else "multipel of 3 and 5" if  a%5==0 and a%3==0 else "not multipel of 3 and 5"
print(l3(15))
