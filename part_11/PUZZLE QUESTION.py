# Python Face-to-Face Interview Puzzle Questions
# --------------------------------------------------------------------

# List, String, Function & Mixed Coding Challenges
# LIST – Interview Puzzle Questions
# --------------------------------------------------------------------------

# 1. Split and Sort
# list1 = [5, 4, 3, 7, 2, 9]
# Create two lists: first list should contain the sorted first half and second list should contain the sorted second
# half.
# Expected: [3, 4, 5] and [2, 7 ,9]
list1 = [5, 4, 3, 7, 2, 9]
a=[]
b=[]


# for i in range(int(len(list1)/2)-1,-1,-1) :
#     a.append(list1[i])
#     b.append(list1[i+int(len(list1)/2)])

print(a)
print(b)


# 2. Alternate Elements
# list1 = [10, 20, 30, 40, 50, 60]
# Create two lists containing elements at even and odd indexes respectively.
# Expected: [10, 30, 50] and [20, 40, 60].
# Constraint: Don't use if.



# 3. Move Even Numbers First
# list1 = [5, 8, 3, 2, 9, 4, 6, 1]
# Create a new list where even numbers come first in ascending order and odd numbers come after in
# ascending order.
# Expected: [2, 4, 6, 8, 1, 3, 5, 9]





# 4. Remove Duplicates Without set()
# list1 = [4, 2, 5, 2, 4, 7, 5, 8]
# Create a new list without duplicates while maintaining the original order.
# Expected: [4, 2, 5, 7, 8]
# 5. Find Second Largest Without sort()
# list1 = [10, 5, 20, 8, 20, 15]
# Find the second-largest unique element without using sort() or sorted().
# Expected: 15
# 6. Rotate List
# list1 = [1, 2, 3, 4, 5]
# Rotate the list 2 positions to the right.
# Expected: [4, 5, 1, 2, 3]
# 7. Pair Elements
# list1 = [10, 20, 30, 40, 50, 60]
# Create: [[10, 60], [20, 50], [30, 40]]
# 8. Find Missing Number
# list1 = [1, 2, 3, 5, 6, 7]
# Find the missing number without sorting.
# Expected: 4
# 9. Separate Repeated Elements
# list1 = [1, 2, 3, 2, 4, 1, 5, 3]
# Create two lists: repeated = [1, 2, 3], non_repeated = [4, 5].
# 10. Find Common Elements Without set()
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 5, 7, 8, 4]
# Create a list containing common elements.
# Expected: [3, 4, 5]
# STRING – Interview Puzzle Questions
# 11. Reverse Words, Not Characters
# s = "Python is easy"
# Reverse the order of words.
# Expected: "easy is Python".
# Constraint: Don't use split()[::-1].
# 12. Reverse Each Word
# s = "Python is easy"
# Reverse each word while keeping the word order.
# Expected: "nohtyP si ysae".
# 13. First Non-Repeated Character
# s = "aabbcddee"
# Find the first character occurring only once.
# Expected: c
# 14. Remove Duplicate Characters
# s = "programming"
# Create a string without duplicate characters while maintaining original order.
# Expected: "progamin".
# 15. Character With Maximum Frequency
# s = "programming"
# Find the character occurring most frequently.
# Expected: m
# 16. Count Words Without split()
# s = "Python is very easy"
# Find the number of words without using split().
# Expected: 4
# 17. Check Anagram Without sorted()
# s1 = "listen"
# s2 = "silent"
# Check whether the two strings are anagrams without using sorted().
# Expected: True
# 18. Move Vowels to Beginning
# s = "programming"
# Create a new string where vowels come first and consonants follow.
# 19. Remove All Repeated Characters
# s = "programming"
# Keep only characters whose frequency is exactly 1.
# 20. Find Longest Word Without max()
# s = "Python programming is interesting"
# Find the longest word without using max().
# Expected: "programming".
# 21. Character Position Puzzle
# s = "abcdef"
# Create a string containing even-index characters followed by odd-index characters.
# Expected: "acebdf".
# 22. String Compression
# s = "aaabbccccd"
# Compress the string using character + count.
# Expected: "a3b2c4d1".
# FUNCTION – Interview Puzzle Questions
# 23. Function Returning Multiple Values
# Write a function that accepts a list and returns minimum, maximum, and average.
# Example: [10, 20, 5, 40, 25]
# Expected: 5, 40, 20.0
# 24. Function to Separate Even and Odd
# Write def separate(numbers) that returns two lists: even numbers and odd numbers.
# Example: [1, 2, 3, 4, 5, 6]
# Expected: [2, 4, 6], [1, 3, 5]
# 25. Function Without Built-in sum()
# Write def total(numbers) that returns the sum of all elements without using sum().
# 26. Function to Find Second Largest
# Write def second_largest(numbers) without using sort() or sorted().
# 27. Recursive String Reverse
# Write a recursive function reverse("python") that returns "nohtyp".
# 28. Recursive Sum of List
# Write def list_sum(numbers) using recursion.
# Example: [10, 20, 30, 40] → 100
# 29. Function as Argument
# Create def calculate(operation, a, b) where operation is another function.
# Example: calculate(add, 10, 20) and calculate(multiply, 10, 20).
# 30. Function With Variable Arguments
# Write a function that accepts any number of numbers using *args and returns their total.
# Example: calculate(10, 20, 30, 40) → 100
# MIXED LIST + STRING + FUNCTION PUZZLES
# 31. List of Strings
# names = ["Anu", "Arun", "Amal", "Binu", "Akhil"]
# Create a list containing only names beginning with "A".
# 32. Longest String
# names = ["cat", "elephant", "dog", "tiger"]
# Write a function to find the longest string without using max().
# Expected: "elephant".
# 33. Sort Strings Based on Length
# words = ["python", "is", "very", "easy"]
# Create: ["is", "very", "easy", "python"].
# First solve using key=len, then solve without sort()/sorted().
# 34. List → Function → Character Count
# words = ["cat", "dog", "python"]
# Write a function that returns the length of each word.
# Expected: [3, 3, 6]
# 35. Function + String Puzzle
# Write remove_vowels("programming") that returns "prgrmmng".
# 36. Function + List + String
# words = ["madam", "python", "level", "hello", "radar"]
# Write a function that returns only palindrome words.
# Expected: ["madam", "level", "radar"]
# 37. Word Frequency
# s = "python is easy and python is powerful"
# Write a function that returns a dictionary containing the frequency of each word.
# 38. Remove Duplicate Words
# s = "python is easy python is powerful"
# Remove duplicate words while maintaining original order.
# Expected: "python is easy powerful".
# 39. List → Function → Sorting
# numbers = [5, 2, 8, 1, 9, 3]
# Write a function that returns two sorted lists: even = [2, 8], odd = [1, 3, 5, 9].
# 40. Final Interview Puzzle
# Write def process(data) for:
# data = ["python", "java", "python", "django", "java", "c"]
# Return the words that occur only once, sorted by their length.
# Expected: ["c", "django"].
# Possible follow-ups: Don't use set(); don't use sorted(); use a dictionary; return duplicate words instead.