'''
# **Python Lab – Lambda Function (Beginner to Intermediate)**

## *(Without Higher-Order Functions like map, filter, reduce)*

-----------------------------------------------------------------

## **Section A: Basic Lambda Functions**

1. Write a lambda function to add two numbers.

2. Write a lambda function to subtract two numbers.

3. Write a lambda function to multiply two numbers.

4. Write a lambda function to divide two numbers.

5. Write a lambda function to find the square of a number.

6. Write a lambda function to find the cube of a number.

7. Write a lambda function to find the remainder of two numbers.

8. Write a lambda function to calculate power (a^b).

-----------------------------------------------------------------------

## **Section B: Conditional Lambda Functions**

9. Write a lambda function to check whether a number is even or odd.

10. Write a lambda function to check whether a number is positive or negative.

11. Write a lambda function to check whether a number is positive, negative, or zero.

12. Write a lambda function to find the greater of two numbers.

13. Write a lambda function to find the smaller of two numbers.

14. Write a lambda function to find the maximum of three numbers.

15. Write a lambda function to find the minimum of three numbers.

---------------------------------------------------------------------------------

## **Section C: Number-Based Problems**

16. Write a lambda function to check whether a number is divisible by 5.

17. Write a lambda function to check whether a number is divisible by both 3 and 5.

18. Write a lambda function to find the last digit of a number.

19. Write a lambda function to remove the last digit of a number.

20. Write a lambda function to check whether a number is a multiple of 10.

----------------------------------------------------------------------------------

## **Section D: Formula-Based Problems**

21. Write a lambda function to calculate simple interest.

22. Write a lambda function to calculate the area of a rectangle.

23. Write a lambda function to calculate the area of a square.

24. Write a lambda function to calculate the perimeter of a rectangle.

25. Write a lambda function to calculate the area of a triangle.

26. Write a lambda function to convert Celsius to Fahrenheit.

27. Write a lambda function to convert Fahrenheit to Celsius.

--------------------------------------------------------------------

## **Section E: String-Based Problems**

28. Write a lambda function to convert a string to uppercase.

29. Write a lambda function to convert a string to lowercase.

30. Write a lambda function to find the length of a string.

31. Write a lambda function to get the first character of a string.

32. Write a lambda function to get the last character of a string.

33. Write a lambda function to reverse a string.

34. Write a lambda function to check whether a string is a palindrome.

35. Write a lambda function to count vowels in a string.

36. Write a lambda function to check whether a string starts with 'A'.

----------------------------------------------------------------------------

## **Section F: Intermediate Level Problems**

37. Write a lambda function to calculate the average of three numbers.

38. Write a lambda function to swap two numbers.

39. Write a lambda function to return the absolute value of a number.

40. Write a lambda function to check whether a character is a vowel.

41. Write a lambda function to check whether a character is an alphabet.

42. Write a lambda function to check whether a character is a digit.

43. Write a lambda function to join two strings.

44. Write a lambda function to repeat a string n times.

45. Write a lambda function to calculate the discounted price.

----------------------------------------------------------------------

## **Section G: Output-Based Questions**

46. What is the output of the following?

```
x = lambda a: a + 5
print(x(10))
```

47. What is the output of the following?

```
x = lambda a, b: a if a > b else b
print(x(7, 12))
```

48. What is the output of the following?

```
x = lambda s: s[::-1]
print(x("hello"))
```

49. What is the output of the following?

```
x = lambda n: "Even" if n % 2 == 0 else "Odd"
print(x(14))
```

50. What is the output of the following?

```
x = lambda a, b, c: a + b * c
print(x(2, 3, 4))
```

-----------------------------------------------------

## **Section H: Debugging Questions**

51. Identify and correct the error:

```
add = lambda a, b: a + b
print(add(5))
```

52. Identify and correct the error:

```
square = lambda x: x * x
print(square())
```

53. Find the output:

```
x = lambda a: a if a > 10 else a * 2
print(x(6))
```

54. Find the output:

```
x = lambda s: s.upper()
print(x("hello"))
```

--------------------------------------------------------

## **Section I: Short Lab Test**

55. Write a lambda function to add two numbers.

56. Write a lambda function to find the square of a number.

57. Write a lambda function to check whether a number is even or odd.

58. Write a lambda function to reverse a string.

59. Write a lambda function to check whether a string is a palindrome.

60. Write a lambda function to calculate simple interest.

61. Write a lambda function to convert Celsius to Fahrenheit.

62. Write a lambda function to find the last digit of a number.

63. Write a lambda function to count vowels in a string.

64. Write a lambda function to find the greater of two numbers.

----------------------------------------------------------------------------

'''

