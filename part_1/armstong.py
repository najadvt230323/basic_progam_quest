# armstong number
d="y"
while d=="y" or d=="Y":
    num=int(input("enter a number : "))
    a=b=num
    i=c=arm=0

    while a/10>0:
        i+=1
        c=c*10+a%10
        a=int(a/10)
        
    print(f"number of digets : {i}")
    print(f"the reverse of number : {c}")
    while b/10>0:
        # r=1
        # for j in range(0,i):
        #     r=r*(b%10)
        # arm=arm+r

        # arm=arm+pow((b%10),i)

        arm=arm+((b%10)**i)

        b=int(b/10)
    if arm==num:
        print(f"the {num} number is armstong number")
    else:
        print(f"the {num} number is not armstong number")
    if c==num:
        print(f"the {num} number is palindrome number")
    else:
        print(f"the {num} number is not palindrome number")
    d=input("do you want repeat (y/n) : ")

# triangle

'''import math
d="y"
while d=="y" or d=="Y":
    print("enter the 3 side of triangle")
    a=int(input())
    b=int(input())
    c=int(input())
    if a+b>c and b+c>a and c+a>b:
        if a==b and b==c:
            print("this triangle is equilateral triangle")
        elif a==b or b==c or c==a:
            print("this triangle is isosceles triangle")
        else:
            print("this triangle is scalene triangle")
        s=(a+b+c)/2
        area= math.sqrt(s*(s-a)*(s-b)*(s-c))
        # area= (s*(s-a)*(s-b)*(s-c))**.5
        print(f"area of triangle = {round(area,2)}")
    else:
        print("this is not a triangle")
    d=input("do you want repeat (y/n) : ")'''


