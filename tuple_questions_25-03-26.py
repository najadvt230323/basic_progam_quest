'''

PYTHON FULL STACK TRAINING: TUPLE LOGIC & INTERVIEW
--------------------------------------------------------
PREP
Topic: Tuples, Immutability, and Data Integrity
----------------------------------------------------
--- PART 1: BASICS & INITIALIZATION ---
--------------------------------------------------
1. Create a tuple containing five different data types (int, float, string, list, boolean).
2. Write a script to check the type of a tuple with a single element. Show the difference
between (5) and (5,).
3. Access the last element of a tuple without knowing its length.
4. Access the second to last element of a tuple using negative indexing.
5. Given nested_tuple = ("Python", [10, 20, 30], (5, 15, 25)), print the number 20.
6. Check if the element 'Sreeraj' exists in a tuple using a membership operator.
7. Find the memory size of a list vs. a tuple with the same elements using the sys module.
8. Unpack a tuple of 3 elements into three variables: x, y, and z.
9. Demonstrate what happens if you try to unpack a tuple of 4 elements into 3 variables.
10. Use the 'extended iterable unpacking' (using *) to grab the first element and the rest into a
list.
--- PART 2: IMMUTABILITY LOGIC ---
-------------------------------------------------
11. Write code that attempts to change the first element of a tuple and handle the resulting
TypeError gracefully.
12. Given a tuple: t = (1, 2, [3, 4]). Change the value 3 to 30. Explain why this works despite
tuples being immutable.
13. Create two tuples, concatenate them, and assign them to a new variable.
14. Use the repetition operator (*) to create a tuple of ten zeros.
15. Swap two variables a and b using tuple unpacking logic in a single line.
16. Write a program to "add" an item to a tuple by converting it to a list first.
17. Write a program to "remove" an item from a tuple.
18. Delete an entire tuple variable from memory and verify its absence using a try-except
block.
19. Sort a tuple of integers and return the result as a new tuple.
20. Reverse a tuple using the slicing method [::-1].

--- PART 3: METHODS & AGGREGATION ---
---------------------------------------
21. Find the index of the first occurrence of the number 10 in a tuple.
22. Count how many times the string "Python" appears in a tuple of job roles.
23. Find the maximum and minimum values in a tuple of stock prices.
24. Calculate the sum of all numeric elements in a tuple.
25. Given a tuple of tuples: ((1, 2), (3, 4), (5, 6)), calculate the sum of the second element of
each internal tuple.
26. Use the index() method to find the position of 'Apple' starting from index 3 in a large fruit
tuple.
27. Write a function that takes a tuple and returns a new tuple containing only the even
numbers.
28. Convert a list of tuples into a single flat list.
29. Create a tuple from a user-input string where each character is an element.
30. Check if all elements in a tuple are truthy using the all() function.

--- PART 4: SLICING & LOOPING ---
-------------------------------------
31. Extract a sub-tuple containing the elements from index 2 to 5 (inclusive).
32. Use slicing to get every second element of a tuple.
33. Write a 'for' loop to print each element of a tuple with its corresponding index number.
34. Use a 'while' loop to iterate through a tuple backwards.
35. Create a tuple of 10 numbers and slice it to get the last 3 elements.
36. Slice a tuple to remove the first and last elements.
37. Use a for loop to concatenate all strings in a tuple into a single sentence.
38. Compare two tuples (1, 2, 3) and (1, 2, 4). Explain the logic of how Python compares
them.
39. Write a program to find duplicate elements in a tuple.
40. Zip two tuples together to create a list of coordinate pairs.

PART 5 - Logical Tuple Problems
-----------------------------------
31. Create a tuple of numbers and find the second largest number.
32. Write a program to remove duplicate elements from a tuple.
33. Write a program to find the frequency of each element in a tuple.
34. Write a program to convert a list of tuples into a dictionary.
Example:
[(1,'A'), (2,'B'), (3,'C')]
35. Write a program to sort a tuple of numbers.
36. Write a program to sort a tuple of tuples based on the second element.
Example:
((1,5),(3,2),(4,8))
37. Write a program to find common elements between two tuples.
38. Write a program to convert a tuple into a string.
39. Write a program to count vowels present in a tuple of characters.
40. Write a program to find the product of all numbers in a tuple.

--- PART 6: INDUSTRIAL TRENDS & ADVANCED (MISSING TOPICS) ---
-------------------------------------------------------------
41. [NamedTuple] Use 'collections.namedtuple' to create a 'Student' object with fields 'name',
'roll_no', and 'course'.
42. [Dictionary Keys] Demonstrate using a tuple as a key in a dictionary (e.g.,
latitude/longitude). Explain why a list cannot be a key.
43. [Data Integrity] Write a function that returns multiple values (name, age, salary) as a
tuple.
44. [Efficiency] Iterate through a tuple of 1,000,000 integers and measure the time taken.
Compare it with a list.
45. [Nested Logic] Given a list of tuples representing products: [("Laptop", 1000), ("Mouse",
25)]. Sort the list based on the price (the second element).
46. [String Formatting] Use a tuple to provide values for an old-style string formatting:
"Hello %s, your ID is %d".
47. [Function Arguments] Write a function that accepts *args and prints the type of 'args'.
48. [Hashing] Use the hash() function on a tuple. Then try it on a list. Note the difference.
49. [Conversion] Convert a tuple of single-character strings into a single string.
50. [Filtering] Use the filter() function with a lambda to remove all None values from a tuple.

'''

