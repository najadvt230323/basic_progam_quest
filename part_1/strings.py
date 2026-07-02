name="najad"
# a="😍abc123!@#$وعليكم السلام"
# b="وعليكم السلام"

print(type(name))
# print(type(a))
# print(a)
# print(b)

print(len(name))
# print(len(b))

for i in name:
    print(i)
for i in name:
    print(i,end="  ")  
print("")

for i in name:
    print(ord(i),end="  ")  
print("")

lis=[]
asc=[]
name=name.upper()
print(name)
for i in name:
    print(ord(i),end="  ")
    lis.append(i)
    asc.append(str(ord(i)))
    # lis.extend(i)
    # asc.extend(str(ord(i)))
    j=list(str(ord(i)))
    # asc.extend(j)

print("")
print(j)
print(lis)
print(asc)
print(chr(65))

print(name)
print(name[::])
print(name[0::])
print(name[0::1])

print(name[-1::])
print(name[:-1:])
print(name[-4::])
print(name[0:-1:])
print(name[0:-1:1])

print(name[1:])
print(name[1:4])
print(name[:4])

print(name[::2])
print(name[::3])

print(name[::-1])
print(name[-1::-1])
print(name[-1:-4:-1])
print(name[::-2])

for i in range(0,255):
    print (chr(i),end="  ")
print("najad")

place="calicut "
place +="dist"
# place *="dist "----error
# place -="dist "----error
# place +=5 ----error
print(place)
print(place*5)

print(place +" "+ name)
print("dist" in place)
print("cali" in place)
print("calci" in place)

print("")
print("dist" not in place)
print("cali" not in place)
print("calci" not in place)

print("")
print("apple" == "apple")
print("apple" > "banana") 
print("cat" != "dog")

print("")
print(dir(name))

""" 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
'title', 'translate', 'upper', 'zfill' """

# tipe of methods in string
#--------------------------------------
#    1.case conversion methods
#    2.searchig and findigs method
#    3.validation / checking
#    4.modification / replacment
#    5.formatting and alignment
#    6.spliting and joining
#    7.encodind and decoding
#    8.miscellaneous


abc="najad VTK 123"

# 1.case conversion methods
print("# 1.case conversion methods")
print(abc)
print(abc.upper())
print(abc.lower())
print(abc.title())
print(abc.capitalize())
print(abc.swapcase())
print(abc.casefold())

# 2.searchig and findigs method

print("")
print("# 2.searchig and findigs method")
print(abc.find("n"))
print(abc.find("naj"))
print(abc.find("nj"))
print(abc.find("a"))
print(abc.rfind("a"))
print(abc.rfind("aj"))
print("")
print(abc.index("j"))
print(abc.index("ja"))
# print(abc.index("z")) ----error
print(abc.rindex("a"))
print(abc.rindex("aj"))

print("")
print(abc.count("a"))
print(abc.count("z"))


# 3.validation / checking

print("")
print("# 3.validation / checking")
print(abc.isalpha())
print(abc.isdigit())
print(abc.isalpha())
print(abc.istitle())
print(abc.isspace())

print(abc.isascii())  #ord value 0-127
print(ord("f"))
print(chr(200))
a=chr(200)
print("f".isascii())
print(a.isascii())


print("")
print("²".isdigit())
print("²".isdecimal())


print("")
print(abc.isupper())
print(abc.islower())


print("")
print(abc.startswith("na"))
print(abc.endswith("ad"))


# 4.modification / replacment
print("")
print(" # 4.modification / replacment")
#      1.replace("value","replace value",times)
#      2. strip()  /  lstrip()  /  rstrip()
#      3.removeprefix  /  removeprefix


#      1.replace("value","replace value",times)
s="python django django django"
print("")
print("#      1.replace(value,replace value,times)")
print(s.replace("django","devevlopmend",2))
print(s.replace("django","devevlopmend",2))
print(s)

print("")
s=s.replace("django","devevlopmend",2)
print(s)
print(s.replace("django","devevlopmend",2))

#      2. strip()  /  lstrip()  /  rstrip()

