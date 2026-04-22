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

print()
def add2(a=0,b=0,c=0):
    return a+b+c

print(add(10,20))