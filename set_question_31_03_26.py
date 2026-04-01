'''
Python Lab Practical Questions
-----------------------------------
Topic: Sets in Python (Beginner → Advanced)
---------------------------------------------

Section 1 – Basic Set Programs
-----------------------------------

1. Create a set containing 5 numbers and print the set.
2. Create a set with mixed data types and print each element.
3. Write a program to create a set from a list.
4. Write a program to remove duplicate elements from a list using a set.
5. Create an empty set and add three elements to it.
6. Write a program to check if an element exists in a set.
7. Create a set and print all elements using a for loop.
8. Write a program to find the length of a set without using len().
9. Write a program to convert a tuple into a set.
10. Write a program to convert a set into a list.

Section 2 – Adding and Removing Elements
--------------------------------------------

11. Create a set and add a new element using add().
12. Write a program to add multiple elements to a set using update().
13. Write a program to remove an element using remove().
14. Write a program to remove an element using discard().
15. Write a program to remove a random element using pop().
16. Write a program to clear all elements from a set.
17. Write a program to copy a set into another set.
18. Write a program to add elements from a list into a set.
19. Write a program to add elements from a tuple into a set.
20. Write a program to update a set with another set.

Section 3 – Set Operations
-----------------------------

21. Write a program to find the union of two sets.
22. Write a program to find the intersection of two sets.
23. Write a program to find the difference between two sets.
24. Write a program to find the symmetric difference between two sets.
25. Write a program to update a set using intersection_update().
26. Write a program to update a set using difference_update().
27. Write a program to update a set using symmetric_difference_update().
28. Write a program to check if one set is a subset of another set.
29. Write a program to check if one set is a superset of another set.
30. Write a program to check if two sets are disjoint.

Section 4 – Logical Set Problems
-----------------------------------

31. Write a program to find common elements between two lists using sets.
32. Write a program to find unique elements from two lists.
33. Write a program to find elements present in the first list but not in the second list.
34. Write a program to remove duplicates from a sentence using sets.
35. Write a program to find unique characters in a string using sets.
36. Write a program to count unique words in a sentence.
37. Write a program to find the difference between two strings using sets.
38. Write a program to find vowels present in a string using sets.
39. Write a program to check whether two strings contain the same characters.
40. Write a program to find common characters between two strings.

Section 5 – Set Comprehension
----------------------------------

41. Write a program to create a set of squares from numbers 1–10 using set
comprehension.
42. Write a program to create a set of cubes using set comprehension.
43. Write a program to create a set of even numbers from 1–20 using set comprehension.
44. Write a program to create a set of odd numbers using set comprehension.
45. Write a program to create a set containing lengths of words in a sentence.

Section 6 – Industry Based Problems
---------------------------------------

46. Given two sets representing students enrolled in Python and Java, find students
enrolled in both courses.
47. Given two sets representing users who logged in today and yesterday, find new users
today.
48. Given two sets representing available skills and required job skills, find missing skills.
49. Create a set representing product categories in an e-commerce system and remove a
category dynamically.
50. Given two datasets of email IDs, remove duplicates and print all unique email IDs.

Bonus Interview Questions
---------------------------

1. Why are sets unordered in Python?
2. What is the difference between remove() and discard()?
3. Why can't sets contain mutable elements like lists?
4. What is the difference between difference() and difference_update()?
5. When should sets be used instead of lists in real-world applications?

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
# Create a set containing 5 numbers and print the set.

'''
a={i for i in range(1,6)}
print(a)

'''

# 2 :
# Create a set with mixed data types and print each element.

'''
a={1,2,"najad",(1,2)}
print(a)

'''

# 3 :
# Write a program to create a set from a list.

'''
a=[1,1,2,4,3,3,4,5,5]
print(set(a))

'''

# 4 :
# Write a program to remove duplicate elements from a list using a set.

'''
a=[1,1,2,4,3,3,4,5,5]
print(list(set(a)))

'''

# 5 :
# Create an empty set and add three elements to it.

'''
a=set()
for i in range(3):
    b=input("enter a string :")
    a.add(b)
print(a)

'''

# 6 :
# Write a program to check if an element exists in a set.

'''
a={1,2,3,4,5,6,7,8}
b=int(input("enter checking element :"))
c=0
for i in a:
    if i==b:
        print("element exists in a set")
        c+=1
if c==0:
    print("element not exists in a set")

'''

# 7 :
# Create a set and print all elements using a for loop.

'''
a={i if i%10==0 else 5 for i in range(1,101)}
b=0
for i in a:
    print(i)

'''

# 8 :
# Write a program to find the length of a set without using len().

'''
a={i if i%10==0 else 5 for i in range(1,101)}
b=0
for i in a:
    b+=1
print(f"length of a set : {b}")