# for i  in range(1,65):
#     print(f"# {i} : ")
#     print()
#     print(r"# '''")
#     print()
#     print()
#     print(r"# '''")
#     print()


# 1 :
# Write a lambda function to add two numbers. 

# '''


# '''

# 2 :Write a lambda function to subtract two numbers.

# '''


# '''

# 3 :Write a lambda function to multiply two numbers.  

# '''


# '''

# 4 :
# Write a lambda function to divide two numbers. 

# '''


# '''

# 5 :Write a lambda function to find the square of a number.

# '''


# '''

# 6 :
# Write a lambda function to find the cube of a number. 

# '''


# '''

# 7 : 
# Write a lambda function to find the remainder of two numbers.

# '''


# '''

# 8 :
# Write a lambda function to calculate power (a^b). 

# '''


# '''

# 9 :
# Write a lambda function to check whether a number is even or odd.  

# '''


# '''

# 10 :
# Write a lambda function to check whether a number is positive or negative.

# '''


# '''

# 11 : 
# Write a lambda function to check whether a number is positive, negative, or zero.

# '''


# '''

# 12 :
# Write a lambda function to find the greater of two numbers.  

# '''


# '''

# 13 :
# Write a lambda function to find the smaller of two numbers. 

# '''


# '''

# 14 :
# Write a lambda function to find the maximum of three numbers. 

'''
print("enter a 3 intger  : ")
a=int(input("enter 1st intger : "))
b=int(input("enter 2nd intger : "))
c=int(input("enter 3rd intger : "))
d=lambda x,y,z : x if x>y and x>z else y if y>x and y>z else z if z>y and z>x else f"2 num are maximum : {x}" if x==y and x>z  else f"2 num are maximum : {x}" if x==z and x>y else f"2 num are maximum : {y}" if y==z and y>x else f"3 num are same : {y}"
print(f"the maximum of three numbers : {d(a,b,c)}")

'''

# 15 :
# Write a lambda function to find the minimum of three numbers. 

'''
print("enter a 3 intger  : ")
a=int(input("enter 1st intger : "))
b=int(input("enter 2nd intger : "))
c=int(input("enter 3rd intger : "))
d=lambda x,y,z : x if x<y and x<z else y if y<x and y<z else z if z<y and z<x else "2 num are minmum {x}" if x==y and x<z  else "2 num are minmum {x}" if x==z and x<y else "2 num are minmum {y}" if y==z and y<x else "3 num are same {y}"
print(f"the minimum of three numbers : {d(a,b,c)}")

'''

# 16 :
# Write a lambda function to check whether a number is divisible by 5. 

'''
print("a number is divisible by 5")
print("-------------------------------")
a=int(input("enter a intger  : "))
b=lambda x: "number is divisible by 5" if x%10==5 else "number is NOT divisible by 5"
print(b(a))

'''

# 17 :
# Write a lambda function to check whether a number is divisible by both 3 and 5. 

'''
a=int(input("enter a number : "))
b=lambda a:"multipel of 5" if a%5==0 and not a%3==0 else "multipel of 3" if not a%5==0 and a%3==0 else "multipel of 3 and 5" if  a%5==0 and a%3==0 else "not multipel of 3 and 5"
print(b(a))
'''

# 18 : 
# Write a lambda function to find the last digit of a number.

