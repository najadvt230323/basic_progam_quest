# a=[[1,2,3],[4,5,6],[7,8,9]]
# s=0
# for i in a:
#     for j in i:
#         print(j,end=" ")
#         s+=j
#     print()
# print(s)

a={i:i**2 if i%2==0 else i**3 for i in range(1,21)}
b={k**2:v for k,v in a.items() if not k%2==0}
print(a)
print(b)