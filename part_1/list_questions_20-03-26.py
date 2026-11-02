
'''
Python Data Structures (Lists) – Lab Practical
-------------------------------------------------
Question Bank
Beginner → Advanced + Logical & Interview-Oriented Questions

Section 1: Beginner Level
-------------------------------
1 1. Create a list of five integers and print all elements using a for loop.
2 2. Write a program to find the length of a list without using len().
3 3. Create a list of numbers and print the maximum and minimum values.
4 4. Write a program to append a new element to a list entered by the user.
5 5. Insert an element at a specific position in a list.
6 6. Remove an element from a list using remove() and pop().
7 7. Write a program to check whether a given element exists in a list.
8 8. Reverse a list without using reverse().
9 9. Sort a list of numbers in ascending and descending order.
10 10. Create a list of numbers and print only the even numbers.
11 11. Count how many times a specific element appears in a list.
12 12. Write a program to copy one list into another list.
13 13. Concatenate two lists using the + operator.
14 14. Repeat a list three times using the * operator.
15 15. Demonstrate positive and negative indexing in a list.

Section 2: Intermediate Level
-----------------------------------------

1 16. Write a program to remove duplicates from a list.
2 17. Find the second largest element in a list.
3 18. Write a program to rotate a list to the left by one position.
4 19. Write a program to rotate a list to the right by one position.
5 20. Move a specific element (e.g., 50) to the first position of a list.
6 21. Create a list of squares of numbers from 1–10 using list comprehension.
7 22. Create a list containing only odd numbers from 1–50 using list comprehension.
8 23. Write a program to merge two lists and remove duplicates.
9 24. Find the sum of all elements in a list without using sum().
10 25. Write a program to find common elements between two lists.
11 26. Write a program to split a list into two halves.
12 27. Find the index of a given element without using index().
13 28. Write a program to flatten a nested list.
14 29. Create a program to find the frequency of each element in a list.
15 30. Reverse each element of a list of strings.

Section 3: Advanced Level
-----------------------------
1 31. Implement a matrix using nested lists and print it in matrix format.
2 32. Write a program to add two matrices using nested lists.
3 33. Write a program to transpose a matrix.
4 34. Flatten a 2D list into a single list using list comprehension.
5 35. Find the largest sublist length in a nested list.
6 36. Write a program to find the intersection of multiple lists.
7 37. Write a program to group list elements by their length (strings).
8 38. Implement a simple stack using a Python list.
9 39. Implement a queue using a Python list.
10 40. Write a program to shuffle elements in a list.
11 41. Write a program to find the kth largest element in a list.
12 42. Write a program to check whether a list is a palindrome.
13 43. Write a program to generate all possible pairs from a list.
44. Create a list of prime numbers within a given range using list comprehension.
45. Write a program to remove all negative numbers from a list.

Section 4: Logical / Problem Solving
-------------------------------------
1 46. Given a list of numbers, move all zeros to the end while maintaining order.
2 47. Find the first non-repeating element in a list.
3 48. Find the highest frequency element in a list.
4 49. Find all pairs whose sum equals a given target value.
5 50. Write a program to detect duplicates in a list.
6 51. Given two lists, determine whether they contain the same elements regardless of order.
7 52. Write a program to partition a list into even and odd numbers.
8 53. Implement bubble sort using lists.
9 54. Implement selection sort using lists.
10 55. Write a program to remove consecutive duplicate elements.

Section 5: Interview-Oriented Questions
-------------------------------------------
1 56. Explain the difference between list.copy() and copy.deepcopy(). Demonstrate with code.
2 57. What is list comprehension? Write examples and compare it with loops.
3 58. What happens when you modify a list during iteration? Demonstrate with an example.
4 59. Explain the difference between append(), extend(), and insert().
5 60. Demonstrate shallow copy behavior using lists.
6 61. Explain time complexity of list operations (append, insert, pop).
7 62. Write a program to implement a stack using a list and explain push/pop.
8 63. Write a program to remove duplicates while preserving order.
9 64. Explain the difference between mutable and immutable data structures in Python.
10 65. Write a Python program to simulate a simple task queue using lists
'''
# for i  in range(1,66):
#     print(f"# {i} : ")
#     print()
#     print()


# 1 :
# Create a list of five integers and print all elements using a for loop. 

'''
a=[i for i in range(1,6)]
for i in a:
    print(i)

'''

# 2 :
# Write a program to find the length of a list without using len().

'''
a=[i for i in range(100)]
b=0
for i in a:
    b+=1
print(f"length of a list : {b}")

'''

# 3 :
# Create a list of numbers and print the maximum and minimum values.

