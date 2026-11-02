# set

s=set()
print(type(s))

print()
s1={1,2,3,4,5,5,1.5,"najad","richu",(10,20,30)}
s2=list(s1)
print(type(s1))
print(s1)
print(s2)

print()
a=[1,2,3,3,4,4,4,5,5,(10,10,20),(10,10,20),(10,20,10),(10,10,20)]
b=set(a)
c=list(b)
print(a)
print(b)
print(c)

print()
s3=set({10,20,30})
print(s3)

print()
a=[1,2,3,(10,20),{"najad",'ricu',100,200}]
print(a.index(3))

print()
print(dir(s1))
'''
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', 
'__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', 
'__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 
'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

'''

print()
print(enumerate(a))
print(list(enumerate(a)))
print(tuple(enumerate(a)))
# print(set(enumerate(a))) #error
for i,v in enumerate(a):
    print(i,v)

print()
print(enumerate("najad"))
print(list(enumerate("najad")))

# add

print()
a={1,2,3}
a.add("najad")
print(a)
a.add(100)
print(a)
a.add(("ricu",'shahal'))
print(a)
a.add(tuple("ricu"))
print(a)

print()
a.update("naju")
print(a)
# a.update(200) #error
a.update({200})
print(a)

print()
# a += 'naju' #error
# a += tuple("naju") #error
# a *=3  #error 
print(a)
a.remove(100)
print(a)
# a.remove("naju") #error
a.remove("najad")
print(a)

print()
a.pop()
print(a)
a.pop()
print(a)

print()
a.discard(200)
print(a)
a.discard(500)
print(a)

print()
a.clear()
print(a)

print()
a={1,2,3,4,5,7,8}
b={4,5,6,7,8}
c={7,8,9,10,11}
print(a.union(b))
print(a|b)

print()
print(a.union(b,c))
print(a|b|c)
print(len(a|b|c))

print()
print(a.intersection(b))
print(a&b)

print()
print(a.intersection(b,c))
print(a&b&c)
print(len(a&b&c))

print()
a.intersection_update(b)
print(a)
a&=c
print(a)

a={1,2,3,4,5,7,8}
b={4,5,6,7,8}
c={3,7,8,9,10,11}
print()
print(a.difference(b))
print(a-b)
print(a)

print()
a.difference_update(b)
print(a)
a-=c
print(a)

a={1,2,3,4,5,7,8}
b={4,5,6,7,8}
c={3,7,8,9,10,11}
print()
print(a.symmetric_difference(b))
print(a^b)
print(a)

print()
a.symmetric_difference_update(b)
print(a)
a^=c
print(a)

a={1,2,3,4,5,7,8}
b={4,5,6,7,8}
c={3,2}
print()
print(c.issubset(a))
print(a.issubset(c))
print(b.issubset(a))

print()
print(c.issuperset(a))
print(a.issuperset(c))
print(b.issuperset(a))

print()
print(b.isdisjoint(a))
print(b.isdisjoint(c))

# set comperehension
# ------------------------

print()
num={1,2,3,4,5,6,7,8,9,10,11,12}
num3={i for i in num if i%3==0}
print(num3)
a={i for i in range(7) if i%3==0}
print(a)

print()
b={"even" if i%2==0 else "odd" for i in range(1,11)}
print(b)

b=["even" if i%2==0 else "odd" for i in range(1,11)]
print(b)
b=[0 if i<5 else 1 for i in range(1,11)]
print(b)
b=[0 if i<5 else 5 if i==5 else 1  for i in range(1,11)]
print(b)

b={0 if i<5 else 1 for i in num}
print(b)
b={0 if i<5 else 5 if i==5 else 1  for i in num}
print(b)