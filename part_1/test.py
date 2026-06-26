class Solution:
    def addTwoNumbers(self, l1: list, l2:list):
        a=str()
        b=str()
        for i in l1:
            a=a+str(i)
        for i in l2:
            b=b+str(i)
        a=a[::-1]
        b=b[::-1]
        c=int(a)+int(b)
        c=str(c)
        print(c)
        c=c[::-1]
        d=[]
        for i in c:
            d.append(int(i))
        print(d)

a=Solution()
a.addTwoNumbers([2,4,3],[5,6,4])