'''

# 9 :
# Write a program to convert a tuple into a set.

'''
a={1,1,2,3,(1,2,3)}
b=(*a,)
print(b)

'''
'''
a={1,1,2,3,(1,2,3)}
b=[]
for i in a:
    b.append(i)
print(tuple(b))

'''

# 10 :
# Write a program to convert a set into a list. 

'''
a={1,1,2,3,(1,2,3)}
b=[*a,]
print(b)

'''

# 11 :
# Create a set and add a new element using add().

'''
a=set()
a.add(5)
a.add("najad")
# a.add({"naju"})      #erroe
a.add((7,6))
print(a)

'''

# 12 :
# Write a program to add multiple elements to a set using update().

'''
a=set()
a.update("najad","aju","rciju")
a.update({"najad"},{"aju"})
# a.update(5)     #error
a.update()
print(a)

'''

# 13 :
# Write a program to remove an element using remove().

'''
a={10,20,30,40}
a.remove(20)
# a.remove(60)     #error
print(a)

'''

# 14 :
# Write a program to remove an element using discard().

'''
a={10,20,30,40}
a.discard(20)
a.discard(60)
print(a)

'''

# 15 :
# Write a program to remove a random element using pop().

'''
a={10,20,30,40}
print(a)
a.pop()
print(a)
a.pop()
print(a)

'''

# 16 :
# Write a program to clear all elements from a set.

'''
a={10,20,30,40}
print(a)
a.clear()
print(a)

'''

# 17 :
# Write a program to copy a set into another set.

'''
a={10,20,30,40,(10,20,30)}
b=set()
b=a.copy()
print(b)

'''

# 18 :
# Write a program to add elements from a list into a set.

'''
a=[10,20,30,"najad",(1,2)]
b=set()
for i in a:
    b.add(i)
print(b)

'''
'''
a=[10,20,30,"najad",(1,2)]
b=set()
for i in a:
    b=b|{i}
print(b)

'''
'''
a=[10,20,30,"najad",(1,2)]
b={i for i in a}
print(b)

'''
'''
a=[10,20,30,"najad",(1,2)]
b={*a}
print(b)

'''
'''
a=[10,20,30,"najad",(1,2)]
b=set(a)
print(b)

'''


# 19 :
# Write a program to add elements from a tuple into a set.

'''
a={10,20,30,40,(10,20,30)}
b=set()
b=a.copy()
print(b)

'''

# 18 :
# Write a program to add elements from a list into a set.

'''
a=(10,20,30,"najad",(1,2))
b=set()
for i in a:
    b.add(i)
print(b)

'''
'''
a=(10,20,30,"najad",(1,2))
b=set()
for i in a:
    b=b|{i}
print(b)

'''
'''
a=(10,20,30,"najad",(1,2))
b={i for i in a}
print(b)

'''
'''
a=(10,20,30,"najad",(1,2))
b={*a}
print(b)

'''
'''
a=(10,20,30,"najad",(1,2))
b=set(a)
print(b)

'''

# 20 :
# Write a program to update a set with another set.

'''
a={10,20,30,"najad",(1,2)}
b={100,200}
for i in a:
    b.update({i})
print(b)

'''
'''
a={10,20,30,"najad",(1,2)}
b={100,200}
for i in a:
    b=b|{i}
print(b)

'''
'''
a={10,20,30,"najad",(1,2)}
b={100,200}
b=b|a
print(b)

'''
'''
a={10,20,30,"najad",(1,2)}
b={100,200}
b|=a
print(b)

'''
'''
a={10,20,30,"najad",(1,2)}
b={100,200}
b={*b,*a}
print(b)

'''

# 21 :
# Write a program to find the union of two sets.

'''
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.union(b))
print(a|b)

'''

# 22 :
# Write a program to find the intersection of two sets.

'''
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.intersection(b))
print(a&b)

'''

# 23 :
# Write a program to find the difference between two sets.

'''
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.difference(b))
print(a-b)
print(b.difference(a))
print(b-a)

'''

# 24 :
# Write a program to find the symmetric difference between two sets.

'''
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.symmetric_difference(b))
print(a^b)

'''

# 25 :
# Write a program to update a set using intersection_update().

'''
a={1,2,3,4,5}
b={4,5,6,7,8}
a.intersection_update(b)
print(a)

'''

# 26 :
# Write a program to update a set using difference_update().

'''
a={1,2,3,4,5}
b={4,5,6,7,8}
a.difference_update(b)
print(a)

'''

# 27 :
# Write a program to update a set using symmetric_difference_update().

'''
a={1,2,3,4,5}
b={4,5,6,7,8}
a.symmetric_difference_update(b)
print(a)

'''

# 28 :
# Write a program to check if one set is a subset of another set.


'''
a={1,2,3,4,5}
b={4,5,}
c={5,6}
print(b.issubset(a))
print(c.issubset(a))

