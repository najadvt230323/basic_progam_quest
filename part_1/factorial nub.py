a=int(input("entera number:"))
fact=1
fino=0
b=1
x=0
y=0
if a>0:
 for i in range(1,a+1):
  fact=fact*i
else:
 print("enter a valued number")
print(f"factoriyal of {a}! = {fact}")
# print(a)
print(f"fibonacci of {a} = ")
if a>0:
 for i in range(0,a):
  print(fino, end=" ")
  c=fino
  fino=fino+b
  b=c
print(" ")

for i in range(2,a):
 if a%i==0:
  print(f"{a} is not a prime number")
  break
if i==a-1:
   print(f"{a} is prime number")

print("prime number between 1-100 : 1 2",end=" ")
# print(i)
while x<100:
    x=x+1
    y=0
    for i in range(2,x):
      if x%i==0:
        y=y+1
    if i==x-1 and y==0:
     print(x,end=" ")   
