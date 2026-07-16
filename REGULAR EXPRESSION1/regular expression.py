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
print(result4)                                             #output : ['pho', 'num', 'ber', '956', '202', '020', '207']
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
print()
data1="MY pHone -2   Number 3542 is 956202020207 \n *^@ 😍👌😁"

a=r"[a-z]"
b=r"[A-Z]"
c=r"[a-zA-Z]"
d=r"[0-9]"
e=r"[a-zA-Z0-9]"
f=r"[^a-zA-Z]"
g=r"[^0-9]"
h=r"[^a-zA-Z0-9]"
i=r"^MY"
j=r"^my"
k=r"😁$"
l=r"😍&"

print(re.findall(a,data1))  #output : ['p', 'o', 'n', 'e', 'u', 'm', 'b', 'e', 'r', 'i', 's']
print(re.findall(b,data1))  #output : ['M', 'Y', 'H', 'N']
print(re.findall(c,data1))  #output : ['M', 'Y', 'p', 'H', 'o', 'n', 'e', 'N', 'u', 'm', 'b', 'e', 'r', 'i', 's']
print(re.findall(d,data1))  #output : ['2', '3', '5', '4', '2', '9', '5', '6', '2', '0', '2', '0', '2', '0', '2', '0', '7']
print(re.findall(e,data1))  #output : ['M', 'Y', 'p', 'H', 'o', 'n', 'e', '2', 'N', 'u', 'm', 'b', 'e', 'r', '3', '5', '4', '2', 'i', 's', '9', '5', '6', '2', '0', '2', '0', '2', '0', '2', '0', '7']
print(re.findall(f,data1))  #output : [' ', ' ', '-', '2', ' ', ' ', ' ', ' ', '3', '5', '4', '2', ' ', ' ', '9', '5', '6', '2', '0', '2', '0', '2', '0', '2', '0', '7', ' ', '\n', ' ', '*', '^', '@', ' ', '😍', '👌', '😁']
print(re.findall(g,data1))  #output : ['M', 'Y', ' ', 'p', 'H', 'o', 'n', 'e', ' ', '-', ' ', ' ', ' ', 'N', 'u', 'm', 'b', 'e', 'r', ' ', ' ', 'i', 's', ' ', ' ', '\n', ' ', '*', '^', '@', ' ', '😍', '👌', '😁']
print(re.findall(h,data1))  #output : [' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', '*', '^', '@', ' ', '😍', '👌', '😁']
print(re.findall(i,data1))  #output : ['MY']
print(re.findall(j,data1))  #output : []
print(re.findall(k,data1))  #output : ['😁']
print(re.findall(l,data1))  #output : []

# -------------------------------------------------------------------------------------------------------------------------

print()
data1="MY pHone -2   Number 3542 is 956202020207 \n *^@ 😍👌😁"

a=r"[a-z]{3}"
b=r"[A-Z]{3}"
c=r"[a-zA-Z]{3}"
d=r"[0-9]{3}"
e=r"[a-zA-Z0-9]{3}"
f=r"[^a-zA-Z]{3}"
g=r"[^0-9]{3}"
h=r"[^a-zA-Z0-9]{3}"

print(re.findall(a,data1))  #output : ['one', 'umb']
print(re.findall(b,data1))  #output : []
print(re.findall(c,data1))  #output : ['pHo', 'Num', 'ber']
print(re.findall(d,data1))  #output : ['354', '956', '202', '020', '207']
print(re.findall(e,data1))  #output : ['pHo', 'Num', 'ber', '354', '956', '202', '020', '207']
print(re.findall(f,data1))  #output : [' -2', '   ', ' 35', '42 ', ' 95', '620', '202', '020', '7 \n', ' *^', '@ 😍']
print(re.findall(g,data1))  #output : ['MY ', 'pHo', 'ne ', '   ', 'Num', 'ber', ' is', ' \n ', '*^@', ' 😍👌']
print(re.findall(h,data1))  #output : ['   ', ' \n ', '*^@', ' 😍👌']

# ----------------------------------------------------------------------------------------------------------
print()
data1="MY pHone -2   Number 3542 is 956202020207 \n *^@ 😍👌😁"

pattern=r"\d+"
pattern1=r"\w{3}"
pattern2=r"\w{3,}"

data_pattern=re.compile(pattern)
data_pattern1=re.compile(pattern1)
data_pattern2=re.compile(pattern2)

print(data_pattern.findall(data1))            #output : ['2', '3542', '956202020207']
print(data_pattern1.findall(data1))           #output : ['pHo', 'Num', 'ber', '354', '956', '202', '020', '207']
print(data_pattern2.findall(data1))           #output : ['pHone', 'Number', '3542', '956202020207']

print(data_pattern.search(data1))             #output : <re.Match object; span=(10, 11), match='2'>
print(data_pattern1.search(data1))            #output : <re.Match object; span=(3, 6), match='pHo'>
print(data_pattern2.search(data1))            #output : <re.Match object; span=(3, 8), match='pHone'>

print(data_pattern.search(data1).group())     #output : 2
print(data_pattern1.search(data1).group())    #output : pHo
print(data_pattern2.search(data1).group())    #output : pHone 

# ------------------------------------------------------------------------------------------------------------

print()
data1="MY pHone -2   Number 3542 is 956202020207  *^@ 😍👌😁"

data2=re.sub(r" " , r"_" ,data1)
data3=re.sub(r" " , r"_" ,data1,count=3)
data4=re.subn(r" " , r"_" ,data1)
data5=re.subn(r" " , r"_" ,data1,count=3)
data6=re.split(r" " ,data1)
data7=re.split(r" " ,data1,maxsplit=5)
 
print(data2)                                 #output : MY_pHone_-2___Number_3542_is_956202020207__*^@_😍👌😁
print(data3)                                 #output : MY_pHone_-2_  Number 3542 is 956202020207  *^@ 😍👌😁
print(data4)                                 #output : ('MY_pHone_-2___Number_3542_is_956202020207__*^@_😍👌😁', 11)
print(data5)                                 #output : ('MY_pHone_-2_  Number 3542 is 956202020207  *^@ 😍👌😁', 3)
print(data6)                                 #output : Y', 'pHone', '-2', '', '', 'Number', '3542', 'is', '956202020207', '', '*^@', '😍👌😁']
print(data7)                                 #output : ['MY', 'pHone', '-2', '', '', 'Number 3542 is 956202020207  *^@ 😍👌😁']

# -----------------------------------------------------------------------------------------------------------------------------------











