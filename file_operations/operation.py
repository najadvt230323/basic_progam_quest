# f=open("sample.txt")
# print(f.read())
# f.close()

# files=open("test.py","r+")
# print(files.read())
# files.write("\nprint(a,b,c,d)")
# files.close()

# with open("sample.txt") as f:
#     print(f.read())

# with open("test.py","r+") as f1:
#     print(f1.read())
#     f1.write("\nprint(a,b,c,d)")

# with open("test.py","r+") as f1:
#     f1.write("\nprint(a,b,c,d)")

# "r" → read (default)
# "w" → write (overwrites file)
# "a" → append (adds to file)
# "x" → create (fails if file exists)
# "b" → binary mode (e.g., images)

# with open("text1.py","w") as f1:
#     f1.write("a=1\nb=2\nc=3\nd=a+b+c\nprint(a,b,c,d)")

# with open("text1.py","w") as f1:
#     pass

# with open("text2.py","w") as f1:
#     f1.write("a=1\nb=2\nc=3\nd=a+b+c\nprint(a,b,c,d)")


# with open("text4.py","w+")as f:
#     f.read()
#     f.write("hi najad")
#     f.write("\nhow are you")


# with open("text4.txt","w+")as f:
#     # print(f.read())
#     f.write("hi najad")
#     # print(f.read())
#     f.write("\nhow are you")
#     print(f.read())
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     print(f.read())
#     print(f.read())


# with open("text4.txt","a")as f:
#     print(f.tell())
#     # print(f.read())
#     f.write("\nhi najad")
#     # print(f.read())
#     f.write("\nhow are you")
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())


# with open("text4.txt","a+")as f:
#     print(f.tell())
#     print(f.read())
#     f.write("\nhi najad")
#     f.write("\nhow are you")
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     print(f.read())

# with open("text4.txt","x")as f:
#     pass                          #FileExistsError: [Errno 17] File exists: 'text4.txt'


# with open("text5.txt","x+")as f:
#     print(f.tell())
#     print(f.read())
#     f.write("\nhi najad")
#     f.write("\nhow are you")
#     print(f.tell())
#     f.seek(0) 
#     print(f.tell())
#     print(f.read())







# with open("iron-man.jpg","w+b")as f:
#     a=f.read()
#     f.write(a)
#     print(f.tell())

# with open("text5.txt","a+")as f:
#     print(f.writable())
#     print(f.readable())
#     print(f.tell())
#     f.seek(0)
#     print(f.readline())
#     print(f.tell())
#     print(f.readline())
#     print(f.readline())

# with open("text5.txt","a+")as f:
#     print(f.tell())
#     print(f.readlines())
#     f.seek(0)
#     print(f.readlines())
#     f.seek(0)
#     a=f.readlines()
# print(a)


# with open("text6.txt","w+")as f:
#     for i in range(len(a)):
#         f.write(a[i])

# with open("text6.txt","w+")as f:
#     f.writelines(a)


'''

with open("loki.jpg","r+b")as f:
    a=f.read()
    # print(f.tell())


with open("iron-man1.jpg","r+b")as f:
    b=f.read()

with open("iron-man.jpg","w+b")as f:
    # f.read()
    # f.write(a)
    f.write(b)

print(len(a))
print(len(b))
c=len(a)
d=len(b)
e=len(a)+len(b)
# print(e)
f=0
g=""
while f<e:
    for i in range(len(a)):
        g=g+a[i]
        if i<len(b):
            g=g+b[i]
    f=len(g)
print(len(g))



with open("iron-man.jpg","w+b")as f:
    # f.write(a)
    f.write(b)

'''

