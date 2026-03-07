'''Python Strings – Lab Practical Questions (Beginner to Advanced)
-------------------------------------------------------------------------------
Designed for practical labs and interview preparation
--------------------------------------------------------------------
A.Beginner Level
-------------------------------------
• 1. Create a string and print it.
• 2. Print each character of a string using indexing.
• 3. Print the first and last character of a string.
• 4. Demonstrate positive and negative indexing on a string.
• 5. Extract the first five characters from a string using slicing.
• 6. Reverse a string using slicing.
• 7. Count the length of a string without using len().
• 8. Convert a string to uppercase and lowercase.
• 9. Capitalize the first letter of a string.
• 10. Swap the case of each character in a string.
• 11. Check whether a string starts with a specific substring.
• 12. Check whether a string ends with a specific substring.
• 13. Count the number of occurrences of a character in a string.
• 14. Replace a word in a string with another word.
• 15. Remove leading and trailing spaces from a string.

B.Intermediate Level
-------------------------
• 1. Check whether a string contains only alphabets.
• 2. Check whether a string contains only digits.
• 3. Check whether a string is alphanumeric.
• 4. Split a sentence into words using split().
• 5. Join a list of words into a single string.
• 6. Find the first occurrence of a substring in a string.
• 7. Find the last occurrence of a substring in a string.
• 8. Remove a prefix from a string.
• 9. Remove a suffix from a string.
• 10. Center align a string within a given width.
• 11. Left justify and right justify a string.
• 12. Pad a number string with zeros using zfill().
• 13. Use format() method in string formatting.
• 14. Create a formatted string using f-strings.
• 15. Use partition() to split a string into three parts.

C.Logical Problem Solving
--------------------------------------
• 1. Check whether a string is a palindrome.
• 2. Count the number of vowels and consonants in a string.
• 3. Remove duplicate characters from a string.
• 4. Find the most frequent character in a string.
• 5. Check if two strings are anagrams.
• 6. Reverse each word in a sentence without reversing the sentence order.
• 7. Find the longest word in a sentence.
• 8. Compress a string (example: aaabb ® a3b2).
• 9. Remove all spaces from a string.
• 10. Convert the first letter of every word to uppercase without using title().
• 11. Extract digits from a string and store them separately.
• 12. Count the number of words in a sentence.
• 13. Replace multiple spaces with a single space.
• 14. Check whether a string contains special characters.
• 15. Find the ASCII value of each character.

D.Advanced / Real-world Tasks
----------------------------------------
• 1. Encode and decode a string.
• 2. Create a translation table using maketrans() and translate characters.
• 3. Simulate a simple password validator using string methods.
• 4. Parse key-value pairs from a string like 'name=John;age=25'.
• 5. Implement a simple email validation using string methods.
• 6. Extract hashtags from a text.
• 7. Mask sensitive data like phone numbers.
• 8. Implement basic text formatting similar to markdown.
• 9. Check if a sentence is a pangram.
• 10. Sort characters in a string alphabetically.

E.Interview-Oriented Questions
-------------------------------------------------
• 1. Explain the difference between find() and index() with code.
• 2. Explain the difference between split() and rsplit() with examples.
• 3. Explain the difference between strip(), lstrip(), and rstrip().
• 4. Explain the difference between isdigit(), isnumeric(), and isdecimal().
• 5. Check whether two strings are rotations of each other.'''


# for i  in range(1,16):
#     print(f"# A : {i}")
# for i  in range(1,16):
#     print(f"# B : {i}")
# for i  in range(1,16):
#     print(f"# C : {i}")
# for i  in range(1,11):
#     print(f"# D : {i}")
# for i  in range(1,6):
#     print(f"# E : {i}")


# A : 1
# A : 2
# A : 3
# A : 4
# A : 5
# A : 6
# A : 7
# A : 8
# A : 9
# A : 10
# A : 11
# A : 12
# A : 13
# A : 14
# A : 15


# B : 1
# B : 2
# B : 3
# B : 4
# B : 5
# B : 6
# B : 7
# B : 8
# B : 9
# B : 10
# B : 11
# B : 12
# B : 13
# B : 14
# B : 15



# C : 1
# palindrome

'''
s=input("enter a string :")
pali=""
for i in s:
    pali=i+pali
print(pali)
if s==pali:
    print("the string is palindrome")
else:
    print("the string is not palindrome")
'''


# C : 2
# number of vowels and consonants

'''
s=input("enter a string :")
vowels=0
sp=0
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" or i==" ":
        if i==" ":
            sp +=1
        else:
            vowels +=1
num=len(s)
print(f"total steing langth {num} nubers.\nthere are {vowels} number vowels in thes string.")
print(f"there are {num-(vowels+sp)} number consonants in thes string.\nthere are {sp} number spices in thes string. ")
'''

# C : 3
'''
s=input("enter a string :")
a=""
for i in s:
    if i not in a:
        a=a+i
print(a)
'''

# C : 4
# C : 5
# C : 6
# C : 7
# C : 8
# C : 9
# C : 10
# C : 11
# C : 12
# C : 13
# C : 14
# C : 15



# D : 1
# D : 2
# D : 3
# D : 4
# D : 5
# D : 6
# D : 7
# D : 8
# D : 9
# D : 10



# E : 1 ghjogjhojhogj
# E : 2
# E : 3
# E : 4
# E : 5



 
























