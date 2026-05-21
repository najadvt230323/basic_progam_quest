class opeartion:
    def add(self,a,b):
        return(a+b)
    def multi(self,a,b):
        return(a*b)   
a1=opeartion()
print(a1.add(10,20))
print(a1.add("naj","ad"))
# print(a1.add("naj",20))     #TypeError: can only concatenate str (not "int") to str

print(a1.multi(10,20))
# print(a1.multi("naj","ad")) #TypeError: can't multiply sequence by non-int of type 'str'
print(a1.multi("naj",4))