'''
a=int(input("enter a number : "))
b=lambda x: x%10
print(f"the last digit of a number : {b(a)}")

'''

# 19 :
# Write a lambda function to remove the last digit of a number. 

'''
a=int(input("enter a number : "))
b=lambda x: int(x/10)
print(f"remove the last digit of a number : {b(a)}")

'''

# 20 :
# Write a lambda function to check whether a number is a multiple of 10. 

'''
print("a number is a multiple of 10")
print("-------------------------------------------------")
a=int(input("enter a intger  : "))
b=lambda x: "number is a multiple of 10" if x%10==0 else "number is not a multiple of 10"
print(b(a))

'''

# 21 : 
# Write a lambda function to calculate simple interest.

'''
print("calculate simple interest and compound interest.")
print("-------------------------------------------------")
amond=int(input("enter the amnd : "))
year=int(input("enter the how many years : "))
inter=int(input("enter the interest rate : "))
sim_in=lambda a,b,c:((a*b*c)/100)
print(f"simple interest : {sim_in(amond,year,inter)} \ntotel : {amond+sim_in(amond,year,inter)}")

'''

# 22 :
# Write a lambda function to calculate the area of a rectangle. 

'''
print("the area of a square.")
print("enter tha 2 sides of a rectangle.")
a=int(input("enter 1st side : "))
b=int(input("enter 2nd side : "))
c=lambda a,b:a*b
print(f"area of a rectangle : {c(a,b)}")

'''

# 23 :
# Write a lambda function to calculate the area of a square. 

'''
print("the area of a square.")
a=int(input("enter side : "))
c=lambda a:a*a
print(f"area of a rectangle : {c(a)}")

'''

# 24 :
# Write a lambda function to calculate the perimeter of a rectangle.

'''
print("the perimeter of a rectangle.")
print("enter tha 2 sides of a rectangle.")
a=int(input("enter 1st side : "))
b=int(input("enter 2nd side : "))
c=lambda a,b:2*(a+b)
print(f"perimeter of a rectangle : {c(a,b)}")

'''

# 25 :
# Write a lambda function to calculate the area of a triangle.  

'''
print("the area of a triangle.")
print("enter tha 3 sides of a triangle.")
a=int(input("enter 1st side : "))
b=int(input("enter 2nd side : "))
c=int(input("enter 3rd side : "))
d=(a+b+c)/2
e=lambda a,b,c,d:(d*(d-a)*(d-b)*(d-c))**.5
print(f"area of a triangle : {e(a,b,c,d)}")

'''

# 26 :
# Write a lambda function to convert Celsius to Fahrenheit. 

'''
a=int(input("enter tha Celsius :"))
b= lambda x:(x*9/5)+32
print(f"Fahrenheit : {b(a)}")
'''
'''
a=int(input("enter tha Fahrenheit :"))
b= lambda x:(x- 32)*5/9
print(f"Celsius : {b(a)}")
'''

# 27 : 
# Write a lambda function to convert Fahrenheit to Celsius.

'''
a=int(input("enter tha Fahrenheit :"))
b= lambda x:(x- 32)*5/9
print(f"Celsius : {b(a)}")
'''
'''
a=int(input("enter tha Celsius :"))
b= lambda x:(x*9/5)+32
print(f"Fahrenheit : {b(a)}")
'''

# 28 :
# Write a lambda function to convert a string to uppercase.

'''
a=input("enter a stering :")
b=lambda x: x.upper()
print(b(a))

'''

# 29 :
# Write a lambda function to convert a string to lowercase. 

'''
a=input("enter a stering :")
b=lambda x: x.lower()
print(b(a))

'''

# 30 :
# Write a lambda function to find the length of a string 

'''
a=input("enter a stering :")
b=lambda x: len(x)
print(b(a))

'''

# 31 :
# Write a lambda function to get the first character of a string. 

'''
a=input("enter a stering :")
b=lambda x: x[0]
print(b(a))

'''
'''
a=['najad',"richu","aju","fazil"]
print(list(map(lambda x: x[0],a)))

'''

