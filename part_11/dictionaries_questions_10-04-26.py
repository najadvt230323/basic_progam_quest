'''
PYTHON FULL STACK TRAINING: DICTIONARY LOGIC &INTERVIEW PREP
--------------------------------------------------------------------
Topic: Key-Value Pairs, JSON-like Structures, and Data Mapping
-----------------------------------------------------------------

--- PART 1: DICTIONARY BASICS & CREATION ---
-----------------------------------------------

1. Create a dictionary representing a 'Laptop' with keys: brand, model, and price.
2. Access the value of the 'model' key using square brackets.
3. Access the value of a key that doesn't exist using .get() and explain why it's safer than [].
4. Create an empty dictionary using both {} and the dict() constructor.
5. Add a new key-value pair 'processor': 'i7' to an existing dictionary.
6. Update the 'price' of the laptop to a new value.
7. Use the len() function to find how many key-value pairs are in a dictionary.
8. Create a dictionary where the keys are numbers 1 to 5 and the values are their squares.
9. Check if a specific key exists in a dictionary using the 'in' operator.
10. Delete a key-value pair using the 'del' keyword and handle the case if the key is missing.

--- PART 2: METHODS & MANIPULATION ---
--------------------------------------------

11. Use the pop() method to remove a key and store its value in a variable.
12. Use popitem() to remove the last inserted item and explain its behavior in Python 3.7+.
13. Use the keys() method to print all the keys in a dictionary.
14. Use the values() method to print all the values in a dictionary.
15. Use the items() method to iterate through a dictionary and print "Key: Value" for each
pair.
16. Merge two dictionaries: {'a': 1, 'b': 2} and {'c': 3, 'd': 4} using the update() method.
17. Clear all items from a dictionary using the clear() method.
18. Use the setdefault() method to add a key 'country' with value 'India' only if it doesn't exist.
19. Create a shallow copy of a dictionary and show that modifying the copy doesn't change
the original.
20. Create a dictionary from two lists: one for keys and one for values using the zip()
function.

--- PART 3: NESTED DICTIONARIES (API STYLE) ---
-------------------------------------------------------

21. Create a nested dictionary called 'Employees' containing data for three different people.
22. Access a value inside a nested dictionary (e.g., Employees['emp1']['salary']).
23. Update a value inside a nested dictionary.
24. Add a new nested dictionary (a new employee) to the existing 'Employees' structure.
25. Write a loop to print only the names of all employees from the nested 'Employees'
dictionary.
26. Create a dictionary where a key points to a list of values (e.g., 'hobbies': ['coding',
'reading']).
27. Append a new hobby to the list inside that dictionary.
28. Given a dictionary of students and their marks (a list), calculate the average marks for one
student.
29. Flatten a simple nested dictionary (convert {'a': {'b': 1}} to {('a', 'b'): 1}).
30. Represent a JSON response from a weather API as a nested dictionary and extract the
'temperature'.

--- PART 4: COMPREHENSIONS & LOGIC ---
----------------------------------------------

31. [Comprehension] Create a dictionary of even numbers between 1-10 as keys and their
cubes as values.
32. [Comprehension] Given a dictionary, create a new one with only items where the value is
> 100.
33. [Comprehension] Swap keys and values in a dictionary (Reverse Mapping).
34. Sort a dictionary by its keys in alphabetical order.
35. Sort a dictionary by its values in ascending order.
36. Find the key with the maximum value in a dictionary of product prices.
37. Count the frequency of each character in a string "Python Trainer" using a dictionary.
38. Combine two dictionaries by adding values for common keys.
39. Convert a dictionary into a list of tuples.
40. Check if all values in a dictionary are the same.

--- PART 5: INDUSTRIAL & INTERVIEW SCENARIOS ---
--------------------------------------------------------

41. [JSON] Use the 'json' module to convert a dictionary into a JSON string.
42. [Data Cleaning] Remove all keys from a dictionary that have None or empty string
values.
43. [Security] Explain why a list cannot be used as a dictionary key, but a tuple can.
44. [Logic] Write a program to find the sum of all values in a numeric dictionary.
45. [Simulation] Use a dictionary to simulate a simple "Switch-Case" statement logic.
46. [Efficiency] Compare the time it takes to find a value in a list of 10,000 items vs. a
dictionary.
47. [Functionality] Use **kwargs in a function to accept arbitrary keyword arguments as a
dictionary.
48. [Mapping] Create a dictionary to map Roman numerals to Integers (e.g., 'I': 1, 'V': 5).
49. [Logic] Given a list of words, group them by their starting letter using a dictionary.
50. [Interview Question] Explain the difference between '==' and 'is' when comparing two
identical dictionaries.

'''

