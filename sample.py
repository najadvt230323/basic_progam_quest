# a=[[1,2,3],[4,5,6],[7,8,9]]
# s=0
# for i in a:
#     for j in i:
#         print(j,end=" ")
#         s+=j
#     print()
# print(s)

# a={i:i**2 if i%2==0 else i**3 for i in range(1,21)}
# b={k**2:v for k,v in a.items() if not k%2==0}
# print(a)
# print(b)

a="fullstack"
b=[]
c=[]
f={}
g=[]
for i in a:
    b.append(i)
    d=a.count(i)
    c.append(d)
e=len(b)
for i in range(e):
    if not i in g:
        f.update({b[i]:c[i]})
        g.append(b[i])
print(f)

a="fullstack"
h={i:a.count(i) for i in a}
print(h)


# a=[10,20,30,40]
# b=[]
# for i in range(1,len(a)):
#     b.append(a[i])
# b.append(a[0])
# print(b)




# a={"a","b","c","d"}
# b={"c","d","e","f"}
# print(a&b)
# print(a-b)
# print(a|b)

# a=[[1,2,3],[4,5,6],[7,8,9]]
# print(f"row 2 : {a[1]}, element : {a[2][1]}")

a=[1,2,3]
b=a
b.append(4)
print(a)

# a=[10,20,10,30,40,20,50,30]
# b=[]
# c=[]
# for i in a:
#     if not i in b:
#         b.append(i)
#     d=a.count(i)
#     if d>1:
#         if not i in c:
#             c.append(i)
# print(a)
# print(b)
# print(c)

# ways to pass valu to a function
# -------------------------------------
# 1.pass by Value
# -------------------------
# -> tha function get acopy of tha data .if tha function changes that copy,
#    tha original variable outside tha function stays tha same

def modify(a:int)-> int:
    print(a)               #output - 5
    a=25
    print(a)               #output - 25
    return(a)
b=5
print(modify(b))           #output - 25
print(b)                   #output - 5






# 2 pass by Referenc
# -----------------------
# -> tha function gets a referenc (a pointer) to tha original data. iftha function 
#     modify