# 32 :
# Write a lambda function to get the last character of a string. 

'''
a=input("enter a stering :")
b=lambda x: x[-1]
print(b(a))

'''
'''
a=['najad',"richu","aju","fazil"]
print(list(map(lambda x: x[-1],a)))

'''

# 33 :Write a lambda function to reverse a string.

'''
a=input("enter a stering :")
b=lambda x: x[::-1]
print(b(a))

'''
'''
a=['najad',"richu","aju","fazil"]
print(list(map(lambda x: x[::-1],a)))

'''

# 34 :Write a lambda function to check whether a string is a palindrome.  

'''
a=input("enter a stering :")
b=lambda x: x[::-1]
if a==b(a):
    print("stering is a palindrome")
else:
    print("stering is not a palindrome")

'''

# 35 :Write a lambda function to count vowels in a string. 

'''
a=input("enter a stering :")
b=lambda x: sum(1 for i in a if i in "aeiou")
print(b(a))

'''

# 36 :
# Write a lambda function to check whether a string starts with 'A'. 

'''
a=input("enter a stering :")
b=lambda x: "yes,string starts with 'A'" if x[0]=="a" or x[0]=="A" else "no,string not starts with 'A'"
print(b(a))

'''

# 37 :
# Write a lambda function to calculate the average of three numbers. 

'''
print("calculate the average of three numbers.")
a=int(input("enter 1st inger : "))
b=int(input("enter 2nd inger : "))
c=int(input("enter 3rd inger : "))
d=lambda x,y,z: (x+y+z)/3
print(d(a,b,c))

'''

# 38 :
# Write a lambda function to swap two numbers. 

'''
print("swap two numbers.")
a=int(input("enter 1st inger : "))
b=int(input("enter 2nd inger : "))
print(a,b)
c=lambda x,y :(y,x)
a,b=c(a,b)
print(a,b)

'''

# 39 :Write a lambda function to return the absolute value of a number. 

'''
print("absolute value of a number")
a=int(input("enter number : "))
b= lambda a :a*-1 if a<0 else a
print(f"absolute value of a number : {b(a)}")

'''

# 40 :
# Write a lambda function to check whether a character is a vowel. 

'''
a=input("enter a stering :")
b=lambda x: True if x[0] in "aeiouAEIOU" else False
print(b(a))

'''

# 41 :
# Write a lambda function to check whether a character is an alphabet. 

'''
a=input("enter a stering :")
b=lambda x: True if x.isalpha() else False
print(b(a))

'''

# 42 :
# Write a lambda function to check whether a character is a digit. 

'''
a=input("enter a stering :")
b=lambda x: True if x.isdigit() else False
print(b(a))

'''

# 43 :
# Write a lambda function to join two strings. 

'''
a=input("enter a stering :")
b=input("enter anther stering :")
c=lambda x,y: x+y
print(c(a,b))

'''

# 44 :
# Write a lambda function to repeat a string n times. 

'''
a=input("enter a stering :")
b=int(input("hwo many times repeat stering :"))
c=lambda x,y: x*y
print(c(a,b))

'''

# 45 :
# Write a lambda function to calculate the discounted price. 

'''
a=int(input("enter tha price :"))
b=lambda x:x-(x*.1) if x<=100 else  x-(x*.2) if x<=200 else  x-(x*.3) if x<=300 else  x-(x*.4) if x<=400 else x-(x*.5)
print(b(a))

'''

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

# 51 : 

# '''


# '''

# 52 : 

# '''


# '''

# 53 : 

# '''


# '''

# 54 : 

# '''


# '''

# 55 : 

# '''


# '''

# 56 : 

# '''


# '''

# 57 : 

# '''


# '''

# 58 : 

# '''


# '''

# 59 : 

# '''


# '''

# 60 : 

# '''


# '''

# 61 : 

# '''


# '''

# 62 : 

# '''


# '''

# 63 : 

# '''


# '''

# 64 : 

# '''


# '''