# for i  in range(1,51):
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


# 18 :


# 19 :


# 20 :


# 21 :


# 22 :


# 23 :
# Find the maximum and minimum values in a tuple of stock prices.

'''
a=(5,1,4,3,5,2,6,8,7,9,10,1,2,-1)
minimum=0
maximum=0
for i in a:
    if maximum>a[i]:
        maximum=a[i]
    if minimum<a[i]:
        minimum=a[i]
print(f"minmun valu = {minimum}")
print(f"maximum value = {maximum}")

 '''       

# 24 :
# Calculate the sum of all numeric elements in a tuple.

'''

a=(10,20,30,40,50)
sum=0
for i in a:
    sum=sum+i
print(sum)

'''
# 25 :
# Given a tuple of tuples: ((1, 2), (3, 4), (5, 6)), calculate the sum of the second element of
# each internal tuple.

'''

a=((1, 2), (3, 4), (5, 6))
s=0
for i in range(len(a)):
    s=s+a[i][1]
print(s)

'''

# 26 :
# Use the index() method to find the position of 'Apple' starting from index 3 in a large fruit tuple.
'''

a=("banana","kivi","apple","orage")
print(a.index("apple"))

'''

# 27 :


# 28 :


# 29 :


# 30 :


# 31 :
# Create a tuple of numbers and find the second largest number.

'''

s=(1,2,5,6,8,9,9)
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

# 32 :
# Write a program to remove duplicate elements from a tuple.
'''

a=(1,1,1,2,2,2,3,3,3,'a','a','b','b')
b=()
for i in a:
    if not i in b:
        b+=(i,)
print(b)

'''

# 33 :
# Write a program to find the frequency of each element in a tuple.

'''
a=(1,2,3,3,3,4,2,1,8)
for i in a:
    print(f"{i} frequency = {a.count(i)}")

'''

'''
a=("najad","riju","aju",100)
b=0
for i in a:
    if isinstance(i,int):
        j=i
        while j>0:
            b+=1
            j=int(j/10)
        print(f"{i} frequency = {b}")
    elif i.isalpha:
        print(f"{i} frequency = {len(i)}")
'''

# 34 :
# Write a program to convert a list of tuples into a dictionary.
# Example:
# [(1,'A'), (2,'B'), (3,'C')]

'''
a=[]
for i in range(1,27):
    a.append((i,chr(64+i)))
print(a)
print()
a.clear()
for i in range(1,27):
    a.append((i,chr(96+i)))
print(a)

'''

# 35 :
# Write a program to sort a tuple of numbers.

'''
c=(1,2,5,7,-1,2,-2)
b=0
a=list(c)
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]<a[j]:
            b=a[i]
            a[i]=a[j]
            a[j]=b
print(tuple(a))

'''

# 36 :
# Write a program to sort a tuple of tuples based on the second element.
# Example:
# ((1,5),(3,2),(4,8))

'''
a=((1,5),(3,2),(4,8),(8,1))
b=list(a)
c=0
for i in range(len(b)):
    for j in range(len(b)):
        if b[i][-1]<b[j][-1]:
            c=b[i]
            b[i]=b[j]
            b[j]=c
print(a)
print(b)

'''

# 37 :
# Write a program to find common elements between two tuples.

'''

a=(1,2,3,4,5,6,7,8,9)
b=(5,6,7,8,9,10,11,12)
c=[]
for i in a:
    if i in b:
        c.append(i)
print(tuple(c))

'''

# 38 :
# Write a program to convert a tuple into a string.

'''
a=input("enter a string : ")
print(tuple(a.split()))

'''

# 39 :
# Write a program to count vowels present in a tuple of characters.

# '''


# '''

# 40 :
# Write a program to find the product of all numbers in a tuple.

# '''


# '''

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
