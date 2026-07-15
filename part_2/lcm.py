print("enter two num :")
a=int(input(""))
b=int(input(""))

c=a*b+1
for i in range(max(a,b),c):
    if i%a==0 and i%b==0:
        print(f"lcm :{i}")
        break
    
for i in range(max(a,b),0,-1):
    if a%i==0 and b%i==0:
        print(f"gcd :{i}")
        break