# for i  in range(1,51):
#     print(f"# {i} : ")
#     print()
#     print(r"# '''")
#     print()
#     print()
#     print(r"# '''")
#     print()


# 1 : 
# Create a dictionary representing a 'Laptop' with keys: brand, model, and price.

# '''


# '''

# 2 : 
# Access the value of the 'model' key using square brackets.

'''
a={i:i**2 for i in range(1,4)}
for i in range(1,4):
    print(a[i])

'''

# 3 :
# Access the value of a key that doesn't exist using .get() and explain why it's safer than [].

'''
a={i:i**2 for i in range(1,4)}
print(a.get(4))
print(a.get(4),'key that doesn\'t exist')

'''

# 4 :
# Create an empty dictionary using both {} and the dict() constructor.

'''
a={}
b=dict()
print(type(a))
print(type(b))

'''

# 5 :
# Add a new key-value pair 'processor': 'i7' to an existing dictionary.

'''
a={i:i**2 for i in range(1,4)}
print(a)
a['processor']='i7'
print(a)

'''

# 6 :
# Update the 'price' of the laptop to a new value.

'''
a={i:i**2 for i in range(1,11)}
print(a)
for i in range(1,11):
    a.update({i:i**3})
print(a)

'''

# 7 :
# Use the len() function to find how many key-value pairs are in a dictionary.

'''
a={i:i**2 for i in range(1,11)}
print(a)
print(len(a))

'''

# 8 :
# Create a dictionary where the keys are numbers 1 to 5 and the values are their squares.

'''
a={i:i**2 for i in range(1,6)}
print(a)

'''

# 9 :
# Check if a specific key exists in a dictionary using the 'in' operator.

'''
a={i:i**2 for i in range(1,11)}
print(a)
for i in range(1,21):
    b=i in a
    print(b)

'''

# 10 :
# Delete a key-value pair using the 'del' keyword and handle the case if the key is missing.

'''
a={i:i**2 for i in range(1,11)}
print(a)
del(a)
print(a)

'''

# 11 :
# Use the pop() method to remove a key and store its value in a variable.

'''
a={i:i**2 for i in range(1,11)}
print(a)
for i in range(1,11):
    a.pop(i)
    print(a)

'''

# 12 :
# Use popitem() to remove the last inserted item and explain its behavior in Python 3.7+.

'''
a={i:i**2 for i in range(1,11)}
print(a)
for i in range(1,11):
    a.popitem()
    print(a)

'''

# 13 :
# Use the keys() method to print all the keys in a dictionary.

'''
a={i:i**2 for i in range(1,11)}
print(a)
for k in a.keys():
    print(k)

'''

# 14 :
# Use the values() method to print all the values in a dictionary.

'''
a={i:i**2 for i in range(1,11)}
print(a)
for v in a.values():
    print(v)

'''

# 15 :
# Use the items() method to iterate through a dictionary and print "Key: Value" for each pair.

'''
a={i:i**2 for i in range(1,11)}
print(a)
for k,v in a.items():
    print(f"{k} -- {v}")

'''

