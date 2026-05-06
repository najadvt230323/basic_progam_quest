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