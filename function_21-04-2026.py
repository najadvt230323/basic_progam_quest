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

      




