# class opeartion:
#     def add(self,a,b):
#         return(a+b)
#     def multi(self,a,b):
#         return(a*b)   
# a1=opeartion()
# print(a1.add(10,20))
# print(a1.add("naj","ad"))
# # print(a1.add("naj",20))     #TypeError: can only concatenate str (not "int") to str

# print(a1.multi(10,20))
# # print(a1.multi("naj","ad")) #TypeError: can't multiply sequence by non-int of type 'str'
# print(a1.multi("naj",4))

# # ----------------------------------------------------------------------------------------------
# # constcater over loding
# # ========================
# class A:
#     def __init__(self):
#         pass
#     def __init__(self, name, bases, dict, /, **kwds):
#         pass

# # a=A()      #TypeError: A.__init__() missing 3 required positional arguments: 'name', 'bases', and 'dict

# class A:
#     def __init__(self, name, bases, dict, /, **kwds):
#         pass
#     def __init__(self):
#         print("---------------------")

# a=A()            #output : ---------------------


# -------------------------------------------------------------------------------
# meterd ovrrriding in python
# =============================
print()
from oops_inheritance import Animal

a=Animal()
a.eat()
a.sleep()