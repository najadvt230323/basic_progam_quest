'''
🔹 Section A: Basic File Opening (r mode)
------------------------------------------------------------------
Write a Python program to open a file in read (r) mode and display its content.
Write a program to read the first 10 characters from a file.
Write a program to print all lines using a loop.
Write a program to count total characters in a file.
Write a program to count total lines in a file.
Write a program to display only the first line of a file.
Write a program to display the last line of a file.
Write a program to read a file and print it in uppercase.
Write a program to read a file and count number of words.
Write a program to check what happens if file does not exist in r mode.
Write a program to read a file using with statement.
Write a program to check if file is closed after reading.
Write a program to print alternate lines from a file.
Write a program to read file content and reverse it.

🔹 Section B: Writing Files (w mode)
-----------------------------------------------
Write a program to create a file using write (w) mode.
Write a program to write a single line into a file.
Write a program to write multiple lines into a file.
Write a program to overwrite existing file content.
Write a program to write user input into a file.
Write a program to create a file and write numbers from 1 to 10.
Write a program to write a list of names into a file.
Write a program to write formatted text into a file.
Write a program to write content and close the file manually.
Write a program using with statement to write into a file.
Write a program to demonstrate that w mode overwrites existing data.
Write a program to write a paragraph into a file.
Write a program to write data and check file size.
Write a program to write lowercase letters into a file.
Write a program to write even numbers into a file.

🔹 Section C: Read + Write Mode (r+)

Write a program to open a file in r+ mode and display content.
Write a program to read a file and then write additional data using r+.
Write a program to overwrite the beginning of a file using r+.
Write a program to modify the first line of a file using r+.
Write a program to read and append data using r+.
Write a program to move file pointer and write data.
Write a program to demonstrate pointer position in r+ mode.
Write a program to update specific content in a file using r+.
Write a program to replace a word in a file using r+.
Write a program to read and rewrite file content using r+.

🔹 Section D: Mixed Practice Questions
--------------------------------------------------------
Write a program to copy content from one file to another using r and w.
Write a program to merge two files into a third file.
Write a program to read file and write only vowels into another file.
Write a program to read file and write only consonants into another file.
Write a program to read numbers from file and write their squares into another file.
Write a program to read file and remove blank lines.
Write a program to read file and write reversed lines into another file.
Write a program to read file and count frequency of a word.
Write a program to read file and write unique words into another file.
Write a program to read file and write lines starting with a vowel into another file.

🔹 Section E: Small Practical 
---------------------------------------------
Create a file student.txt, write student names, then read and display them.
Create a file marks.txt, write marks, then read and calculate total.
Create a file and update its first line using r+.
Read a file and duplicate its content into another file.
Write a program to demonstrate all three modes (r, w, r+) in one program.

'''
# for i  in range(1,55):
#     print(f"# {i} : ")
#     print()
#     print(r"# '''")
#     print()
#     print()
#     print(r"# '''")
#     print()


# 1 :
# Write a Python program to open a file in read (r) mode and display its content. 

'''
with open ("sample.txt" , "r") as f:
    a=f.read()
    print(a)

'''

# 2 :
# Write a program to read the first 10 characters from a file. 

'''
with open ("sample.txt" , "r") as f:
    a=f.read()
    print(a[:10])

'''

# 3 :'
# Write a program to print all lines using a loop. 

'''
with open ("sample.txt" , "r") as f:
    a=f.read()
    for i in a:
        if not i=="\n":
            print(i,end="")
    print() 
    for i in a:
        if not i=="\n":
            print(i,end="")
        else:
            print()
'''

# 4 :
# Write a program to count total characters in a file.

'''
with open ("sample.txt" , "r") as f:
    a=f.read()
    print(len(a))

'''

# 5 :
# Write a program to count total lines in a file.

'''
with open ("sample.txt" , "r") as f:
    a=f.read()
    b=1
    for i in a:
        if i=="\n":
            b+=1
    print(f"lines in a file : {b}")

'''

# 6 :
# Write a program to display only the first line of a file.
  
'''
with open ("sample.txt" , "r") as f:
    a=f.read()
    for i in a:
        if not i=="\n":
            print(i,end="")
        else:
            break
    print()

'''

# 7 :
# Write a program to display the last line of a file.  

'''
with open ("sample.txt" , "r") as f:
    a=f.read()
    b=a.split("\n")
    print(b[-1])


'''

# 8 :
# Write a program to read a file and print it in uppercase.

'''
with open("sample.txt" , "r") as a:
    b=a.read().upper()
    print(b)

'''

