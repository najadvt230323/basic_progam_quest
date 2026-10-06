a=[]
sum=0
i=int(input("enter how many numbers :"))
c=i
d=i

print("enter tha number")
for i in range(i):
    b=float(input())
    sum=sum+b
    a.append(b)
print(f"your enterd values:{a}")
# print(i)
print(f"totel sum : {sum}")

while c>=0:
    for i in range(i):
     if a[i]>a[i+1]:
        e=a[i+1]
        a[i+1]=a[i]
        a[i]=e
    c=c-1
print("ascending order:")
for d in range (d):
 print(a[d], end=" ")
print(" ")
# d=d+1
print("descending order:")
for d in range(d,-1,-1):
 print(a[d], end=" ")
print(" ")

print(f"largest number :{a[-1]}")
print(f"lowest number :{a[0]}")
print(f"second largest number :{a[-2]}")
print(f"second lowest number :{a[1]}")

# for d in range (0,d):
#  print(a[d])
# print(d)
