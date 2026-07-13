a={}
print(type(a))

print()

a={"name" : "richu" , "age" : 22 , "place" : "calicut" }
b={"name" : "richu" , "age" : 22 , "place" : "calicut" , "name" : "najad " ,"name" : "najad "}
c={"name" : "richu" , "age" : 22 , "place" : "calicut" ,"valu": 22 }
# d={1:"a",2:"b",3:"c",[1,2,3]:"d"}  #error
# d={1:"a",2:"b",3:"c",{1,2,3}:"d"}  #error
d={1:"a",2:"b",3:"c",(1,2,3):"d"}
# d={1:"a",2:"b",3:"c",{1:3}:"d"}  #error

print(a)
print(b)
print(c)
print(d)

print()
e={1:"a",2:"b",3:"c",4:[1,2,3]}  
f={1:"a",2:"b",3:"c",4:{1,2,3}} 
g={1:"a",2:"b",3:"c",4:(1,2,3)}
h={1:"a",2:"b",3:"c",4:{1:3}} 
print(e)
print(f)
print(g)
print(h)

print(dir(a))
'''
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', 
'__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
'__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 
'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
'''

print()
print(len(a))

print()
print(a)
a["batch"]="python"
a["name"]="najad"
print(a)

print()
a.update({"roll no":23, "age" :20 ,"domain" : "python"})
print(a)

print()
b={'name': 'richu', 'age': 22, 'place': ['calicut']}
print(b)
b["place"].append("nallaam")
print(b)

print()
print(a["name"])
print(a.get("name"))

# print(a["teacher"])    #error # KeyError: 'teacher'
print(a.get("teacher"))   #output ---  None
print(a.get("teacher" ,'key doesn\'t exist'))   #output ---  key doesn\'t exist

print()
print(a)
del a["place"]
print(a)

a.pop("roll no")
print(a)

p=a.pop("domain")
print(a)
# a.pop() #error
print(p)

print()
print(a)
a.popitem()
print(a)
a.popitem()
print(a)

a.clear()
print(a)

del a
# print(a) # error # NameError: name 'a' is not defined


print()
a={"name" : "richu" , "age" : 22 , "place" : "calicut" ,}
for i in a:
    print(i)
print()
for i,j in a.items():
    print(i,j)

print()
for i in a.keys():
    print(i)

print()
for i in a.values():
    print(i)

print()
print(a)
print(a.keys())
print(a.values())
print(a.items())


# fromkeys()

print()
a=[1,2,3]
d=dict.fromkeys(a)
print(d)

print()
a=(1,2,3)
d=dict.fromkeys(a)
print(d)

print()
c={}
a=[1,2,3]
d=c.fromkeys(a)
print(d)

print()
c={"name" : "richu" , "age" : 22 , "place" : "calicut" }
a=[1,2,3]
d=c.fromkeys(a)
print(c)
print(d)

# print()
# a=[1,2,3]
# # d=z.fromkeys(a) #error
# print(d)

print()
a={"a":1,"b":2}
print(a)
# print(a["c"]) #error
print(a.get("c"))
print(a.get("c",500))
print(a)
print(a.setdefault("d"))
print(a)
print(a.setdefault("d",500))
print(a)
print(a.setdefault("e",500))
print(a)


# zip
print()
a=[1,2,3,4,5]
b=[10,20,30,40]
c=zip(a,b)
print(c)
print(dict(c))
print(list(c))
print(list(dict(c)))

print()
a={
    "student1" : {
        "name" : "najad",
        "age" : 25 ,
        "batch" : "data science"
    },
    "student2" : {
        "name" : "yaseen",
        "age" : 26 ,
        "batch" : "data analist" ,
        "phone" : [9562020207,9249730116]      
    }
}
print(a)
print(a["student1"])
print(a["student2"])
print(a["student1"]["name"])
print(a["student2"]["name"])
print(a["student2"]["phone"])
print(a["student2"]["phone"][1])

print()
a["student2"]["phone"]=9400454130
print(a["student2"]["phone"])
a["student2"]["phone"]=(9400454130,9020020313)
print(a)
print(a["student2"]["phone"])
print()
print(a["student2"]["name"])
a["student2"]["name"]="richu"
print(a["student2"]["name"])
print(a)
print()

# dictionaries comperehension
# -------------------------------

a={i:i**2 for i in range(1,11)}
print(a)

a={i:i**2 for i in range(1,11) if i%2==0}
print(a)

a={i:i**2 if i%2==0 else i**3  for i in range(1,11)}
print(a)

a={"a":1,"b":2,"c":3,"d":4 ,"e":5}
b={k:v for k ,v in a.items() if v%2==0}
c={v:k for k ,v in a.items()}
print(a)
print(b)
print(c)

print()
alph=['a','b','c','d']
a={k:ord(k) for k in alph }
print(a)

print()
alph=[chr(i) for i in range(97,123)]
print(alph)
a={k:ord(k) for k in alph }
print(a)

print()
a={chr(k):k for k in range(97,123) }
print(a)
a={chr(k):k for k in range(65,91) }
print(a)

print()
a={i:i**2 if i%2==0 else i**3  for i in range(1,11)}
print(a)





