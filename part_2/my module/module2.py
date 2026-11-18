# from folder1.module1 import a,greet

# print(a)
# print(greet("richu"))


# from folder1.module1 import *
# print(a)
# print(pi)
# print(greet("richu"))

# import folder1.module1
# print(folder1.module1.a)
# print(folder1.module1.pi)
# print(folder1.module1.greet("richu"))


import folder1.module1 as t
print(t.a)
print(t.pi)
print(t.greet("richu"))


from folder1.module1 import a as b,greet as c

print(b)
print(c("richu"))


print()
import math
# --------------------------
print(math.pi)
print(math.sqrt(36))
print(math.pow(10,2))
print(math.factorial(5))
print(math.ceil(3.25))
print(math.floor(3.25))
print(math.fabs(-5.5))
print(math.trunc(3.25))
print(math.trunc(-5.9))


from datetime import *

dt=datetime.today()
print(dt)
dt1=datetime(2000,4,5)
year=dt.year-dt1.year
print(year)




