
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


# 2 :


# 3 :


# 4 :


# 5 :


# 6 :


# 7 :


# 8 :


# 9 :


# 10 :


# 11 :


# 12 :


# 13 :


# 14 :


# 15 :


# 16 :


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


# 19 :


# 20 :


# 21 :


# 22 :


# 23 :


# 24 :


# 25 :


# 26 :


# 27 :


# 28 :


# 29 :


# 30 :


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


# 36 :


# 37 :


# 38 :


# 39 :


# 40 :


# 41 :


# 42 :


# 43 :


# 44 :


# 45 :


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