'''

# 29 :
# Write a program to check if one set is a superset of another set.

'''
a={1,2,3,4,5}
b={4,5,}
c={5,6}
print(a.issuperset(b))
print(a.issuperset(c))

'''

# 30 :
# Write a program to check if two sets are disjoint.

'''
a={1,2,3,4,5}
b={4,5,}
c={5,6}
d={6,7}
print(a.isdisjoint(b))
print(a.isdisjoint(c))
print(a.isdisjoint(d))
print(d.isdisjoint(a))

'''

# 31 :
# Write a program to find common elements between two lists using sets.

'''
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a|b
print(c)

'''

# 32 :
# Write a program to find unique elements from two lists.

'''
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a^b
print(c)

'''

# 33 :
# Write a program to find elements present in the first list but not in the second list.

'''
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a-b
print(c)

'''

# 34 :
# Write a program to remove duplicates from a sentence using sets.

'''
a=[0,1,2,2,4,1,5,2,3,4]
print(list(set(a)))

'''

# 35 :
# Write a program to find unique characters in a string using sets.

'''
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a&b
print(c)

'''

# 36 :
# Write a program to count unique words in a sentence.

'''
a=input("enter a string : ")
b=a.split(" ")
c=len(b)
d=set(b)
j=0
print(d)
for i in d:
    j+=1
if c==j:
    print("the string contains unique words")
else:
    print("the string contains  not unique words")

'''

# 37 :
# Write a program to find the difference between two strings using sets.

'''
a=input("enter 1st string : ")
b=input("enter 2nd string : ")
c=set(a.split())^set(b.split())
print(c)

'''

# 38 :
# Write a program to find vowels present in a string using sets.

'''
a=input("enter a string : ")
b=set()
j=0
b.update(a)
for i in b:
    if i in "aeiouAEIOU":
        j+=1
if j==0:
    print("vowels is not present in a string")
else:
    print("vowels is present in a string")

'''

# 39 :
# Write a program to check whether two strings contain the same characters.

'''
a=input("enter 1st string : ")
b=input("enter 2nd string : ")
a=a.lower()
b=b.lower()
if set(a) == set(b):
    print("Strings contain the same characters")
else:
    print("Strings do NOT contain the same characters")

'''

# 40 :
# Write a program to find common characters between two strings.

'''
a=input("enter 1st string : ")
b=input("enter 2nd string : ")
a=a.lower()
b=b.lower()
c=set(a) & set(b)
print(c)

'''

# 41 :
# Write a program to create a set of squares from numbers 1–10 using set
# comprehension.

'''
a={i for i in range(1,11)}
print(a)

'''

# 42 :
# Write a program to create a set of cubes using set comprehension.

'''
a={i**3 for i in range(1,11)}
print(a)

'''

# 43 :
# Write a program to create a set of even numbers from 1–20 using set comprehension.

'''
a={i for i in range(1,21) if i%2==0}
print(a)

'''

# 44 :
# Write a program to create a set of odd numbers using set comprehension.

'''
a={i for i in range(1,21) if i%2==1}
print(a)

'''

# 45 :
# Write a program to create a set containing lengths of words in a sentence.

'''
set1=("richu","najad","shabin","aju","fazil","asif")
a={len(i) for i in set1}
print(a)

'''

# 46 :
# Given two sets representing students enrolled in Python and Java, find students
# enrolled in both courses.

'''
python={"najad","aju","richu","fazil"}
java={"najad","ashif","nihal","aju"}
print(f"students enrolled in both courses : {python&java}")

'''

# 47 :
# Given two sets representing users who logged in today and yesterday, find new users
# today.

'''
loging_today={"najad","aju","richu","fazil"}
loging_yesterday={"najad","ashif","nihal","aju"}
print(f"new users today : {loging_today-loging_yesterday}")

'''

# 48 :
# Given two sets representing available skills and required job skills, find missing skills.

'''
available_skills={"MS Office","Python","Analytical thinking","Accounting",}
required_job_skills={"Python","Java","Data analysis","Accounting","Digital marketing"}
print(f"missing skills : {required_job_skills-available_skills}")


'''

# 49 :
# Create a set representing product categories in an e-commerce system and p

'''
categories={"Mobile phones","Laptops & computers","Cameras","Men’s clothing","Kids’ wear","Footwear","Furniture"}
print(f"categories : {categories}")
b=input("enter remove category : ")
categories.discard(b)
print(f"categories : {categories}")

'''

# 50 :
# Given two datasets of email IDs, remove duplicates and print all unique email IDs.

'''
a=[]
b=int(input("enter  how many email IDs :"))
for i in range(b):
    c=input(f"enter tha {i+1} email ID :")
    a.append(c)
a=set(a)
print("the email IDs")
for i in a:
    print(i)

'''









