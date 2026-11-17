


'''A Python list is a built-in data structure that allows
you to store an ordered collection
of items. Lists can hold items of different data types,
 including numbers, strings, and even other lists.
They are mutable, meaning you can change their contents
(add, remove, or modify elements)
after the list is created.'''

#Features of Python Lists:
# Ordered:The items in a list have a specific order, and that order is maintained.
# Indexed: Each item in a list has an index starting from 0 for the first element.
# Mutable: You can change a list by adding, removing, or modifying elements.
# Heterogeneous: A list can contain elements of different data types.
#
#====================================================================================
# Example:
#
thislist = ["apple", "banana", "cherry"]
print(thislist)
#
# Explanation: A list named `thislist` is created with three string elements:
# `"apple"`, `"banana"`, and `"cherry"`. The `print()` function outputs the list.
#
# Output:['apple', 'banana', 'cherry']
#
# ====================================================================================
# 2. List Characteristics
#
# Ordered:
# Lists maintain the order of elements as they are added.
#
# Changeable:
# - You can modify, add, or remove elements after the list is created.
#
# Allow Duplicates:
# - Lists can contain duplicate elements.
#
# Example:
#
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#
# Explanation: The list contains duplicate values. The `print()` function outputs
# the list with duplicates.
#
# Output:['apple', 'banana', 'cherry', 'apple', 'cherry']
#
#=======================================================================================
# 3. List Length
#
# Function:
# Use `len()` to determine the number of elements in a list.
#
# Example:
#
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#
# Explanation: `len(thislist)` returns the number of elements in `thislist`, which is `3`.
#
# Output:3

# ============================================================================================
# 4. List Data Types
#
# Versatility:
# List elements can be of any data type, including strings, integers, and booleans.
#
# Example:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
#
# Explanation: Three lists are created: `list1` contains strings, `list2` contains integers,
# and `list3` contains boolean values.
#
# Output:
# ['apple', 'banana', 'cherry']
# [1, 5, 7, 9, 3]
# [True, False, False]
#
# ====================================================================================================
# 5. Mixed Data Types in a List
#
# Example:

list1 = ["abc", 34, True, 40, "male"]
print(list1)

# Explanation: This list contains a mix of strings, integers, and a boolean value.
# Output:['abc', 34, True, 40, 'male']

# ===================================================================================
# 6. List Type
#
# Function:
# You can check the data type of a list using the `type()` function.
#
# Example:

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#
# Explanation: `type(mylist)` returns `<class 'list'>`, indicating that `mylist` is a list.
#
# Output: <class 'list'>

#========================================================================================
# 7. The `list()` Constructor
#
# Creating Lists:
# Lists can also be created using the `list()` constructor.
#
# Example:

thislist = list(("apple", "banana", "cherry"))
print(thislist)

# Explanation: The `list()` constructor creates a list from a tuple.
#
# Output: ['apple', 'banana', 'cherry']

# ========================================================================
# 8. Accessing List Items
#
# Indexing:
# Lists are indexed, starting from 0. You can access elements using their index.
#
# Example:
#
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#
# Explanation: `thislist[1]` accesses the second element, `"banana"`.
#
# Output:banana
#
# Negative Indexing:
# - Negative indexing allows you to access elements from the end of the list.
#
# Example:
#
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#
# Explanation:`thislist[-1]` accesses the last element, `"cherry"`.
#
# Output: cherry
#
# Range of Negative Indexes:
# You can specify a range using negative indexes to access multiple elements.
#
# Example:
#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#
# Explanation: `thislist[-4:-1]` returns elements from the fourth last to the second last element.
#
# Output:['orange', 'kiwi', 'melon']
#
# =============================================================================
# 9. Checking if an Item Exists
#
# Example:
#
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
#
# Explanation: The `in` keyword checks if `"apple"` is in `thislist`.
#
# Output:Yes, 'apple' is in the fruits list
#
# ========================================================================
# 10. Changing List Items
#
# Changing a Single Item:
# You can change the value of an element by referencing its index.
#
# Example:
#
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#
# Explanation: The second element, `"banana"`, is replaced with `"blackcurrant"`.
#
# Output:['apple', 'blackcurrant', 'cherry']
#
#
# Changing a Range of Items:
# You can change multiple elements at once by specifying a range of indexes.
#
# Example:
#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#
# Explanation: The elements at indexes 1 and 2 are replaced with `"blackcurrant"` and `"watermelon"`.
#
# Output:['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
#
#
# Inserting More Items:
# If you replace a single item with multiple items, the list will expand.
#
# Example:
#
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)
#
# Explanation: The second element is replaced with two new elements.
#
# Output:['apple', 'blackcurrant', 'watermelon', 'cherry']
#
#
# Inserting Fewer Items:
# If you replace multiple items with a single item, the list will shrink.
#
# Example:
#
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)
#
# Explanation: The second and third elements are replaced with a single element.
#
# Output: ['apple', 'watermelon']
#
# ====================================================================================
# 11. Inserting Items
#
# Insert Method:
# Use `insert()` to add an item at a specific index without
# replacing any existing items.
#
# Example:
#
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#
# Explanation: `"watermelon"` is inserted at index 2, shifting `"cherry"` to the right.
#
# Output:['apple', 'banana', 'watermelon', 'cherry']

