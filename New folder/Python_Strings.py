

# In Python, a string is a sequence of characters enclosed in quotes.
# Strings are used to store and manipulate text.
#
#  Creating Strings
#
# 1. Using Single Quotes
#
#    single_quote_string = 'Hello, World!'
#
#
# 2. Using Double Quotes
#
#    double_quote_string = "Hello, World!"
#
#
# 3. **Using Triple Quotes** (for multi-line strings):
#
#    triple_quote_string = """Hello,
#    World!"""
#
#
# ### String Operations
#
# 1. Concatenation:
#
   str1 = 'Hello'
   str2 = 'World'
   combined = str1 + ' ' + str2  # 'Hello World'
#
#
# 2. Repetition:
#
   repeated = 'Hello ' * 3  # 'HelloHelloHello'

# 3. Indexing:
#
   text = 'Python'
   first_char = text[0]  # 'P'
#
# 4. Slicing:

   text = 'Python'
   slice = text[1:4]  # 'yth'
#
# 5. Length:
#
#    length = len(text)  # 6
#
#
# ### String Methods
#
# 1. `lower()` - Converts to lowercase:

   text = 'Hello'
   print(text.lower())  # 'hello'
#
# 2. `upper()` - Converts to uppercase:
#
   text = 'Hello'
   print(text.upper())  # 'HELLO'
#
#
# 3. `strip()` - Removes whitespace from both ends:
#
   text = '  Hello  '
   print(text.strip())  # 'Hello'
#
# 4. `replace()` - Replaces a substring with another:
#
   text = 'Hello World'
   print(text.replace('World', 'Python'))  # 'Hello Python'
#
#
# 5. `split()` - Splits a string into a list:
#
   text = 'Hello World'
   print(text.split())  # ['Hello', 'World']
#
#
# 6. `join()` - Joins elements of a list into a string:
#
#    words = ['Hello', 'World']
#    sentence = ' '.join(words)  # 'Hello World'
#
#
# Strings in Python are immutable, which means that once a string is created, it cannot be changed.
# Instead, any operation that modifies a string will create a new string.


# #Syntax:
# str="Hi python"
# print(str)
# print(type(str))
#
# str = "HELLO"
# print(str[0]) # returns H
# print(str[1]) # returns E
# print(str[2]) # returns L
# print(str[3]) # returns L
# print(str[4]) # returns O

# Given String
# str = "INTERNATIONAL"
# # Start Oth index to end
# print(str[0:])
# # Starts 1th index to 4th index
# print(str[1:5])
# # Starts 2nd index to 3rd index
# print(str[2:4])
# # Starts 0th to 2nd index
# print(str[:3])
# #Starts 4th to 6th index
# print(str[4:7])

# Given String
str = "INTERNATIONAL"
print(str[-3:]) # 
print(str[-3]) # 
print(str[-2:]) #
print(str[-4:-1]) #ONA
print(str[-7:-2]) #ATION
# Reversing the given string
print(str[::-1]) #reverse
print(str[-12]) #N

# Example 1
# isalnum
str1 = "Welcome2023"
print(str1.isalnum())  # True

# Example 2
str2 = "Hello World"
print(str2.isalnum())  # False, because of the space

# Example 3
str3 = "123456"
print(str3.isalnum())  # True

# Example 4
str4 = "Hello@2023"
print(str4.isalnum())  # False, because of the '@' symbol
#======================================================================

# Example 1
str1 = "Python"
print(str1.isalpha())  # True

# Example 2
str2 = "Python3"
print(str2.isalpha())  # False, because of the digit '3'

# Example 3
str3 = "Hello World"
print(str3.isalpha())  # False, because of the space

# Example 4
str4 = "Python!"
print(str4.isalpha())  # False, because of the '!' symbol

#=========================================================================

# Example 1
str1 = "12345"
print(str1.isdigit())  # True

# Example 2
str2 = "12345a"
print(str2.isdigit())  # False, because of the letter 'a'

# Example 3
str3 = "123 45"
print(str3.isdigit())  # False, because of the space

# Example 4
str4 = "12.345"
print(str4.isdigit())  # False, because of the dot '.'

#=============================================================================

# Example 1
str1 = "python"
print(str1.islower())  # True

# Example 2
str2 = "Python"
print(str2.islower())  # False, because of the uppercase 'P'

# Example 3
str3 = "python3"
print(str3.islower())  # True, digits are ignored

# Example 4
str4 = "python!"
print(str4.islower())  # True, special characters are ignored

#=========================================================================

# Example 1
str1 = "WELCOME"
print(str1.isupper())  # True

# Example 2
str2 = "Welcome"
print(str2.isupper())  # False, because of the lowercase 'e'

# Example 3
str3 = "HELLO123"
print(str3.isupper())  # True, digits are ignored

# Example 4
str4 = "HELLO!"
print(str4.isupper())  # True, special characters are ignored