# 16 :
# Merge two dictionaries: {'a': 1, 'b': 2} and {'c': 3, 'd': 4} using the update() method.

'''
a= {'a': 1, 'b': 2}
b={'c': 3, 'd': 4}
a.update(b)
print(a)

'''

# 17 :
# Clear all items from a dictionary using the clear() method.

'''
a= {'a': 1, 'b': 2}
print(a)
a.clear()
print(a)

'''

# 18 :
# Use the setdefault() method to add a key 'country' with value 'India' only if it doesn't exist.

'''
a= {'a': 1, 'b': 2}
print(a.setdefault('country','India'))
print(a)

'''

# 19 :
# Create a shallow copy of a dictionary and show that modifying the copy doesn't change the original.

'''
a= {'a':{1:10}, 'b': {2:20}}
b=a.copy()
print(a)
b.update({'a':{3:30}})
print(b)
print(a)

'''

# 20 :
# Create a dictionary from two lists: one for keys and one for values using the zip() function.

'''
a=[i for i in range(1,11)]
b=[i**2 for i in range(1,11)]
c=zip(a,b)
print(c)
print(dict(c))
'''

# 21 :
# Create a nested dictionary called 'Employees' containing data for three different people.

'''
n=int(input("enter how many Employees : "))
a={}
name=[]
salary=[]
age=[]
for i in range(1,n+1):
    n=input(f"enter {i} Employees name :")
    name.append(n)
    s=int(input(f"enter {i} Employees salary :"))
    salary.append(s)
    ag=int(input(f"enter {i} Employees age :"))
    age.append(ag)
    print()
    a.update({i:{"name" : name[i-1],"age" : age[i-1] ,"salary" : salary[i-1]}})
print(a)

'''

# 22 :
# Access a value inside a nested dictionary (e.g., Employees['emp1']['salary']).

'''
a={
    1 : {
        "name" : "najad",
        "age" : 25 ,
        "batch" : "data science",
        "phone" : [[9562020207],[9249730116]]      

    },
    2 : {
        "name" : "yaseen",
        "age" : 26 ,
        "batch" : "data analist" ,
        "phone" : [[9562020207],[9249730116]]      
    },
    3 : {
        "name" : "yaseen",
        "age" : 26 ,
        "batch" : "data analist" ,
        "phone" : [[9562020207],[9249730116]]
    }
}
print("------NAME------")
for k in a:
    print(a[k]["name"])
print()
print("------AGE------")
for k in a:
    print(f"{a[k]["name"]} : {a[k]["age"]}")
print()
print("------BATCH------")
for k in a:
    print(f"{a[k]["name"]} : {a[k]["batch"]}")
print()
print("------PHONE------")
for k in a:
    print(f"{a[k]["name"]} : {a[k]["phone"]}")
    print()
print("------PHONE------")
for k in a:
    for i in range(len(a[k]["phone"])):
        print(f"{a[k]["name"]} : {a[k]["phone"][i]}")

'''

# 23 :
# Update a value inside a nested dictionary.

'''
a={
    1 : {
        "name" : "najad",
        "age" : 25 ,
        "batch" : "data science"
    },
    2 : {
        "name" : "yaseen",
        "age" : 26 ,
        "batch" : "data analist" ,
        "phone" : [9562020207,9249730116]      
    },
    3 : {
        "name" : "yaseen",
        "age" : 26 ,
        "batch" : "data analist" ,
        "phone" : [9562020207,9249730116]
    }
}
a.update({3:{"name" : "aju","age" : 28 ,"batch" : "python" ,"phone" : [9249730116]}})
print(a)
print()
for k,v in a.items():
    print(f"{k} : {v}")
    print()
'''

# 24 :
# Add a new nested dictionary (a new employee) to the existing 'Employees' structure.

