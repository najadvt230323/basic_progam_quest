sum=0
rev=0
arm=0
b=int(input("enter minimum 2 digit intgar number :"))
a=c=b
if a>10:
 while a>0:
    
    sum=sum+a%10
    arm=arm+pow(a%10,3)
    rev=rev*10+(a%10)
    a=int(a/10)

 print(f"sum = {sum}")
 print(f"reves={rev}")
else:
  print("error")

if b==arm:
   print(f"this number is armstong")
else:
   print(f"this number is not a armstong")