#==================================================================================

# Example 1
str1 = "   "
print(str1.isspace())  # True

# Example 2
str2 = "Hello World"
print(str2.isspace())  # False, because it contains non-whitespace characters

# Example 3
str3 = "\t\n"
print(str3.isspace())  # True, tab and newline are considered whitespace

# Example 4
str4 = " "
print(str4.isspace())  # True, single space

#================================================================================

# Example 1
str1 = "Welcome To Python"
print(str1.istitle())  # True

# Example 2
str2 = "welcome to Python"
print(str2.istitle())  # False, because 'welcome' is not capitalized

# Example 3
str3 = "Welcome To python"
print(str3.istitle())  # False, because 'python' is not capitalized

# Example 4
str4 = "Welcome To Python3"
print(str4.istitle())  # True, digits are ignored

#==============================================================================

# Example 1
str1 = "Python"
print(str1.lower())  # "python"

# Example 2
str2 = "WELCOME"
print(str2.lower())  # "welcome"

# Example 3
str3 = "Hello World"
print(str3.lower())  # "hello world"

# Example 4
str4 = "Python3!"
print(str4.lower())  # "python3!"

#=============================================

# Example 1
str1 = "   Python"
print(str1.lstrip())  # "Python"

# Example 2
str2 = ">>>Python"
print(str2.lstrip('>'))  # "Python"

# Example 3
str3 = "   Hello World   "
print(str3.lstrip())  # "Hello World   "

# Example 4
str4 = "\t\nPython"
print(str4.lstrip())  # "Python"

#===================================================

# Example 1
str1 = "Java is a programming language"
print(str1.replace("Java", "Python"))  # "Python is a programming language"

# Example 2
str2 = "Hello World"
print(str2.replace("World", "Python"))  # "Hello Python"

# Example 3
str3 = "12345"
print(str3.replace("3", "8"))  # "12845"

# Example 4
str4 = "banana"
print(str4.replace("a", "o"))  # "bonono"

str5 = "banana"
print(str4.replace("a", "o",2))  #"bonona
#
# #===================================================================================

# Example 1
str1 = "Python   "
print(str1.rstrip())  # "Python"

# Example 2
str2 = "Python>>>"
print(str2.rstrip('>'))  # "Python"

# Example 3
str3 = "   Hello World   "
print(str3.rstrip())  # "   Hello World"

# Example 4
str4 = "Python\t\n"
print(str4.rstrip())  # "Python"

#==================================================

# Example 1
str1 = "Java is a programming language"
print(str1.split(" "))  # ['Java', 'is', 'a', 'programming', 'language']

# Example 2
str2 = "apple,banana,cherry"
print(str2.split(","))  # ['apple', 'banana', 'cherry']

# Example 3
str3 = "Hello-World-Python"
print(str3.split("-"))  # ['Hello', 'World', 'Python']

# Example 4
str4 = "Python"
print(str4.split())  # ['Python'], default delimiter is any whitespace

#=======================================================================

# Example 1
str1 = "Hello Python"
print(str1.startswith("Hello"))  # True

# Example 2
str2 = "Python Programming"
print(str2.startswith("Java"))  # False

# Example 3
str3 = "Hello Python"
print(str3.startswith("Python", 6))  # True

# Example 4
str4 = "Python"
print(str4.startswith("Py"))  # True
# ===========================================================
# Example 1
str1 = "Hello Python"
print(str1.endsswith("Python"))  # True

# Example 2
str2 = "Python Programming"
print(str2.endswith("Java"))  # False

# Example 3
str3 = "Hello Python"
print(str3.endswith("Python", 6))  # True

# Example 4
str4 = "Python"
print(str4.endswith("on"))  # True

#===============================================================

# Example 1
str1 = "Hello Python"
print(str1.swapcase())  # "hELLO pYTHON"

# Example 2
str2 = "PYTHON"
print(str2.swapcase())  # "python"

# Example 3
str3 = "python3!"
print(str3.swapcase())  # "PYTHON3!"

# Example 4
str4 = "Hello World"
print(str4.swapcase())  # "hELLO wORLD"

#==============================================

# Example 1
str1 = "hello python"
print(str1.title())  # "Hello Python"

# Example 2
str2 = "HELLO WORLD"
print(str2.title())  # "Hello World"

# Example 3
str3 = "python programming"
print(str3.title())  # "Python Programming"

# Example 4
str4 = "hello world! python3"
print(str4.title())  # "Hello World! Python3"

#===============================================================

# Example 1
str1 = "Hello python"
print(str1.upper())  # "HELLO PYTHON"

# Example 2
str2 = "welcome"
print(str2.upper())  # "WELCOME"

# Example 3
str3 = "Python3!"
print(str3.upper())  # "PYTHON3!"

# Example 4
str4 = "hello world"
print(str4.upper())  # "HELLO WORLD"

#=============================================================