#
# Inserting a List:
# You can insert a list within another list.
#
# Example:
#
thislist = ["apple", "banana", "cherry"]
newlist = ["jackfruit", "Mango"]
thislist.insert(1, newlist)
print(thislist)
#
# Explanation: The list `newlist` is inserted as a single element at index 1.
#
# Output:['apple', ['jackfruit', 'Mango'], 'banana', 'cherry']

#==============================================================================
# 12. Extending a List
#
# Extend Method:
# `extend()` adds elements from one list to another.
#
# Example:
#
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)
#
# Explanation: Elements from `tropical` are added to `thislist`.
#
# Output:['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
#
#
# Adding Any Iterable:
# You can extend a list with any iterable object.
#
# Example:
#
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
#
#
# print(thislist)
#
# Explanation: Elements from `thistuple` are added to `thislist`.
#
# Output:['apple', 'banana', 'cherry', 'kiwi', 'orange']
#
# ===================================================================
# 13. Removing List Items
#
# Remove Method:
# `remove()` deletes a specified item from the list.
#
# Example:
#
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)
#
# Explanation: `"banana"` is removed from `thislist`.
#
# Output:['apple', 'cherry']

#
# Pop Method:
# `pop()` removes an item at a specified index or the last item if no index is specified.
#
# Example:
#
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)
#
# Explanation: The element at index 1, `"banana"`, is removed.
#
# Output:['apple', 'cherry']

#
# Delete Keyword:
# `del` can remove an item at a specific index or delete the entire list.
#
# Example:
#
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
#
# Explanation: The first element, `"apple"`, is deleted.
#
# Output: ['banana', 'cherry']
#
# Clear Method:
# `clear()` empties the list without deleting the list itself.
#
# Example:
#
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)
#
# Explanation:All elements are removed from `thislist`.
#
# Output:[]

# =======================================================================
# 14. Looping Through a List
#
# For Loop:
# You can loop through a list using a `for` loop to access each element.
#
# Example:
#
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)
#
# Explanation: The loop iterates over `thislist` and prints each element.
#
# Output:
# apple
# banana
# cherry
#====================================================
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while thislist[i:] :
#     print(thislist[i])
#     i = i + 1
#======================================================
#
# Looping with Index:
# You can also loop through a list by index using `range()` and `len()`.
#
# Example:
#
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])
#
# Explanation: The loop iterates over the indexes and prints the elements at those indexes.
#
# Output:

# apple
# banana
# cherry

#
# While Loop:
# A `while` loop can also be used to iterate over a list.
#
# Example:
#
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1
#
# Explanation: The loop prints each element until the index `i` equals the length of the list.
#
# Output:

# apple
# banana
# cherry

#
# List Comprehension:
# List comprehension is a concise way to create lists.
#
# Example:
#
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# Explanation: A list comprehension iterates through `thislist`, printing each element.
#
# Output:
#
# apple
# banana
# cherry
#
# ============================================================================================
# 15. List Comprehension
#
# Definition:
# A way to create new lists by applying an expression to each item in an existing list.
#
# Example:
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# Explanation: The list comprehension checks for the presence of `"a"` in each element
# of `fruits` and creates a new list with those elements.
#
# Output:['apple', 'banana', 'mango']
#
# Syntax:

# newlist = [expression for item in iterable if condition == True]
#
# Explanation: This is the general syntax of a list comprehension,
# where `expression` is applied to each `item` in an `iterable`, and the item is
# included in the `newlist` if the `condition` is true.
#
# Example:
#
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)

# Explanation: The list comprehension replaces `"banana"` with `"orange"` in the new list.
#
# Output:['apple', 'orange', 'cherry', 'kiwi', 'mango']
#===============================================================================================

# 16.Using an Iterable Other Than a List
#
# newlist = [x for x in range(10)]
#
# print(newlist)

#
# Explanation: range(10)**: Generates numbers from 0 to 9.newlist: Includes all those numbers.
#
# Output:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ==============================================================================================
# 17. List Comprehension with a Condition on Numbers
#
# newlist = [x for x in range(10) if x < 5]
#
# print(newlist)
# Explanation:if x < 5: Only numbers less than 5 are included in `newlist`.
#
#Output:[0, 1, 2, 3, 4]
#
# ===============================================================================
# 18. Manipulating Items During Iteration
#
# Example: Uppercase Conversion
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
#
# print(newlist)
#
#
# Explanation:
# x.upper(): Converts each item in `fruits` to uppercase.
#
# Output:['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

#
# Example : Replacing All Values with 'hello'

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = ['hello' for x in fruits]
#
# print(newlist)

#
# Explanation:
# 'hello': Every item in the new list is replaced with the string 'hello'.
#
#  Output:['hello', 'hello', 'hello', 'hello', 'hello']
#============================================================================
'''Conclusion:
List comprehension is a powerful tool in Python, allowing you to create and
transform lists with minimal code. You can include conditions, manipulate data, 
and even handle multiple iterables all within a single, readable line of code.'''