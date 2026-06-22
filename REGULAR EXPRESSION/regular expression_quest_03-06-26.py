import re
test= 'a ab abc abbc abbcc abbbccc aaabbbccc'

print(re.findall(r"a*",test))
#output : ['a', '', 'a', '', '', 'a', '', '', '', 'a', '', '', '', '', 'a', '', '', '', '', '', 'a', '', '', '', '', '', '', '', 'aaa', '', '', '', '', '', '', '']
print(re.findall(r"a\w*",test))
#output : ['a', 'ab', 'abc', 'abbc', 'abbcc', 'abbbccc', 'aaabbbccc']
print(re.findall(r"a+",test))
#output : ['a', 'a', 'a', 'a', 'a', 'a', 'aaa']
print(re.findall(r"a\w+",test))
#output : ['ab', 'abc', 'abbc', 'abbcc', 'abbbccc', 'aaabbbccc']
print(re.findall(r"a?",test))
#output : ['a', '', 'a', '', '', 'a', '', '', '', 'a', '', '', '', '', 'a', '', '', '', '', '', 'a', '', '', '', '', '', '', '', 'a', 'a', 'a', '', '', '', '', '', '', '']
print(re.findall(r"a\w?",test))
#output : ['a', 'ab', 'ab', 'ab', 'ab', 'ab', 'aa', 'ab']

# --------------------------------------------------------------------------------------------

print()
import re
with open ("regex_practice_dataset.txt","r")as f:
    a=f.read()

print("Vehicle Numbers : ",re.findall(r"\w{2}-\d{2}-\w{2}-\d{4}",a)) 
print("IP Addresses : ",re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",a)) 
print("Credit Card Numbers : ",re.findall(r"\d{4}-\d{4,6}-\d{4,5}",a)) 

b=str(re.findall(r"\w{5}\d{4}\w",a))
print("PAN Numbers : ",re.findall(r"\D{5}\d{4}\D",b))

c=r"[A-Z]{5}[0-9]{4}[A-Z]"
print("PAN Numbers : ",re.findall(c,a))

print("EMAIL : ",re.findall(r"\w{3,}@gmail.com",a))