'''
a=[10,16,1,2,8,-4,8,5,0,15,7,3,-10]
minimum=a[0]
maximum=a[0]
for i in a:
    if minimum>i:
        minimum=i
    if maximum<i:
        maximum=i   
print(minimum)
print(maximum)

'''
'''
a=[16,1,2,8,-4,8,5,0,15,7,3,-10]
print(max(a))
print(min(a))

'''

# 4 :
# Write a program to append a new element to a list entered by the user.

'''
a=[]
b="y"
while b=="y" or b=="Y":
    c=input("enter append a new element to a list :")
    a.append(c)
    b=input("do you want continue (y/n) :")
print(a)

'''

# 5 :
# Insert an element at a specific position in a list.

'''
a=[i for i in range(11)]
a.insert(2,10)
print(a)

'''

# 6 :
# Remove an element from a list using remove() and pop().

'''
a=[i for i in range(21)]
for i in range(5):
    a.pop()
    print(a)
for i in range(5):
    a.pop(i)
    print(a)
# a.pop(15)  #error
# a.remove()  #error
a.remove(15)
print(a)
# a.remove(14,13) #error

'''

# 7 :
# Write a program to check whether a given element exists in a list.

'''
a=[i for i in range(101)]
print(a)
b=int(input("enter a intgar :"))
if b in a:
    print(f"{b} exists in a list")
else:
    print(f"{b} not exists in a list")

'''

# 8 :
# Reverse a list without using reverse().

'''
a=[i for i in range(21)]
print(a[::-1])

for i in range(len(a)-1,-1,-1):
    print(a[i], end=" ")
'''

# 9 :
# Sort a list of numbers in ascending and descending order.

'''
a=[1,20,1,3,5,7,8,64,5,-11]
for i in range(len(a)):
    b=0
    for j in range(1,len(a)):
        if a[j]<a[j-1]:
            b=a[j]
            a[j]=a[j-1]
            a[j-1]=b
print(a)
print(a[::-1])

'''
'''
a=[1,20,1,3,5,7,8,64,5,-11]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

'''

# 10 :
# Create a list of numbers and print only the even numbers.

'''
a=[i for i in range(101)]
b=[i for i in a if i%2==0]
print(b)

'''

# 11 :
# Count how many times a specific element appears in a list.

'''
a=[1,2,1,2,3,4,2,1,5,2]
for i in a:
    print(f"{i} cound : {a.count(i)}")

'''

# 12 :
# Write a program to copy one list into another list.

'''
a=[i for i in range(5)]
b=a.copy()
print(b)

'''

# 13 :
# Concatenate two lists using the + operator.

'''
a=[i for i in range(4)]
b=[i for i in range(4,9)]
print(a+b)

'''

# 14 :
# Repeat a list three times using the * operator.

'''
a=[i for i in range(4)]
print(a*3)

'''

# 15 :
# Demonstrate positive and negative indexing in a list.

'''
a=[i for i in range(-10,11)]
b=[i for i in a if i>=0]
c=[i for i in a if i<0]
print(a)
print(b)
print(c)

'''

# 16 :
# Write a program to remove duplicates from a list.

'''
a=[1,2,3,4,5,2,1,2,1,3,4,6]
b=[]
for i in a:
    if not i in b:
        b.append(i)
print(b) 

'''
'''
a=[1,2,3,4,5,2,1,2,1,3,4,6]
print(list(set(a)))

'''

# 17 :
# Find the second largest element in a list.
'''

a=[1,5,6,8,1,4,5,6,9,9]
a.sort()

# print(a[-2])

l=len(a)
for i in range(l-1,0,-1):
    if a[i]>a[i-1]:
        print(a[i-1])
        break

m=max(a)
for i in range(l-1,0,-1):
    if a[i]!=m:
        print(a[i])
        break

s=[1,2,5,6,8,9,9]
large=0
s_large=0
for i in range(len(s)):
    if s[i]>large:
        s_large=large
        large=s[i]
    elif large > s[i] > s_large :
        s_large=s[i]
print (s_large)

'''

# 18 :
# Write a program to rotate a list to the left by one position.

'''
a=[i for i in range(1,21)]
b=a[1:]+a[:1]
print(b)

'''
'''
a=[i for i in range(1,21)]
b=[]
for i in range(1,len(a)):
    b.append(a[i])
b.append(a[0])
print(a)
print(b)

'''

# 19 :
# Write a program to rotate a list to the right by one position.

'''
a=[i for i in range(1,21)]
b=a[-1:]+a[:-1]
print(b)

'''
'''
a=[i for i in range(1,21)]
b=[]
b.append(a[-1])
for i in range(len(a)-1):
    b.append(a[i])
print(b)

'''

