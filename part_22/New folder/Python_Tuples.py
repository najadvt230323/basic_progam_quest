
#  1. Introduction to Tuples
#
# Tuples are a built-in data type in Python that allows you to store multiple
# items in a single variable. Tuples are one of four collection data types in Python,
# along with Lists, Sets, and Dictionaries. The unique characteristics of tuples are that they are:
# Ordered: The items have a defined order that does not change.
# Unchangeable (Immutable): You cannot modify the tuple after it is created.
# Allow Duplicates: Tuples can contain multiple items with the same value.
#
# 2. Creating a Tuple
#
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
#
# thistuple = ("apple", "banana", "cherry") This line creates a tuple named `thistuple`
# containing three items: `"apple"`, `"banana"`, and `"cherry"`.
# print(thistuple): This line prints the tuple, and the output is `('apple', 'banana', 'cherry')`.
#
# 3. Tuple Items
#
# Ordered: The order of elements is preserved.
# Unchangeable: Once created, you can't change the elements.
# Allow Duplicates: Tuples can have repeated elements.
#
#  4. Tuples Allow Duplicate Values
#
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#
# thistuple = ("apple", "banana", "cherry", "apple", "cherry"): This tuple contains duplicate
# items `"apple"` and `"cherry"`.
# print(thistuple): The output will include all the items, showing that duplicates are allowed.
#
#  5. Tuple Length
#
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# print(len(thistuple)): The `len()` function returns the number of items in the tuple.
# In this case,
# the output is `3`.
#
#  6. Creating a Tuple with One Item
#
# thistuple = ("apple",)
# print(type(thistuple))
#
# thistuple = ("apple")
# print(type(thistuple))

# thistuple = ("apple",): When creating a tuple with one item, you must include a comma
# after the item to make it a tuple.
# print(type(thistuple)): The `type()` function shows that this is a tuple.
# thistuple = ("apple"): Without the comma, Python treats this as a string, not a tuple.
#
# 7. Tuple Items - Data Types
#
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
#
# print(tuple1)
# print(tuple2)
# print(tuple3)

# - Tuples can hold items of any data type (strings, integers, booleans).
#
#  8.The `tuple()` Constructor**
#
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

thistuple2 = tuple(["apple", "banana", "cherry"])
print(thistuple2)

("apple", "banana", "cherry")
#
# tuple(("apple", "banana", "cherry")): Creates a tuple from another tuple or list.
# thistuple2 = tuple(["apple", "banana", "cherry"]): Creates a tuple from a list.
#
# 9. **Accessing Tuple Items
#
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# thistuple[1]: Accesses the item at index `1`, which is `"banana"`.
#
# 10.Accessing the Last Item in a Tuple
#
# print(thistuple[-1])

#thistuple[-1]: Accesses the last item in the tuple, `"cherry"`.
#
# 11. Range of Indexes
#
#
# print(thistuple[2:5])
#
# thistuple[2:5]: This slice returns a new tuple from index `2` (included) to `5` (excluded).
#
#  12. Range of Negative Indexes**
#
#
# print(thistuple[-4:-1])
#
# thistuple[-4:-1]: Accesses the items from the fourth last to the second last.
#
# 13. Check if Item Exists
#
#
# if "apple" in thistuple:
#     print("Yes, 'apple' is in the fruits tuple")

#
# if "apple" in thistuple: Checks if `"apple"` is in the tuple.
# print("Yes, 'apple' is in the fruits tuple"): If found, prints a confirmation.
#
# 14. Update Tuples (Workarounds)
#
# Convert to List and Back:
#
    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)
    print(x)

#     Converts a tuple to a list, modifies it, and converts it back to a tuple.
#
# Add Items:
#
#     y.append("orange")
#
#     Appends `"orange"` to the list before converting back to a tuple.
#
# Add Tuple to Tuple:
#
#     y = ("orange",)
#     thistuple += y
#     print(thistuple)
#
#     Adds a new tuple to the existing one.
#
# 15. Removing Items (Workarounds)
#
# y.remove("apple")

# y.remove("apple"): Removes `"apple"` from the list before converting back to a tuple.
#
# 16. Delete Tuple
#
# del thistuple
#
# del thistuple: Deletes the entire tuple.
#
# 17. Unpacking Tuples
#
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Unpacking: Assigns the tuple items to variables `green`, `yellow`, and `red`.

# 18. Using Asterisk `*` for Variable-Length Unpacking
#
# (green, yellow, *red) = fruits

# (green, yellow, *red): Assigns the first two items to `green` and `yellow`, and the rest to `red` as a list.
#
#  19. Looping Through a Tuple
#
 thistuple= ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# for x in thistuple: Iterates over each item in the tuple.

#fruits = ("apple", "banana", "cherry")
# i=0
# while fruits[i:]:
#     print(fruits[i])
#     i=i+1
#
# 20. Loop Through Index Numbers
#
# for i in range(len(thistuple)):
#     print(thistuple[i])

#for i in range(len(thistuple)): Uses a loop to iterate over indexes.
#
#  21. Using a While Loop
#
# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i = i + 1
#
# while i < len(thistuple):Loops through the tuple using a `while` loop.
#
# 22. Joining Tuples
#
# tuple3 = tuple1 + tuple2
# print(tuple3)
#
# tuple1 + tuple2: Joins two tuples together.
#
#  23. **Multiplying Tuples
#
# mytuple = fruits * 2
# print(mytuple)
#
#fruits * 2: Duplicates the tuple contents.
#
#  24. Tuple Methods
#
# count():
#     x = thistuple.count(5)
#
#     Counts how many times `5` appears in the tuple.


thistuple = (1,2,3,4,5,5,5,6,7,8)
x = thistuple.count(5)
print(x)
#
# index():
#      x = thistuple.index(80)
#
#   Returns the index of the first occurrence of `80`.

# thistuple = (1,2,3,4,5,5,5,6,7,8,80,80)
# x = thistuple.index(80)
# print(x)