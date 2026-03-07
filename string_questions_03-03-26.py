# 1.  Write a Python program to take a string from the user and print the
#     first character using slicing.

# 2.  Write a program to display the last character of a string using
#     slicing.

# 3.  Given a string, print the first 5 characters using slicing.

# 4.  Write a program to print all characters of a string except the first
#     one.

# 5.  Write a program to print all characters of a string except the last
#     one.

# 6.  Given a string, print characters from index 2 to index 6.

# 7.  Write a program to print every character at even index positions
#     using slicing.

# 8.  Write a program to print every character at odd index positions
#     using slicing.

# 9.  Write a program to reverse a string using slicing.

# 10. Given a string, print the middle character(s) using slicing (assume
#     length can be even or odd).

# INTERMEDIATE LEVEL

# 11. Write a program to check whether a string is a palindrome using
#     slicing.

# 12. Given a string, extract the first half and second half using slicing
#     and print them separately.

# 13. Write a program to remove the first and last two characters from a
#     string using slicing.

# 14. Given a string, print characters from index 1 to the second last
#     character.

# 15. Write a program to extract every third character from a string using
#     slicing.

# 16. Given a string, reverse only the first half of the string using
#     slicing.

# 17. Write a program to extract the domain name from an email ID using
#     slicing.

# 18. Given a sentence, extract and print the last word using slicing.

# 19. Write a program to swap the first and last characters of a string
#     using slicing.

# 20. Given a string, print all characters except vowels using slicing and
#     looping logic.

# 21. Write a program to split a string into two parts based on a given
#     index using slicing.

# 22. Given a string, print the string in reverse order skipping every
#     second character.

# 23. Write a program to extract the username from an email ID using
#     slicing.

# 24. Given a string, check whether the first half and second half are
#     equal using slicing.

# 25. Write a program to count how many characters are present in a
#     substring obtained using slicing.

# CONCEPT-FOCUSED PRACTICE

# 26. Write a program to demonstrate positive and negative indexing using
#     slicing.

# 27. Given a string, show the difference between string[start:end] and
#     string[start:end:step].

# 28. Write a program to demonstrate slicing with only start index, only
#     end index, and only step.

# 29. Write a program to safely slice a string even if the index range
#     exceeds the string length.

# 30. Write a program to show that string slicing does not modify the
#     original string.



name="qis Academy"
print(name)
# 1
print(name[0])
# 2
print(name[-1])
# 3
print(name[:5])
# 4
print(name[1:])
# 5
print(name[:-1])
# 6
print(name[2:7])
# 7
print(name[2::2])
# 8
print(name[1::2])
# 9
print(name[::-1])
# 10
a=len(name)
print(a)
if a%2==1:
    a=int(a/2)
    print(name[a])
else:
    a=int(a/2)
    print(name[a-1:a+1])
# 11

# palindrom=name[::-1]
# print(palindrom)

if name[::-1]==name:
    print("the string is palindrom")
else:
    print("the string is not palindrom")

# 12
a=len(name)
print(a)
a=int(a/2)
print(name[:a])
print(name[a:])

# 13
print(name[1:-1])

# 14
print(name[1:-1])

# 15
print(name[::3])

# 16
a=len(name)
print(a)
print(name)
a=int(a/2)
print(name[a::-1])

# 17

a=(name.find("@gmail.com"))
print(a)
print(name[:a])

# 18
a=(name.rfind(" "))
print(name[a+1:])

# 19

print(name[-1],end="")
print(name[1:-1],end="")
print(name[0])

# 20

for i in name:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        pass
    elif i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        pass
    else:
        print(i,end="")

# 21

# a=int(input("enter split index : "))
# b=len(name)
# print(b)
# if a<b-2 and a>=0:
#     print(name[:a])
#     print(name[a:])
# elif a>1-b:
#     print(name[:a])
#     print(name[a:])
# else:
#     print("unable to split")

# 22

print(name[-2::-2])

# 23 = 17

a=(name.find("@gmail.com"))
print(a)
print(name[a:])


# 24

name1="abcabc"
a=len(name1)
b =0
if a%2==0:
    for i in range(0,int(a/2)):
        if not name1[i] == name1[i+int(a/2)]:
            print("first half not equle second half")
            b=b+1 
            break
    if b==0:
        print("first half equle second half")

# 25

# a=input("enter a character : ")
# print(name.count(a))

# 26

print(name[1:-1])

# 27
print(name[1:10])
print(name[1:10:1])
print(name[10:1:-1])

# 28

print(name[1::])
print(name[:10:])
print(name[::-1])

# 29



# 30