# 20 :
# Move a specific element (e.g., 50) to the first position of a list.

'''
a=[i for i in range(1,101)]
a.insert(0,50)
print(a)
'''

# 21 :
# Create a list of squares of numbers from 1–10 using list comprehension.

'''
a=[i**2 for i in range(1,11)]
print(a)

'''


# 22 :
# Create a list containing only odd numbers from 1–50 using list comprehension.

'''
a=[i for i in range(1,50) if i%2==1]
print(a)

'''
'''
a=["odd" if i%2==1 else "even" for i in range(1,50)]
print(a)

'''


# 23 :
# Write a program to merge two lists and remove duplicates.

'''
a=[i for i in range(1,80)]
b=[i for i in range(40,101)]
c=[]
for i in range(len(a)):
    if not a[i] in c:
        c.append(a[i])
for i in range(len(b)):
    if not b[i] in c:
        c.append(b[i])
print(c)
print(len(c))

'''
'''
a=[i for i in range(1,80)]
b=[i for i in range(40,101)]
c=list({*a,*b})
print(c)
print(len(c))

'''

# 24 :
# Find the sum of all elements in a list without using sum().

'''
a=[i for i in range(11)]
b=0
for i in a:
    b+=i
print(b)

'''

# 25 :
# Write a program to find common elements between two lists.

'''
a=[1,2,3,4,5,6]
b=[4,5,6,7,8,9]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)

'''
'''
a=[1,2,3,4,5,6]
b=[4,5,6,7,8,9]
print(list(set(a)&set(b)))

'''

# 26 :
# Write a program to split a list into two halves.

'''
a=[i for i in range(1,101)]
b=[]
c=[]
d=int((len(a))/2)
for i in range(d):
    b.append(a[i])
    c.append(a[i+d])
print(f"{b}\n{c}")

'''


# 27 :
# Find the index of a given element without using index().
 
'''
a=(10,20,30,40,50,60,70)
for i,j in enumerate(a):
    print(i,j)
print(enumerate(a))
print(list(enumerate(a)))
print(tuple(enumerate(a)))
print(set(enumerate(a)))

'''
'''
a=(10,20,30,40,50,60,70)
for i in range(len(a)):
    print(f"index {i} = {a[i]}")

'''

# 28 :
# Write a program to flatten a nested list.

'''
a=[1,2,3,[4,5],[6,7,[8,9],10],11]
b=[]
for i in a:
    if isinstance(i,list):
        for j in i :
            if isinstance(j,list):
                for k in j :
                    b.append(k)
            else:
                b.append(j)
    else:
        b.append(i)
print(b)

'''


# 29 :
# Create a program to find the frequency of each element in a list.

'''
a=["najad","aju","fazil"]
for i in a:
    print(f"{i} - frequency - {len(i)}")

'''


# 30 :
# Reverse each element of a list of strings.

'''

a=["najad","aju","fazil"]
print(a)
for i in range(len(a)):
    b=""
    for j in range(len(a[i])):
        b=a[i][j]+b
    a[i]=b
print(a)
    
'''

# 31 :
# Implement a matrix using nested lists and print it in matrix format.

'''
print("enter the size of matrix (lenth and width):")
a=[]
x=int(input())
y=int(input())
print(f"enter tha elament of materix {x} * {y} :")
for i in range(x):
    b=[]
    for j in range(y):
        c=int(input())
        b.append(c)
    a.append(b)
for i in range(x):
    print(a[i])
 '''         

# 32 :
# Write a program to add two matrices using nested lists.

'''
print("addition and subtraction two matrices")
print("enter the size of matrix (lenth and width):")
a=[]
d=[]
e=[]
x=int(input())
y=int(input())
print(f"enter tha elament of 1st materix {x} * {y} :")
for i in range(x):
    b=[]
    for j in range(y):
        c=int(input())
        b.append(c)
    a.append(b)
print(f"enter tha elament of 2st materix {x} * {y} :")
for i in range(x):
    b=[]
    for j in range(y):
        c=int(input())
        b.append(c)
    d.append(b)
# print(a)
# print(d)
print("tha elament of 1st materix")
for i in range(x):
    print(a[i])
print("tha elament of 2st materix")
for i in range(x):
    print(d[i])

for i in range(x):
    f=[]
    for j in range(y):
        f.append(a[i][j]+d[i][j])
    e.append(f)

print("tha addition of 2 materix")
for i in range(x):
    print(e[i])
e.clear()
for i in range(x):
    f=[]
    for j in range(y):
        f.append(a[i][j]-d[i][j])
    e.append(f)

print("tha subtraction of 2 materix")
for i in range(x):
    print(e[i])

'''

