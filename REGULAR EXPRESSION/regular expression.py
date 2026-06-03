import re

data="my phone number is 956202020207"

pattern= r"\d\d"

result=re.search(pattern,data)
result1=re.findall(pattern,data)
result2=re.match(pattern,data)


print(result)                                               #output : <re.Match object; span=(19, 21), match='95'>
print(result.group())                                       #output : 95
print(result1)                                              #output : ['95', '62', '02', '02', '02', '07']
print(result2)                                              #output : None
# print(result2.group())
# -----------------------------------------------------------------------------------

data1="my phone number is 956202020207 \n *^@ 😍👌😁"

pattern1=r"\D\D"

result3=re.search(pattern1,data1)
result4=re.findall(pattern1,data1)
result5=re.match(pattern1,data1)


print(result3)                                             #output : <re.Match object; span=(0, 2), match='my'>
print(result3.group())                                     #output : my
print(result4)                                             #output : ['my', ' p', 'ho', 'ne', ' n', 'um', 'be', 'r ', 'is', ' \n', ' *', '^@', ' 😍', '👌😁']
print(result5)                                             #output : <re.Match object; span=(0, 2), match='my'>
print(result5.group())                                     #output : my

# ---------------------------------------------------------------------------------------
print()
data1="my phone number is 956202020207 \n *^@ 😍👌😁"

pattern1=r"\w\w\w"

result3=re.search(pattern1,data1)
result4=re.findall(pattern1,data1)
result5=re.match(pattern1,data1)


print(result3)                                             #output : <re.Match object; span=(3, 6), match='pho'>
print(result3.group())                                     #output : pho
print(result4)                                             #output : ['my', ' p', 'ho', 'ne', ' n', 'um', 'be', 'r ', 'is', ' \n', ' *', '^@', ' 😍', '👌😁']
print(result5)                                             #output : None
# print(result5.group())                                    

# ---------------------------------------------------------------------------------

print()
data1="my phone number is 956202020207 \n *^@ 😍👌😁"

pattern1=r"\W\W"

result3=re.search(pattern1,data1)
result4=re.findall(pattern1,data1)
result5=re.match(pattern1,data1)


print(result3)                                             #output : <re.Match object; span=(31, 33), match=' \n'>
print(result3.group())                                     #output : 

print(result4)                                             #output : [[' \n', ' *', '^@', ' 😍', '👌😁'] ' *', '^@', ' 😍', '👌😁']
print(result5)                                             #output : None
# print(result5.group())                                    

# ---------------------------------------------------------------------------------

print()
data1="my phone number is 956202020207 \n *^@ 😍👌😁"

pattern1=r"\s"

result3=re.search(pattern1,data1)
result4=re.findall(pattern1,data1)
result5=re.match(pattern1,data1)


print(result3)                                             #output : <re.Match object; span=(2, 3), match=' '>
print(result3.group())                                     #output : 
print(result4)                                             #output : [' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ']
print(result5)                                             #output : None
# print(result5.group())                                    

# ---------------------------------------------------------------------------------

print()
data1="my phone number is 956202020207 \n *^@ 😍👌😁"

pattern1=r"\S\S\S"

result3=re.search(pattern1,data1)
result4=re.findall(pattern1,data1)
result5=re.match(pattern1,data1)


print(result3)                                             #output : <re.Match object; span=(3, 6), match='pho'>
print(result3.group())                                     #output : pho
print(result4)                                             #output : ['pho', 'num', 'ber', '956', '202', '020', '207', '*^@', '😍👌😁']
print(result5)                                             #output : None
# print(result5.group())                                    

# ---------------------------------------------------------------------------------

print()
data1="my phone number is 956202020207 \n *^@ 😍👌😁"

pattern1=r"p...e"

result3=re.search(pattern1,data1)
result4=re.findall(pattern1,data1)
result5=re.match(pattern1,data1)


print(result3)                                             #output : <re.Match object; span=(3, 8), match='phone'>
print(result3.group())                                     #output : phone
print(result4)                                             #output : ['phone']
print(result5)                                             #output : None
# print(result5.group())                                    

# ---------------------------------------------------------------------------------

a="call me on +91-95620-20207 or +91-94004-541130"
p = r"\+91-\d\d\d\d\d-\d\d\d\d\d"                          #output : ['+91-95620-20207', '+91-94004-54113']
p1 = r"\+91-\d{5}-\d{5}"                                   #output : ['+91-95620-20207', '+91-94004-54113']
b=re.findall(p,a)
c=re.findall(p1,a)
print(b)
print(c)

# --------------------------------------------------------------------------------------------------------------

print()
data1="my phone number is 956202020207 \n *^@ 😍👌😁"

print(re.search(r"phon",data1))                            #output : <re.Match object; span=(3, 7), match='phon'>
print((re.search(r"phon",data1)).group)                    #output : <built-in method group of re.Match object at 0x00000211BD4E9840>
print((re.search(r"phon",data1)).group())                  #output : phon
print((re.search(r"phon",data1)).start())                  #output : 3
print((re.search(r"phon",data1)).end())                    #output : 7
print((re.search(r"phon",data1)).span())                   #output : (3, 7)






