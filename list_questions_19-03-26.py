a=[1,5,6,8,1,4,5,6,9,9]
a.sort()

# print(a[-2])

l=len(a)
for i in range(l-1,0,-1):
    if a[i]>a[i-1]:
        print(a[i-1])
        break

m=max(a)
for i in range(l-1,0,-1):
    if a[i]!=m:
        print(a[i])
        break

s=[1,2,5,6,8,9,9]
large=0
s_large=0
for i in range(len(s)):
    if s[i]>large:
        s_large=large
        large=s[i]
    elif large > s[i] > s_large :
        s_large=s[i]
print (s_large)