# if __name__ == '__main__':
#     n = int(input().strip())
# if n%2==1:
#     print("Weird")
# elif n>=2 and n<=5 and n%2==0:
#     print("Not Weird")
# elif n<=20 and n>=6:
#     print("Weird")
# elif n>20:
#     print("Not Weird")


# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# r=[]
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if not i+k+j==n:
#                 r.append([i,j,k])
# print(r)


# n = int(input())
# c=input()
# a=c.split()
# print(a)
# for i in range(n):
#     a[i]=int(a[i])
# for i in  range(n-1):
#     for j in range(n-1):
#         if a[j]>a[j+1] :
#             b=a[j]
#             a[j]=a[j+1]
#             a[j+1]=b
# print(a)
# for i in range(n-1,0,-1):
#     if a[i]>a[i-1]:
#         print(a[i-1])
#         break


# def swap_case(s):
#     s=s.swapcase()
#     return(s)

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

# def split_and_join(line):
#     # write your code here
#     l=line.split()
#     l1="-".join(l)
#     return(l1)
    

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)


# def print_full_name(first, last):
#     # Write your code here
#     print(f"Hello {first} {last}! You just delved into python.")
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

def mutate_string(string, position, character):
    s=""
    for i in range(position):
        s=s+string[i]
    s=s+character
    l=len(string)
    for i in range(position+1,l):
        s=s+string[i]
    return(s)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