# 33 :
# Write a program to transpose a matrix.

'''
print("a program to transpose a matrix.")
print("enter the size of matrix (lenth and width):")
a=[]
d=[]
e=[]
x=int(input())
y=int(input())
print(f"enter tha elament of 1st materix {x} * {y} :")
for i in range(x):
    b=[]
    for j in range(y):
        c=int(input())
        b.append(c)
    a.append(b)
print(f"enter tha elament of 2st materix {x} * {y} :")
for i in range(x):
    b=[]
    for j in range(y):
        c=int(input())
        b.append(c)
    d.append(b)
print("tha elament of 1st materix")
for i in range(x):
    print(a[i])
print("tha elament of 2st materix")
for i in range(x):
    print(d[i])
a,d=d,a
print("transpose a matrix.")
print("tha elament of 1st materix")
for i in range(x):
    print(a[i])
print("tha elament of 2st materix")
for i in range(x):
    print(d[i])

'''


# 34 :
# Flatten a 2D list into a single list using list comprehension.

'''
a=[[1,2,3],[4,5,6],"najad"]
b=[j for i in range(len(a)) for j in a[i]]
print(b)


'''

# 35 :
# Find the largest sublist length in a nested list.

'''
a=[1,[1,2],[1,2,4,5,6],[5,6,7],5,4]
b=len(a)
d=0
for i in range(b):
    if isinstance(a[i],list):
        c=len(a[i])
        if d<c:
            d=c
print(f"largest sublist length in a nested list : {d}")

'''

# 36 :
# Write a program to find the intersection of multiple lists.

'''
a=[i for i in range(1,101)]
b=[i for i in range(80,121)]
c=[i for i in a if i in b]
print(c)

'''

# 37 :
# Write a program to group list elements by their length (strings).

''' 
a=input("enter a string : ")
print(f"elements by their length : {len(a.split())}")

'''      

# 38 :
# Implement a simple stack using a Python list.

'''
a=[]
n=1
while n==1:
    print("1.Pushed a intgre value \n2.Poped a intgre value \n3.disply a  values ")
    b=int(input("enter your option :"))
    if b==1:
        c=int(input("enter hwo many no : "))
        print("enter tha no :")
        for i in range(c):
            d=int(input())
            a.append(d)
        a.sort()
        print(f"the list : {a}")
        print(f"Top element : {a[-1]}")
        print(f"botam element : {a[0]}")
    elif b==2:
        c=int(input("enter Poped a intgre value : "))
        if c in a:
            a.remove(c)
        else:
            print("enter Poped a intgre value not in list : ")
        print(f"Poped list : {a}")
        print(f"Top element : {a[-1]}")
        print(f"botam element : {a[0]}")
    elif b==3:
        print(f"the list : {a}")
        if len(a)>0:
            print(f"Top element : {a[-1]}")
            print(f"botam element : {a[0]}")
    n=int(input("do you want repet (1.yas , 2.no) : "))

'''
# 39 :
# Implement a queue using a Python list.

# '''


# '''

# 40 :
# Write a program to shuffle elements in a list.

# '''


# '''

# 41 :
# Write a program to find the k th largest element in a list.

'''
a=[]
c=int(input("enter hwo many no : "))
print("enter tha no :")
for i in range(c):
    d=int(input())
    a.append(d)
print(a)
a.sort()
print(f"sortrd list : {a}")
b=int(input("entar the k th largest : "))
d=list(set(a))
d.sort()
e=len(d)
if e>=b:
    print(f"entar the {b} th largest : {a[b]}")
else:
    print("Invalid k value")

'''

# 42 :
# Write a program to check whether a list is a palindrome.

# '''


# '''

# 43 :Write a program to generate all possible pairs from a list.

# '''


# '''

# 44 :
# Create a list of prime numbers within a given range using list comprehension.

'''

a=[i for i in range(122) if i >1 and not any(i % j == 0 for j in range(2,i))]
b=[i for i in range(122) if i >1 and all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
print(a)
print(b)

'''

# 45 :
# Write a program to remove all negative numbers from a list.

'''
a=[i for i in range(-10,11)]
b=[i for i in a if i>=0]
print(b)

'''

# 46 :


# 47 :


# 48 :


# 49 :


# 50 :


# 51 :


# 52 :


# 53 :


# 54 :


# 55 :


# 56 :


# 57 :


# 58 :


# 59 :


# 60 :


# 61 :


# 62 :


# 63 :


# 64 :


# 65 :







