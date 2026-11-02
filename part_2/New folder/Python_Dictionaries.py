#Python Dictionaries

#  Definition:
# A dictionary in Python is a collection of key-value pairs.
# Each key in the dictionary is unique, and it maps to a specific value.
# Dictionaries are created using curly brackets {} with key-value pairs
# separated by a colon :

# Properties of Dictionaries:

# Ordered: Dictionaries maintain the order of insertion.
# Changeable: You can add, remove, or change items in a dictionary.
# No Duplicates: A key must be unique; if a key is repeated,
# the last value will overwrite the previous one.
#=================================================================
# 1. Creating and Printing a Dictionary
#
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(thisdict)
#
# Explanation:
# thisdict is a dictionary with three key-value pairs.
#  `"brand"` is the key, and `"Ford"` is the value.
#  `"model"` is the key, and `"Mustang"` is the value.
#  `"year"` is the key, and `1964` is the value.
# `print(thisdict)` outputs the entire dictionary, showing all key-value pairs.
#
# Output:
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#==============================================================
#  2. Accessing Dictionary Items
#You can access the value associated with a specific key using square brackets []
# or the get() method.

# x = thisdict["model"]
# print(x)

# Explanation:
# - You access a dictionary value by using its key inside square brackets.
# Here, `thisdict["model"]` retrieves the value `"Mustang"`.
# - The value is stored in the variable `x`, and `print(x)` outputs it.
#
# Output:Mustang

# print(thisdict["brand"])  # Output: Ford
# print(thisdict.get("model"))  # Output: Mustang

# Dictionary Methods:

# keys(): Returns a view object of all keys.

# print(thisdict.keys())  # Output: dict_keys(['brand', 'model', 'year', 'color'])

# values(): Returns a view object of all values.

# print(thisdict.values())  # Output: dict_values(['Ford', 'Mustang', 2020, 'red'])

# items(): Returns a view object of all key-value pairs.

# print(thisdict.items())  # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang')

#========================================================================
#  3. Checking for Key Existence
#
# if "model" in thisdict:
#     print("Yes, 'model' is one of the keys in the thisdict dictionary")
# else:
#   print("No existence")

#
# Explanation:
# - The `in` keyword checks if a key exists in the dictionary.
# - If `"model"` is a key in `thisdict`, the message is printed.
#
# Output:Yes, 'model' is one of the keys in the thisdict dictionary
#=======================================================================
# 4.Changing Dictionary Values
#
# thisdict["year"] = 2018
# print(thisdict)
#
# Explanation:
# - You can change the value of a specific key by reassigning it.
# - `thisdict["year"] = 2018` changes the `"year"` value from `1964` to `2018`.
# - `print(thisdict)` shows the updated dictionary.
#
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
#===============================================================================
# 5. Adding Items to a Dictionary
#
# thisdict["color"] = "red"
# print(thisdict)
#
# Explanation:
# - To add a new key-value pair, you use a new key and assign it a value.
# - `thisdict["color"] = "red"` adds the key `"color"` with the value `"red"` to the dictionary.
# - `print(thisdict)` displays the updated dictionary.
#
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'red'}
#=============================================================================
#  6.Removing Items from a Dictionary
#
# thisdict.pop("model")
# print(thisdict)
#
# Explanation:
# - `pop("model")` removes the key `"model"` and its associated value from the dictionary.
# - `print(thisdict)` shows the dictionary after removal.
#
# Output:{'brand': 'Ford', 'year': 2018, 'color': 'red'}

# pop(): Removes the item with the specified key.

# thisdict.pop("model")
# print(thisdict)  # Output: {'brand': 'Ford', 'year': 2020, 'color': 'red'}

# popitem(): Removes the last inserted item.
# del: Deletes the item or the entire dictionary.
# clear(): Empties the dictionary.
#=========================================================================================
#  7. Looping Through a Dictionary
#
# for x in thisdict:
#     print(x)
#
# Explanation:
# - This loop iterates through all the keys in `thisdict`.
# - Each key is printed one by one.
#
# Output:
# brand
# year
# color

# Loop through keys:

# for key in thisdict:
#     print(key)

# Loop through values:

# for value in thisdict.values():
#     print(value)

# Loop through key-value pairs:

# for key, value in thisdict.items():
#     print(key, value)
#==============================================================
#  8. Copying a Dictionary

# copy(): Creates a shallow copy of the dictionary.
# dict(): Another way to copy the dictionary.

# newdict1 = thisdict.copy()
# newdict2 = dict(thisdict)

# mydict = thisdict.copy()
# print(mydict)

# Explanation:
# - `copy()` creates a shallow copy of the dictionary `thisdict`.
# - `mydict` now contains the same key-value pairs as `thisdict`.
# - `print(mydict)` shows the copied dictionary.
#
# Output:{'brand': 'Ford', 'year': 2018, 'color': 'red'}
#=====================================================================
# 9.Nested Dictionaries
#
# myfamily = {
#     "child1": {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Tobias",
#         "year": 2007
#     },
#     "child3": {
#         "name": "Linus",
#         "year": 2011
#     }
# }
# print(myfamily)
#
# Explanation:
# - **myfamily** is a dictionary containing three dictionaries as values.
# - Each key (`"child1"`, `"child2"`, `"child3"`) has a dictionary as its value, which contains information about a child.
# - `print(myfamily)` outputs the nested structure.
#
# Output:
# {'child1': {'name': 'Emil', 'year': 2004},
# 'child2': {'name': 'Tobias', 'year': 2007},
# 'child3': {'name': 'Linus', 'year': 2011}}
#=======================================================================
#  10.Creating a Nested Dictionary by Combining Dictionaries
#
# child1 = {
#     "name": "Emil",
#     "year": 2004
# }
# child2 = {
#     "name": "Tobias",
#     "year": 2007
# }
# child3 = {
#     "name": "Linus",
#     "year": 2011
# }
#
# myfamily = {
#     "child1": child1,
#     "child2": child2,
#     "child3": child3
# }
# print(myfamily)
#
# Explanation:
# - Here, three separate dictionaries (`child1`, `child2`, `child3`) are created first.
# - Then, `myfamily` combines these dictionaries into a nested dictionary.
# - `print(myfamily)` outputs the combined nested dictionary structure.
#
# Output:
# {'child1': {'name': 'Emil', 'year': 2004},
# 'child2': {'name': 'Tobias', 'year': 2007},
# 'child3': {'name': 'Linus', 'year': 2011}}
