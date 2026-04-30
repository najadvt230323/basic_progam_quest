# f=open("sample.txt")
# print(f.read())
# f.close()

# files=open("test.py","r+")
# print(files.read())
# files.write("\nprint(a,b,c,d)")
# files.close()

with open("sample.txt") as f:
    print(f.read())

with open("test.py","r+") as f1:
    print(f1.read())
    f1.write("\nprint(a,b,c,d)")

with open("test.py","r+") as f1:
    f1.write("\nprint(a,b,c,d)")

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


