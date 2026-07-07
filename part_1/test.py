# class Solution:
#     def addTwoNumbers(self, l1: list, l2:list):
#         a=str()
#         b=str()
#         for i in l1:
#             a=a+str(i)
#         for i in l2:
#             b=b+str(i)
#         a=a[::-1]
#         b=b[::-1]
#         c=int(a)+int(b)
#         c=str(c)
#         print(c)
#         c=c[::-1]
#         d=[]
#         for i in c:
#             d.append(int(i))
#         print(d)

# a=Solution()
# a.addTwoNumbers([2,4,3],[5,6,4])


s="LVIII"

x=s.lower()
a=0
if "iv" in x or "ix" in x or "xl" in x or "xc" in x  or "cd" in x or "cm" in x :
    x= x.replace("iv","4")
    x= x.replace("ix","9")
    x= x.replace("xl","40")
    x= x.replace("xc","90")
    x= x.replace("cd","400")
    x= x.replace("cm","900")
    if "900" in x :
        a=a+900
        x=x.replace("900","a")
    if "400" in x :
        a=a+400
        x=x.replace("400","a")
    if "90" in x :
        a=a+90
        x=x.replace("90","a")
    if "40" in x :
        a=a+40
        x=x.replace("40","a")
    if "9" in x :
        a=a+9
        x=x.replace("9","a")
    if "4" in x :
        a=a+4
        x=x.replace("4","a")
x= x.replace("i","1")       
x= x.replace("v","5")
x= x.replace("x","10")
x= x.replace("l","50")
x= x.replace("c","100")
x= x.replace("d","500")
x= x.replace("m","1000")

if "1000" in x :
    b=x.count("1000")
    a=a+1000*b
    x=x.replace("1000","a")
if "500" in x :
    b=x.count("500")
    a=a+500*b
    x=x.replace("500","a")
if "100" in x :
    b=x.count("100")
    a=a+100*b
    x=x.replace("100","a")
if "50" in x :
    b=x.count("50")
    a=a+50*b
    x=x.replace("50","a")
if "10" in x :
    b=x.count("10")
    a=a+10*b
    x=x.replace("10","a")
if "5" in x :
    b=x.count("5")
    a=a+5*b
    x=x.replace("5","a")
if "1" in x :
    b=x.count("1")
    a=a+1*b
    x=x.replace("1","a")
print(x)
print(a)