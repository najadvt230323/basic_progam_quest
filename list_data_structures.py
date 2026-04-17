'''
paython data structures
-----------------------------
* store multiple valu
* organize and retrieve data quickly
* improve performance of programs
* peroform operation like searching,sortind and updating 
-----------------------------------------------------------
1.list








'''
a=[1,2,3,"quest",10.25,[7,8,9],True,False,None,(1,2,3)]
b=list([1,2,3,"quest",10.25,[7,8,9],True,False,None,(1,2,3)])
c=a
d=list("quest")
# e=list(1)      # Type Error: 'int' object is not iterable


print(type(a))
print(type(b))

print(a)
print(b)
print(c)
print(d)

print(len(a))
print(len(b))
print(len(c))
print(len(d))

print("")
for i in range(len(a)):
    print(a[i])

print(len(a[5]))

# for i in a:
#     for j in i:
#         print(j)

'''operators'''

number=[1,2,3,4,5,6,7,8,9]
number1=[10,20,30,40,50]
# number+=10  #erorr
number+=[10]
print(number)
# number+="10"
# # print(number) #output   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, '1', '0']

number2=number+number1
print(number2)
number3=number*3
number*=2
print(number3)
print(number)

print()
print(dir(number))
'''

['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
'__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 
'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

'''
print()
print(100 in number)
print(10 in number)


n=[1,2,3,4,5,6,7,8,[10,20,30]]
print(30 in n)
print(30 in n[-1])
print(30 in n[8])
print(len(n[-1]))
print(n[8][2])
print(n[-1][-2])
print()
for i in range(len(n)):
    print(n[i],end=" ")

print()
for i in range(-1,-len(n),-1):
    print(n[i],end=" ")

print()
print(n[5:8])
print(n[-1:-4:-1])
print(n[5:])
print(n[:8])
print(n[-5:-1])

n1=["quest","najad","richu",1,2,3]
print(n1[1][1:4])

matrix=[[0,1,2],[3,4,5],[6,7,8]]

for i in range(len(matrix)):
    print(matrix[i])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=" ")
    print()

for i in matrix:
    print(i)

for i in matrix:
    for j in i:
        print(j,end=" ")
    print()



# append()
print()
a=[10,20,30,'najad','richu']
a.append("quest")
a.append([40,50,60])
print(a)

# insert()
print()
a.insert(3,'python')
print(a)

# pop()
print()
a.pop()
print(a)
a.pop()
print(a)
a.pop(2)
print(a)
a.pop(-3)
print(a)

# remove()
print()
a.remove(20)
print(a)
# a.remove(15) #error

# clerar()
print()
a.clear()
print(a)

# count()
a=[1,2,3,4,2,3,4,5,[2,3]]
print()
print(a)
print(a.count(1))
print(a.count(3))
print(a.count(2))

# copy()
b=a.copy()
print(b)
'''
1.shalow copy -----  rafernc
2.deep copy
'''
# b+=[[10,3]]
b[2]=300
print(b)
print(a)
b[-1][-1]=300
print(b)
print(a)

# sort()
a=[1,2,8,6,5,3,4,5,7.5]

print()
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
b=['najad','quest','richu','aju','name','aaa',"is",'Z']
print(b)
b.sort()
print(b)
b.sort(reverse=True)
print(b)
b.sort(key=len)
print(b)
b.sort(key=len,reverse=True)
print(b)

# extend()
print()
a.extend(b)
print(a)
a.extend(["najad"])
print(a)
a.extend("najad")
print(a)

# index()
print()
print(a.index(6))
b=[1,5,6,7,4,5,2,5,"najad"]
print(b)
print(b.index(5))
print(b.index(5,0,3))
print(b.index(5,3,6))
print(b.index(5,6))

# reverse()
b.reverse()
print(b)


a=[2,3,1,4,5,8,9]
print()
print(a)
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sorted(a))
print(sorted(a,reverse=True))
# print(sorted(a,key=len))  #error

a=['najad','my','MY','sreeraj','x']
print()
print(a)
print(len(a))
print(max(a))  
print(min(a)) 
# print(sum(a)) #error
print(sorted(a))
print(sorted(a,reverse=True))
print(sorted(a,key=len))  

# list comperehension
# ------------------------

print()
f=["apple", "banana","cherry","kiwi","mango"]
print(f)
a=[x for x in f if "a" in x]
print(a)

print()
a=[]
for i in range(1,11):
    a+=[i]
print(a)

a=[]
for i in range(1,11):
    a.append(i)
print(a)

a=[i for i in range(1,11)]
print(a)
b=[i for i in a if i%2==0]
print(b)

a=[i**2 for i in range(1,11)]
print(a)
a=[i**.5 for i in range(1,11)]
print(a)

print()
a=[]
for i in range(1,11):
    if i%2==0:
        a.append(i**2)
    else:
        a.append(i**3)
print(a)

a=[i**2 if i%2==0 else i**3 for i in range(1,11)]
print(a)

print()
f=["apple", "banana","cherry","kiwi","mango","elephend"]
print(f)
a=[i.upper() for i in f]
print(a)
a=[i.upper() for i in f if "a" in i]
print(a)
a=[len(i) for i in f]
print(a)

a=[i.upper() if i[0]=="a" or i[0]=="e" or i[0]=="i" or i[0]=="o" or i[0]=="u" or i[0]=="A" or i[0]=="E" or i[0]=="O" or i[0]=="U" else i.title() for i in f]
print(a)

a=[i.upper() if i[0] in "AEIOUaeiou" else i.title() for i in f]
print(a)                                                                                                              

a=[1,0,-6,2,5,-6]
b=[i for i in a if i>=0]
print(b)

a="vnfjbvufh fuyrhiodwjpw"
b=[a[i] for i in  range(0,len(a)) if a[i] in "AEIOUaeiou"]
print(b)
b=[i for i in a if i in "AEIOUaeiou"]
print(b)

list1=[1,2,3,4,5,6]
list2=[4,5,6,7,8,9]
a=[list1[i] for i in range(0,len(list1)) if list1[i] in list2]
print(a)

a=[i for i in list1 if i in list2]
print(a)

list1=['1','2','3','4','5','6']
a=[int(i) for i in list1]
print(a)

list1=['1','2','3','4','5','6','richu']
a=[int(i) for i in list1 if i.isdigit()]
print(a)

b=["even" if i%2==0 else "odd" for i in range(1,11)]
print(b)
b=[0 if i<5 else 1 for i in range(1,11)]
print(b)
b=[0 if i<5 else 5 if i==5 else 1  for i in range(1,11)]
print(b)

# list unpacking

l=[10,20,30]
x,y,z=l
print(x)
print(y)
print(z)

print()
l=[10,20,30,40,50]
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