'''
a={
    1 : {
        "name" : "najad",
        "age" : 25 ,
        "batch" : "data science"
    },
    2 : {
        "name" : "yaseen",
        "age" : 26 ,
        "batch" : "data analist" ,
        "phone" : [9562020207,9249730116]      
    },
    3 : {
        "name" : "yaseen",
        "age" : 26 ,
        "batch" : "data analist" ,
        "phone" : [9562020207,9249730116]
    }
}
a.update({4:{"name" : "aju","age" : 28 ,"batch" : "python" ,"phone" : [9249730116]}})
print(a)
print()
for k,v in a.items():
    print(f"{k} : {v}")
    print()


'''

# 25 :
# Write a loop to print only the names of all employees from the nested 'Employees' dictionary.

'''
a={
    1 : {
        "name" : "najad",
        "age" : 25 ,
        "batch" : "data science"
    },
    2 : {
        "name" : "yaseen",
        "age" : 26 ,
        "batch" : "data analist" ,
        "phone" : [9562020207,9249730116]      
    },
    3 : {
        "name" : "yaseen",
        "age" : 26 ,
        "batch" : "data analist" ,
        "phone" : [9562020207,9249730116]
    }
}
# for i in range(1,4):
#     print(a[i]["name"])

# for k,v in a.items():
#     print(a[k]["name"])

# for k in a.keys():
#     print(a[k]["name"])

for i in a:
    print(a[i]["name"])

'''

# 26 :
# Create a dictionary where a key points to a list of values (e.g., 'hobbies': ['coding','reading']).

'''
print("--------hobbies--------")
a=int(input("how many students : "))
b={}
for i in range(1,a+1):
    name=input(f"enter tha name of {i} student : ")
    print("enter 3 hobbies :")
    c=[]
    for j in range(1,4):
       d= input(f"{j} : ")
       c.append(d)
    b.update({i:{"name":name , "hobbies":c}})
print(b)

'''

# 27 :
# Append a new hobby to the list inside that dictionary.

'''
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
a["student1"].update({"hobby":"footbool"})
a["student2"].update({"hobby":"hoki"})
print(a["student1"])
print(a["student2"])

'''

# 28 :
# Given a dictionary of students and their marks (a list), calculate the average marks for one student.

'''

print("--------student mark list--------")
a=int(input("how many students : "))
b={}
for i in range(1,a+1):
    name=input(f"enter tha name of {i} student : ")
    maths=int(input("enter tha mark in maths : "))
    english=int(input("enter tha mark in english : "))
    science=int(input("enter tha mark in science : "))
    social=int(input("enter tha mark in social : "))
    malayalam=int(input("enter tha mark in malayalam : "))
    average=(maths + english + science + social + malayalam)/5
    b.update({i:{"name":name , "maths":maths,"english":english,"science":science,"social ":social, "malayalam":malayalam,"average":average}})
    print()
    # b[i].append({"name":name , "maths":maths,"english":english,"science":science, "malayalam":malayalam,"average":average})
    # {i:{"name":name , "maths":maths,"english":english,"science":science, "malayalam":malayalam,"average":average}}
# print(b)
for k,v in b.items():
    s=0
    for i,j in v.items():
        # print(v)
        if i=="name":
            continue
        elif i=="average":
            continue
        else:
            # print(v[i])
            s+=v[i]
    print(f"average mark {b[k]["name"]} : {s/5}")

'''

# 29 :
# Flatten a simple nested dictionary (convert {'a': {'b': 1}} to {('a', 'b'): 1}).

'''
a={'a': {'b': 1},'b':{'c':2},'d':{'e':3}}
d={}
for k,v in a.items():
    for i,j in v.items():
        c={(*list(k),*a[k]):a[k][i]}
        d.update(c)
print(a)
print(d)

'''

# 30 :
# Represent a JSON response from a weather API as a nested dictionary and extract the 'temperature'.