print("")
print("#      2. strip()  /  lstrip()  /  rstrip()")
string="         -----python django--------       "
string1="-----python django--------"
string2="aaaaaaaaapython django--------"
print(string)
print(string.strip())
print(string1.strip("-"))
print(string2.strip("a"))
print(string1.lstrip("-"))
print(string1.rstrip("-"))


#        3.removeprefix  /  removesuffix

print("")
print("#        3.removeprefix  /  removesuffix")
string1="-----python django--------"
print(string1.removeprefix("---"))
print(string1.removesuffix("------"))


# 5.formatting and alignment
print("")
print("# 5.formatting and alignment")
print(abc.center(125,("*")))
print(abc.ljust(25,"😁"))
print(abc.rjust(25,"😍"))
print(abc.zfill(25))


print("my name is {} and i am {} years old".format("Alice", 25))
print("my name is {} and i am {} years old".format(25,"Alice"))
print("my name is {1} and i am {0} years old".format(25,"Alice"))
print("my name is {:<10} and i am {} years old".format("Alice", 25))
print("my name is {:>10} and i am {} years old".format("Alice", 25))
print("my name is {:^10} and i am {} years old".format("Alice", 25))
print("my name is {:^10} and i am {:05} years old".format("Alice", 25))
print("my name is {:^10} and  \n i am {:05} years old".format("Alice", 25))
print(r"my name is {:^10} and  \n i am {:05} years old".format("Alice", 25))
print("my name is {:^10} and  \t i am {:05} years old".format("Alice", 25))
print(r"my name is {:^10} and  \t i am {:05} years old".format("Alice", 25))
print("\"\"\'\'")
print(r"\"''!@#$%^&*''\"")

# 6.spliting and joining

s="welcome to the world of python"
s1="welcome-to--the-world of python"
s2="hello world"
s3="hellllo world"
s4=s3.split("l")
s4=s.split()

print("")
print("# 6.spliting and joining")
print(s.split())
print(s.split(" "))
print(s.split(" ",3))
print(s1.split())
print(s1.split("-"))
print(s2.split("l"))
print(s1.split("-",2))
print(s3.split("l"))

print("")
print(s.rsplit(" ",3))
print(s1.rsplit("-",2))
print(s1.rsplit("-",3))

print("")
print(s4)
print(type(s4))

print("")
print("".join(s4))
print(" ".join(s4))
print("❤️".join(s4))

print("")
print("".join(s4))
print("l".join(s4))
print("❤️".join(s4))

s6="job=python="
s7="my name is najad"
print("")
print(s6.partition("="))
print(s6.partition("n="))
print(s6.partition("job=python="))
print(s6.partition("x"))
print(s7.partition(" "))

print("")
print(s6.rpartition("="))
print(s6.rpartition("o"))
print(s6.rpartition("job=python="))
print(s6.rpartition("x"))

# 7.encodind and decoding

s="sreerag"
print("")
print(s)
print(s.encode())
print(s.encode(encoding="utf-8"))
print(s.encode(encoding="utf-8",errors="strict"))
encoded_s=s.encode()
decoded_s=encoded_s.decode()
print(encoded_s)
print(decoded_s)


# 8.miscellaneous
print("")
print("hello\tpython")
print("hello\tpython".expandtabs())
print("hello\tpython".expandtabs(4))
print("hello\tpython".expandtabs(15))
print("hello\tpython".expandtabs(35))
a="hellopython"
b="hello\tpython"
c="hello\tpython".expandtabs(4)
d="hello\tpython".expandtabs(15)
e="hello\tpython".expandtabs(35)

print(len(a))
print(len(b))
print(len(c))         #spaces=tabsize-(curent position / tabsise)
print(len(d))
print(len(e))

# for i in range(1,101):

#     a="\thellopython".expandtabs(i)
#     b="hellop\tython".expandtabs(i)
#     c="hellopython\t".expandtabs(i)
#     print(a)
#     print(len(a))
#     print(b)
#     print(len(b))
#     print(c)
#     print(len(c))


print("")
print("sayana")
print("sayana".translate({97:"x"}))
print("sayana".translate({97:"x" , 115:"y"}))


print("")
text="xxxxxyyyyyyyyyzzzzzz"
text1=text.maketrans("x","a")
text2=text.maketrans("x","a","y")

print(text)
print(text1)
print(text.translate(text1))
print(text.translate(text2))







