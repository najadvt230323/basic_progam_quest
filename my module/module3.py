from math import * 

# print(dir())                                        # Lists all names in the current local scope, including imported ones
# print("Square Root of 16 :", sqrt(16))              # Using sqrt from math module
# print("Value of Pi :", pi)                          # Using pi from math module
# print("Value of e :", e)                            # Using e from math module
# print("celling of 4.2 :", ceil(4.2))                # Using ceil from math module
# print("floor of 4.7 :", floor(4.7))                 # Using floor from math module
# print("factorial of 5 :", factorial(5))             # Using factorial from math module
# print("remainder of 10/3 :", remainder(10, 3))      # Using fmod from math module
# print("cosine of 60 degrees :", cos(radians(60)))   # Using cos and radians from math module
# print("tangent of 45 degrees :", tan(radians(45)))  # Using tan and radians from math module

from datetime import *

# print("Current Date and Time :", datetime.now())            # Current date and time
# print("Current Year :", datetime.now().year)                # Current year
# print("Current Month :", datetime.now().month)              # Current month
# print("Current Day :", datetime.now().day)                  # Current day
# print("Current Time :", datetime.now().time())              # Current time
# print("Current Hour :", datetime.now().hour)                # Current hour
# print("Current Minute :", datetime.now().minute)            # Current minute
# print("Current Second :", datetime.now().second)            # Current second
# print("Current Microsecond :", datetime.now().microsecond)  # Current microsecond
# print("Today's Date :", date.today())  # Today's date


# dt = datetime.now()
# print(dt)

# print("%Y  ->", dt.strftime("%Y"))   # Year, full
# print("%y  ->", dt.strftime("%y"))   # Year, short
# print("%m  ->", dt.strftime("%m"))   # Month number
# print("%B  ->", dt.strftime("%B"))   # Month name (full)
# print("%b  ->", dt.strftime("%b"))   # Month name (abbr)
# print("%d  ->", dt.strftime("%d"))   # Day of month
# print("%A  ->", dt.strftime("%A"))   # Weekday name (full)
# print("%a  ->", dt.strftime("%a"))   # Weekday name (abbr)
# print("%H  ->", dt.strftime("%H"))   # Hour (24-hour)
# print("%I  ->", dt.strftime("%I"))   # Hour (12-hour)
# print("%p  ->", dt.strftime("%p"))   # AM/PM
# print("%M  ->", dt.strftime("%M"))   # Minute
# print("%S  ->", dt.strftime("%S"))   # Second
# print("%f  ->", dt.strftime("%f"))   # Microsecond
# print("%z  ->", dt.strftime("%z"))   # UTC offset
# print("%Z  ->", dt.strftime("%Z"))   # Timezone name
# print("%j  ->", dt.strftime("%j"))   # Day of year
# print("%U  ->", dt.strftime("%U"))   # Week number (Sunday first)
# print("%W  ->", dt.strftime("%W"))   # Week number (Monday first)
# print("%c  ->", dt.strftime("%c"))   # Locale’s date and time
# print("%x  ->", dt.strftime("%x"))   # Locale’s date
# print("%X  ->", dt.strftime("%X"))   # Locale’s time

# data = datetime(2002, 8, 25)
# print(data)

# print(data.day)
# print(data.month)
# new_data = data.replace()
# print(new_data)





# today = datetime.today()
# print(today)
# after_7days = today + timedelta()
# print(after_7days)

# time_after_2 = today + timedelta(hours=2, minutes=20)
# print(time_after_2)

# after = datetime.now()
# print(after)

# dob = date(2001, 11, 5)
# today = date.today()

# age_days = today - dob
# print(age_days.days/365)


# d1 = date(2025, 1, 1)
# d2 = date(2025, 1, 15)

# difference = d2 - d1
# print("Difference:", difference)
# print("Days:", difference.days)

# start_date = date.today()
# expiry_date = start_date + timedelta(days=30)

# print("Start Date:", start_date)
# print("Expiry Date:", expiry_date)





# from random import *
# print(random())

# print(randint(0,200))

# print(randrange(0,8,3))

# students = ['shony','priyanka','richu','shahal','yaseen','jasil']
# name = 'sreeraj'

# print(choice(students))
# print(choice(name))

# print(choices(students, k= 9))
# print(choices(name, k= 5))

# shuffle(students)
# print(students)


# print(sample(students,k=2))




# sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)




# print(random())
# print(randint(1,10))

# print(uniform(1,100))
# print(randrange(2,100,6)) #2,8,14,20,26
# print(randrange(3,100,5)) #3,8,13,18,23
# fruits = ['apple','mango','banana','grapes','cherry','avacado','papaya']
# print(choice(fruits))

# sample_set = {1,2,3,4,5,6}
# print(choice(sample_set)) #error

# sample_tuple = (7,8,9,4,5,6,1)
# print(choice(sample_tuple))

# name = 'PYTHON'
# print(choice(name))

# num = range(1,100)
# print(choice(num))

# dict1 = {'name':'quest','phone':789965412}
# print(choice(dict1))#error

# fruits = ['apple','mango','banana','grapes','cherry','avacado','papaya']
# print(choices(fruits,k=4))

# fruits = ['apple','jack fruits','mango','banana','grapes','cherry','avacado','papaya']
# shuffle(fruits)
# print(fruits)


# a=uniform(1,5)
# print(a)
# print(round(a,2))


from random import *
'''
a=randint(1,10)

for i in range(3) :
    b=int(input("enter a intrer 1 to 10 : "))
    if a==b :
        print("win")
        break
    else:
        if a<b:
            print("your are higher")
        else :
            print("your are lover")
        if not i == 1:
            print("try again")

        print("lose")
print(f"a= {a} ")
print("time up")
'''

print(f"result= {choice(["head","tail"])}")

# print(f"result= {choices(["qu:no:1","qu:no:2","qu:no:3","qu:no:3","qu:no:4","qu:no:5","qu:no:6"],k=3)}")

a=["qu:no:1","qu:no:2","qu:no:3","qu:no:3","qu:no:4","qu:no:5","qu:no:6"]
shuffle(a)
print(f"result= {a[:3]}")

print(f"result= {randint(1000,9999)}")

a=2
b=f"{a:03}"
print(a)
print(b)


import os
print(os.path.exists("module2.py"))
print(os.path.exists("folder1\module1.py"))

# os.remove("abc.py")
# os.remove("folder1/abc.py")


# os.mkdir("abcD")                             # CRATE a folder
# os.makedirs("abc/abcd/a")                    # crate a innar folder



# os.rmdir("najad")
# os.rmdir("folder1/najad1")



import shutil
# shutil.rmtree("")