'''
weather = {
    "location": {
        "city": "Kochi",
        "country": "India"
    },
    "current": {
        "weather": "Sunny",
        "temperature": 32,
        "humidity": 70
    }
}
print(f"{weather['location']["city"]} : {weather["current"]["temperature"]}")

'''

# 31 : 
# [Comprehension] Create a dictionary of even numbers between 1-10 as keys and their cubes as values.

'''
a={i:i**3 for i in range(1,11) if i%2==0}
print(a)

'''

# 32 :
# [Comprehension] Given a dictionary, create a new one with only items where the value is > 100.

'''
a={chr(x):x for x in range(97,123)}
b={k:v for k,v in a.items() if v>100 }
print(a)
print(b)

'''

# 33 : 
# [Comprehension] Swap keys and values in a dictionary (Reverse Mapping).

'''
a={chr(x):x for x in range(97,123)}
b={v:k for k,v in a.items()}
print(a)
print(b)

'''

# 34 : 
# Sort a dictionary by its keys in alphabetical order.

'''

a={"name" : "richu" , "age" : 22 , "place" : "calicut" }
# print(a)
# print(sorted(a))
# print(a.items())
# print(sorted(a.items()))
print(dict(sorted(a.items())))

'''
'''

a={"name" : "richu" , "age" : 22 , "place" : "calicut" }
b=[]
c={}
for i in a:
    b.append(i)
b.sort()
print(b)
for i in b:
    c.update({i:a[i]})
print(c)

'''

# 35 :
# Sort a dictionary by its values in ascending order.

'''
a={chr(x):x for x in range(122,96,-1)}
b=list(a.items())
c=len(b)
print(a)
print(b)
for i in range(c):
    for j in range(1,c-i):
        if b[j][1]<b[j-1][1]:
            d=b[j]
            b[j]=b[j-1]
            b[j-1]=d    
e=dict(b) 
print(b)
print(c)
print(e)

'''

# 36 :
# Find the key with the maximum value in a dictionary of product prices.

'''
a={chr(x):x**2 for x in range(97,123)}
print(a)
b=list(a.items())
c=len(b)
for i in range(c):
    for j in range(1,c):
        if b[j][1]>b[j-1][1]:
            d=b[j]
e=[]
e.append(d)
print(dict(e))

'''

# 37 :
# Count the frequency of each character in a string "Python Trainer" using a dictionary.

'''
a="Python Trainer"
b={}
for i in a:
    b.update({i:a.count(i)})
print(b)
print()
for k,v in b.items():
    print(f"{k} : {v}")
    print()

'''
'''
a=input("enter a string : ")
b={}
for i in a:
    b.update({i:a.count(i)})
print(b)
print()
for k,v in b.items():
    print(f"{k} : {v}")
    print()

'''
'''
a=input("enter a string : ")
b={i:a.count(i) for i in a}
print(b)
for k,v in b.items():
    print(f"{k} : {v}")

'''

# 38 :
# Combine two dictionaries by adding values for common keys.

'''
a={i:i**2 for i in range(1,16)}
b={i:i**2 for i in range(10,21)}
print(a)
print(b)
for k,v in a.items():
    if k in b:
        a[k]+=b[k]
for k,v in b.items():
    if not k in a:
          a[k]=v     
print(a)

'''

# 39 :
# Convert a dictionary into a list of tuples.

'''
a={x:x**2 for x in range(1,11)}
print(tuple(a.items()))

'''

# 40 :
# Check if all values in a dictionary are the same.

'''
a ={i:10 for i in range(1,10)}
b=len(set(a.values())) == 1
print(b)

'''

# 41 :

# '''


# '''

# 42 :

# '''


# '''

# 43 :

# '''


# '''

# 44 :

# '''


# '''

# 45 :

# '''


# '''

# 46 :

# '''


# '''

# 47 :

# '''


# '''

# 48 :

# '''


# '''

# 49 :

# '''


# '''

# 50 :

# '''


# '''

