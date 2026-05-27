# TypeError
# ==========
# for i in range():
#     print(i)


# ZeroDivisionError: division by zero
# ====================================
# print(10/0)


# TypeError: can only concatenate str (not "int") to str
# =======================================================
# Name="najad"
# print(Name+10)


# IndexError: list index out of range
# =====================================
# n=[1,2,3,4,5]
# print(n[6])


# KeyError: 'grade'
# ==================
# s={"name" : "john","age":20}
# print(s["grade"])


# FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt'
# =================================================================
# open("abc.txt")


# NameError: name 'x' is not defined
# ====================================
# print(x)


# AttributeError: 'str' object has no attribute 'sort'
# ======================================================
# text="hello"
# print(text.sort())


# ModuleNotFoundError: No module named 'quest'
# =============================================
# import quest

# --------------------------------------------------------------------------------------------
'''
a=int(input("entet 1st num :"))
b=int(input("enter 2nd num :"))

try:
    print(a/b)
except:
    print("can't devisible zero...")               #output : can't devisible zero...

print("-----------------------------")

try:
    print(a/b)
except ZeroDivisionError:
    print("can't devisible zero...",ZeroDivisionError)     #output : can't devisible zero... <class 'ZeroDivisionError'>

print("------------------------------------------------")

try:
    print(a/b)
except ZeroDivisionError as e:
    print("can't devisible zero...",e)     #output : can't devisible zero... division by zero

print("------------------------------------------------")

try:
    print(a/b)
except ZeroDivisionError as e:
    print("can't devisible zero...",e)     #output : can't devisible zero... division by zero
else:
    print("ther is no error in try block")
finally:
    print("tha code as must ren")

print("------------------------------------------------")

'''
# -------------------------------------------------------------------------------------------------

try:
    import abcd

except ModuleNotFoundError as e:
    print(e)                          #output : No module named 'abcd'
except Exception as e:
    print("Genral block ",e)

print("---------------------------------")


try:
    import abcd
except Exception as e:
    print("Genral block ",e)                 #output : Genral block  No module named 'abcd'
except ModuleNotFoundError as e:
    print(e)                         


print("---------------------------------")
,                                                                                                                                                 

