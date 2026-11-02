
# What is a Set?

# Definition: A set in Python is a collection data type that is unordered
#  and unindexed.
# Usage: Sets are used to store multiple unique items in a single variable.
# Unique Property: Sets do not allow duplicate values.
# Syntax: Sets are defined using curly brackets `{}`.
#
# Example: Create a Set

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Explanation: A set named `thisset` is created containing the elements
# `"apple"`, `"banana"`, and `"cherry"`. When printed, the set might
# display the items in any order because sets are unordered.

# Output
# {'apple', 'banana', 'cherry'}
#
# Set Items
# Unordered: The items in a set do not have a specific order and can appear
# in any sequence.
# Unchangeable: Once a set is created, you cannot modify the existing
# items, but you can add or remove items.
# No Duplicates: Sets automatically ignore duplicate items.
#
# Example: Duplicate Values



# Explanation: If `"apple"` is added twice, only one instance will be
# stored in the set because duplicates are not allowed.
# Output:
# {'apple', 'cherry', 'banana'}

#
# Getting the Length of a Set
#
# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))

# Explanation: The `len()` function returns the number of items in the set.
# Output:
# 3
#
#  Set Items - Data Types
# Different Data Types: Sets can store items of different data types
# including strings, integers, and booleans.
# Examples:
#   set1 = {"apple", "banana", "cherry"}
#   set2 = {1, 5, 7, 9, 3}
#   set3 = {True, False, False}
#   print(set1)
#   print(set2)
#   print(set3)

#   Output:
#     {'banana', 'apple', 'cherry'}
#     {1, 3, 5, 7, 9}
#     {False, True}
#
#  Mixed Data Types
#
set1 = {"abc", 34, True, 40, "male"}
print(set1)
#
# Explanation: Sets can contain a mix of different data types.
# Output:
# {True, 34, 40, 'abc', 'male'}
#
#  Checking the Type of a Set
#
# myset = {"apple", "banana", "cherry"}
# print(type(myset))

# Explanation: The `type()` function returns the data type of `myset`,
# which is `<class 'set'>`.
# Output:
#
# <class 'set'>
#
# The `set()` Constructor

thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)

# Explanation: The `set()` constructor can also be used to create a set.
# The double round brackets are required because `set()` takes an
# iterable as an argument.

# Output:
#
# {'apple', 'banana', 'cherry'}
#
#
#  Accessing Set Items
# No Indexing: Items in a set cannot be accessed using an index or key.
# Looping: You can loop through a set using a `for` loop.
#
# Example: Looping through a Set
#
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
#
# Explanation: This will print each item in the set, although
# the order is not guaranteed.

# Output:
# banana
# apple
# cherry
#
#  Checking for an Item

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Explanation: The `in` keyword checks if an item exists in the set.
# This will return `True` if `"banana"` is in `thisset`.
# Output:
#
# True
#
#
# Adding Items to a Set
# Unchangeable Items: While you cannot change an existing item in a set,
# you can add new items.
# Using `add()` Method: This method adds an item to the set.
#
#  Example: Adding an Item
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# Output:
# {'orange', 'cherry', 'banana', 'apple'}
#
#  Adding Items from Another Set
# Using `update()` Method: This method can add items from another set
# (or any iterable) into the current set.
#
#  Example: Adding Elements from Another Set
#
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# Output:
# {'pineapple', 'cherry', 'banana', 'mango', 'papaya', 'apple'}

#
# Removing Items from a Set
# Using `remove()` Method: This method removes a specified item from the set.
# If the item does not exist, `remove()` raises an error.
# Using `discard()` Method: Similar to `remove()`,
# but does not raise an error if the item is not found.
# Using `pop()` Method: Removes and returns a random item from the set.
# Since sets are unordered, you won’t know which item will be removed.
#
# Example: Removing Items
#
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

# Output:
#
# {'cherry', 'apple'}
#
# Clearing or Deleting a Set
# Using `clear()` Method: This method removes all items from the set.
# Using `del` Keyword: This completely deletes the set.
#
# Example: Clearing a Set
#
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

# Output:
#
# set()
#
# Looping through a Set
#
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#     print(x)
#
# Explanation: Loops through each item in the set and prints it.
#
# Copying a Set
# Using `copy()` Method: This creates a copy of the set.
#
# Example: Copying a Set
# fruits = {"apple", "banana", "cherry"}
# x = fruits.copy()
# print(x)
#
#
# Joining Two Sets
# Using `union()` Method: Returns a new set containing all items from both sets.
# Using `update()` Method: Adds items from one set to another.
#
# Example: Joining Sets with `update()`
#
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)
# Output:
# {'c', 1, 2, 3, 'a', 'b'}
#
# Set Operations
# Union (`|`): Combines items from both sets without duplicates.
# Intersection (`&`): Returns items that are common in both sets.
# Difference (`-`): Returns items in one set but not in the other.
# Symmetric Difference (`^`): Returns items that are in either set but not in both.
#
#  Example: Union
# Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday", "Sunday"}
# Days2 = {"Friday", "Saturday", "Sunday"}
# print(Days1 | Days2)
#
# Output:
#
# {'Wednesday', 'Tuesday', 'Thursday', 'Saturday', 'Friday', 'Monday', 'Sunday'}

#
#  Example: Intersection
#
# Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
# Days2 = {"Monday", "Tuesday", "Sunday", "Friday"}
# print(Days1 & Days2)
#
# Output:
# {'Tuesday', 'Monday'}

# Example: Difference
# Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
# Days2 = {"Monday", "Tuesday", "Sunday"}
# print(Days1 - Days2)
# print(Days2-Days1)---Sunday

# Output:
# {'Wednesday', 'Thursday'}

#
# Example: Symmetric Difference
# a = {1, 2, 3, 4, 5, 6}
# b = {1, 2, 9, 8, 10}
# print(a ^ b)
#
# Output:
# {3, 4, 5, 6, 8, 9, 10}
