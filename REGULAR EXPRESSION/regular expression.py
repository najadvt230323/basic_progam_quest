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

print(re.findall(r"phon",data1))                           #output : ['phon']
print(re.findall(r"\d",data1))                             #output : ['9', '5', '6', '2', '0', '2', '0', '2', '0', '2', '0', '7']
print(re.findall(r"\d\d",data1))                           #output : ['95', '62', '02', '02', '02', '07']
print(re.findall(r"\d{5}",data1))                          #output : ['95620', '20202']
print(re.findall(r"\d{7}",data1))                          #output : ['9562020']
print(re.findall(r"\d{7,}",data1))                         #output : ['956202020207']
print(re.findall(r"\d{3,5}",data1))                        #output : ['95620', '20202']
print(re.findall(r"\d{,3}",data1))#output : ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '956', '202', '020', '207', '', '', '', '', '', '', '', '', '', '', '']

print(re.findall(r"\w{3}",data1))                           #output : ho', 'num', 'ber', '956', '202', '020', '207']
print(re.findall(r"\w{3,}",data1))                          #output : ['phone', 'number', '956202020207']
print(re.findall(r"\w{3,5}",data1))                         #output : ['phone', 'numbe', '95620', '20202']
print(re.findall(r"\w{,6}",data1))#output : ['my', '', 'phone', '', 'number', '', 'is', '', '956202', '020207', '', '', '', '', '', '', '', '', '', '', '']

# --------------------------------------------------------------------------------------------------------
print()
data1="my phone -2   number 3542 is 956202020207 \n *^@ 😍👌😁"

print(re.findall(r"\d+",data1))                             #output : ['2', '3542', '956202020207']
print(re.findall(r"\d+4",data1))                             #output : ['354']
print(re.findall(r"\d+0",data1))                             #output : ['95620202020']

print(re.findall(r"\w+",data1))                             #output : ['my', 'phone', '2', 'number', '3542', 'is', '956202020207']
print(re.findall(r"\w+4",data1))                             #output : ['354']
print(re.findall(r"\w+e",data1))                             #output : ['phone', 'numbe']

print()
print(re.findall(r"\d*",data1))#output : ['', '', '', '', '', '', '', '', '', '', '2', '', '', '', '', '', '', '', '', '', '', '3542', '', '', '', '', '956202020207', '', '', '', '', '', '', '', '', '', '', '']
print(re.findall(r"\d*4",data1))                             #output : ['354']
print(re.findall(r"\d*0",data1))                             #output : ['95620202020']

print(re.findall(r"\w*",data1))#output : ['my', '', 'phone', '', '', '2', '', '', '', 'number', '', '3542', '', 'is', '', '956202020207', '', '', '', '', '', '', '', '', '', '', '']
print(re.findall(r"\w*4",data1))                             #output : ['354']
print(re.findall(r"\w*e",data1))                             #output : ['phone', 'numbe']

print()
print(re.findall(r"\d?",data1))#output : ['', '', '', '', '', '', '', '', '', '', '2', '', '', '', '', '', '', '', '', '', '', '3', '5', '4', '2', '', '', '', '', '9', '5', '6', '2', '0', '2', '0', '2', '0', '2', '0', '7', '', '', '', '', '', '', '', '', '', '', '']
print(re.findall(r"\d?4",data1))                             #output : ['54']
print(re.findall(r"\d?0",data1))                             #output : ['20', '20', '20', '20']

print(re.findall(r"\w?",data1))#output : ['m', 'y', '', 'p', 'h', 'o', 'n', 'e', '', '', '2', '', '', '', 'n', 'u', 'm', 'b', 'e', 'r', '', '3', '5', '4', '2', '', 'i', 's', '', '9', '5', '6', '2', '0', '2', '0', '2', '0', '2', '0', '7', '', '', '', '', '', '', '', '', '', '', '']
print(re.findall(r"\w?4",data1))                             #output : ['54']
print(re.findall(r"\w?e",data1))                             #output : ['ne', 'be']

# -----------------------------------------------------------------------------------------------------
