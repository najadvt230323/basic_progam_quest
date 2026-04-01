t=(15,1.4,'najad',[1,2,3],(4,5,6))
print(t)
print(type(t))

t1=(1,)
print(type(t1))

t2=()
print(type(t2))

t3=tuple()
print(type(t3))

# add tuple

t+=(40,)
print(t)

l=list(t)
l.append(50)
t=tuple(l)
print(t)

# tuple unpacking

l=(10,20,30)
x,y,z=l
print(x)
print(y)
print(z)

print()
l=(10,20,30,40,50)
x,y,*z=l
print(x)
print(y)
print(z)

print()
x,*y,z=l
print(x)
print(y)
print(z)

print()
*x,y,z=l
print(x)
print(y)
print(z)

del l 
# print(l)

print()
print(t)
print(t[2:4])
print(t[-1:-4:-1])
print(t[2:])
print(t[:3])
print(t[-4:-1])


for i in t:
    print(i)
    print(type(i))

for i in range(len(t)):
    print(t[i])

print()
# print(i)
i=0
while i<len(t):
    print(t[i])
    i+=1

print(dir(t))

'''

['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

'''
print(t.count(40))
print(t.index(50))
# print(t.index(10)) #error

t1=t+(10,20)
print(t)
print(t1)
print(t1*3)

print(40 in t)
print(40 not in t)
