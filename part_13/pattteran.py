n=5
a=n
for i in range(1,n+1):
    for j in range(i):
        print("* ",end="")
    print("")

for i in range(n+1,0,-1):
    for j in range(i):
        print("* ",end="")
    print("")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print("")

for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print("")

for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print("")

for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("")

for i in range(1,n+1):
    for j in range(i):
        print("a ",end="")
    print("")

for i in range(1,n+1):
    for k in range(a+1,1,-1):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    a=a-1
    print("")     
for i in range(n,0,-1):
    for k in range(0,a+1):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    a=a+1
    print("") 