# 9 :
# Write a program to read a file and count number of words.

'''
with open("text1.py","r") as f:
    a=f.read().count(" ")+1
    print(a)
    
'''

# 10 :
# Write a program to check what happens if file does not exist in r mode.  

'''
with open("text10.py","r") as f:
    a=f.read().count(" ")+1          
    print(a)                           #FileNotFoundError: [Errno 2] No such file or directory: 'text10.py'
    

'''

# 11 : 
# Write a program to read a file using with statement. 

'''
with open("text1.py","r") as f:
    print(f.read())

'''

# 12 :
# Write a program to check if file is closed after reading.

'''
with open("text1.py","r") as f:
    print(f.read())
# print(f.read())                 #ValueError: I/O operation on closed file.

'''

# 13 :
# Write a program to print alternate lines from a file.

'''
with open("sample.txt","r")as f:
    a=f.read()
    b=1
    c="\n"
    print() 
    for i in a:
        if c=="\n":
            print(f"line {b} :",end="")
            b=b+1
        if not i=="\n":
            print(i,end="")
        else:
            print()
        c=i
print()
'''

# 14 :
# Write a program to read file content and reverse it.   

'''
with open("sample.txt","r") as f:
    print(f.read()[::-1])

'''

# 15 :
# Write a program to create a file using write (w) mode. 

'''
with open("text4.txt","w")as f:
    f.write("hi najad")

'''

# 16 :
# Write a program to write a single line into a file.

'''
with open("text4.txt","w")as f:
    f.write("hi najad")

'''

# 17 :
# Write a program to write multiple lines into a file.  

'''
with open("text4.txt","w")as f:
    f.write("hi najad")
    f.write("\nhi najad")
'''

# 18 :
# Write a program to overwrite existing file content. 

'''
with open("text4.txt","w")as f:
    f.write("hi najad")
    f.write("\nhi najad")

'''

# 19 :
# Write a program to write user input into a file.

'''
with open("text4.txt","w")as f:
    f.write("hi najad")
    f.write("\nhi najad")

'''

# 20 :
# Write a program to create a file and write numbers from 1 to 10. 

'''
with open("text4.txt","w")as f:
    for i in range(1,11):
        f.write(f"{i} \n")

'''

# 21 :
# Write a program to write a list of names into a file. 

'''
a=["najad","richu","aju","shabin"]
with open("text4.txt","w")as f:
    for i in a:
        f.write(f"{i} \n")

'''

# 22 :
# Write a program to write formatted text into a file.  

'''
name = "najad"
age = 25
score = 92.5
with open("text4.txt", "w") as f:
    f.write("Student Information\n")
    f.write("====================\n")
    f.write(f"Name : {name}\n")
    f.write(f"Age  : {age}\n")
    f.write(f"Score: {score:.2f}\n")

'''

# 23 :
# Write a program to write content and close the file manually.

'''
with open("text1.py","r") as f:
    print(f.read())
# print(f.read())                 #ValueError: I/O operation on closed file.

'''

# 24 :
# Write a program using with statement to write into a file. 

'''
with open("text4.txt", "w") as f:
    f.write("hi najad")

'''

# 25 : 
# Write a program to demonstrate that w mode overwrites existing data. 

# '''


# '''

# 26 :
# Write a program to write a paragraph into a file. 

# '''


# '''

# 27 :
# Write a program to write data and check file size.

# '''


# '''

# 28 :
# Write a program to write lowercase letters into a file.


# '''


# '''

# 29 :
# Write a program to write even numbers into a file.   

'''
with open("text4.txt","w")as f:
    for i in range(1,21):
        if i%2==0:
            f.write(f"{i} \n")

'''

# 30 : 

# '''


# '''

# 31 : 

# '''


# '''

# 32 : 

# '''


# '''

# 33 : 

# '''


# '''

# 34 : 

# '''


# '''

# 35 : 

# '''


# '''

# 36 : 

# '''


# '''

# 37 : 

# '''


# '''

# 38 : 

# '''


# '''

# 39 : 

# '''


# '''

# 40 : 

# '''


# '''

# 41 : 

# '''


# '''

# 42 : 

# '''


# '''

# 43 : 

# '''


# '''

# 44 : 

# '''


# '''

# 45 : 

# '''


# '''

# 46 : 

# '''


# '''

# 47 : 

# '''


# '''

# 48 : 

# '''


# '''

# 49 : 

# '''


# '''

# 50 : 

# '''


# '''

# 51 : 

# '''


# '''

# 52 : 

# '''


# '''

# 53 : 

# '''


# '''

# 54 : 

# '''


# '''
