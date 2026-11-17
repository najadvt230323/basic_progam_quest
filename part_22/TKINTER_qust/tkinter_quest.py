# from tkinter import *
# a=Tk()
# a.mainloop()

# ===================================
# from tkinter import *
# a=Tk()
# a.title("my first program")
# a.geometry("300x400")
# a.minsize(200,300)
# a.maxsize(400,500)

# b=Label(text="hai")
# b.pack()
# b=Label(text="hai najad")
# b.pack()
# b=Label(text="hai quest" \
# " hi aju")
# b.pack()
# b=Label(text='''hai quest
#  hi aju ''')
# b.pack()

# c=Label(text="najad")
# b.grid()

# a.mainloop()
# =================================================

# from tkinter import *
# a=Tk()
# a.title("my first program")
# a.geometry("300x400")
# a.minsize(200,300)
# a.maxsize(400,500)

# c=Label(text="najad")
# c.grid(row=0,column=0)

# c=Label(text="hi")
# c.grid(row=1,column=1)

# c=Label(text="najad")
# c.grid(row=2,column=2)

# c=Label(text="hi")
# c.grid(row=3,column=3)

# c=Label(text="najad")
# c.grid(row=4,column=4)

# c=Label(text="najad")
# c.grid(row=18,column=18)

# c=Label(text="hi")
# c.grid(row=8,column=8)

# c=Label(text="najad hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
# c.grid(row=4,column=0)

# a.mainloop()
# ================================================================================

# def onclick():
#     v=box1.get()
#     m=Label()
#     m.grid(row=4,column=1)
#     m.config(text=v)

#     m=Label()
#     m.grid(row=5,column=1)
#     m.config(text=v[::-1])



# from tkinter import *
# a=Tk()
# a.title("my first program")
# a.geometry("300x400")
# a.minsize(200,300)
# a.maxsize(400,500)

# a=Label(text="enter your name : ")
# a.grid(row=0,column=0)
# box1=Entry()
# box1.grid(row=0,column=1)

# a=Label(text="enter your age : ")
# a.grid(row=1,column=0)
# box2=Entry()
# box2.grid(row=1,column=1)

# a=Label(text="enter your place : ")
# a.grid(row=2,column=0)
# box3=Entry()
# box3.grid(row=2,column=1)

# btn=Button(text="register" , command=onclick)
# btn.grid(row=3 , column=1)

# a.mainloop()
# =====================================================================

# def onclick():
#     c=box1.get()
#     d=box2.get()

#     if c.isdigit() and d.isdigit() :
#         m=Label()
#         m.grid(row=4,column=1)
#         m.config(text=(f"add={int(c)+int(d)}"))

#         m=Label()
#         m.grid(row=5,column=1)
#         m.config(text=(f"sub={int(c)-int(d)}"))

#         m=Label()
#         m.grid(row=6,column=1)
#         m.config(text=(f"mult={int(c)*int(d)}"))
#     else :
#         m=Label()
#         m.grid(row=4,column=1)
#         m.config(text="enter 2 intger number ")


# from tkinter import *
# a=Tk()
# a.title("my first program")
# a.geometry("300x400")
# a.minsize(200,300)
# a.maxsize(400,500)

# a=Label(text="enter 1st intger number : ")
# a.grid(row=0,column=0)
# box1=Entry()
# box1.grid(row=0,column=1)

# b=Label(text="enter 2nd intger number : ")
# b.grid(row=1,column=0)
# box2=Entry()
# box2.grid(row=1,column=1)

# btn=Button(text="math" , command=onclick)
# btn.grid(row=2 , column=1)

# # a=

# a.mainloop()

# ==============================================================


# def onclick1():
#     c=box1.get()
#     d=box2.get()

#     if c.isdigit() and d.isdigit() :
#         # m=Label()
#         # m.grid(row=2,column=2)
#         # m.config(text=int(c)+int(d))

#         box=Entry()
#         box.grid(row=2 , column=2)
#         box.insert(0,int(c)+int(d))



#     else :
#         m=Label()
#         m.grid(row=2,column=1)
#         m.config(text="enter 2 intger number ")

# def onclick2():
#     c=box1.get()
#     d=box2.get()


#     if c.isdigit() and d.isdigit() :
#         m=Label()
#         m.grid(row=3,column=2)
#         m.config(text=int(c)-int(d))

#     else :
#         m=Label()
#         m.grid(row=2,column=1)
#         m.config(text="enter 2 intger number ")

# def onclick3():
#     c=box1.get()
#     d=box2.get()

#     if c.isdigit() and d.isdigit() :
#         m=Label()
#         m.grid(row=4,column=2)
#         m.config(text=int(c)*int(d))

#     else :
#         m=Label()
#         m.grid(row=2,column=1)
#         m.config(text="enter 2 intger number ")

# def onclick4():
#     c=box1.get()
#     d=box2.get()

#     if c.isdigit() and d.isdigit() :
#         m=Label()
#         m.grid(row=5,column=2)
#         m.config(text=int(c)/int(d))

#     else :
#         m=Label()
#         m.grid(row=6,column=1)
#         m.config(text="enter 2 intger number ")

# from tkinter import *
# a=Tk()
# a.title("my first program")
# a.geometry("300x400")
# a.minsize(200,300)
# a.maxsize(400,500)

# a=Label(text="enter 1st intger number : ")
# a.grid(row=0,column=0)
# box1=Entry()
# box1.grid(row=0,column=1)

# b=Label(text="enter 2nd intger number : ")
# b.grid(row=1,column=0)
# box2=Entry()
# box2.grid(row=1,column=1)

# btn=Button(text="add" , command=onclick1)
# btn.grid(row=2 , column=1)

# btn=Button(text="sub" , command=onclick2)
# btn.grid(row=3 , column=1)

# btn=Button(text="mult" , command=onclick3)
# btn.grid(row=4 , column=1)

# btn=Button(text="div" , command=onclick4)
# btn.grid(row=5 , column=1)

# # a=

# a.mainloop()

# ===================================================================
'''
def onclick1():
    f=box1.get()

    try:
        f=float(f)
        c=(f-32)*5/9

        box=Entry()
        box.grid(row=0 , column=3)
        box.insert(0,c)
    except:
        box=Entry()
        box.grid(row=0 , column=3)
        box.insert(0,"enter a number ")

        # m=Label()
        # m.grid(row=0,column=3)
        # m.config(text="enter a number ") 

    # if f.isdecimal():
    #     c=(int(f)-32)*5/9

    #     box=Entry()
    #     box.grid(row=0 , column=3)
    #     box.insert(0,c)
    # else :
    #     m=Label()
    #     m.grid(row=0,column=3)
    #     m.config(text="enter intger number ")

def onclick2():
    c=box2.get()
    try:
        c=float(c)
        f=(c*9/5)+32

        box=Entry()
        box.grid(row=1 , column=3)
        box.insert(0,f)
    except :
        box=Entry()
        box.grid(row=1 , column=3)
        box.insert(0,"enter a number ")


from tkinter import *
a=Tk()
a.title("convert to celcius")
a.geometry("500x500")
a.minsize(500,500)
a.maxsize(500,500)

b=Label(text="enter farenheit :")
b.grid(row=0,column=0)
box1=Entry()
box1.grid(row=0,column=1)
btn=Button(text="convert to celcius" , command=onclick1)
btn.grid(row=0,column=2)

b=Label(text="enter celcius :")
b.grid(row=1,column=0)
box2=Entry()
box2.grid(row=1,column=1)
btn=Button(text="convert to farenheit" , command=onclick2)
btn.grid(row=1,column=2)

# z=  
a.mainloop()

'''
# ===============================================================================
'''
def click() :
    messagebox.showinfo("infomation" , "are u sure")
    messagebox.showwarning("warning" , "this is a warning")
    messagebox.showerror("error" , " an error")
    messagebox.askokcancel()
    messagebox.askquestion()
    messagebox.askretrycancel()
    messagebox.askyesno()
    messagebox.askyesnocancel()


from tkinter import *
from tkinter import messagebox

a=Tk()
a.geometry("600x300")
a.maxsize(600,300)
a.minsize(600,300)

btn=Button(text="click" , command=click)
btn.grid()

a.mainloop()
'''
# ============================================================================

'''
def click() :
    btn=c.get()

    Text=Label()
    Text.grid(row=0 ,column=2)
    Text.config(text=btn)

    box=Entry()
    box.grid(row=0 , column=3)
    box.insert(0,btn)

from tkinter import *
from tkinter.ttk import *

a=Tk()
a.geometry("600x300")
a.maxsize(600,300)
a.minsize(600,300)

c=Combobox()
c.grid(row=0 , column=0)
c["value"] = ["select" , "uk" , "usa" ,"india" , "russia"]
c.current(0)

b=Button(text="click" , command=click)
b.grid(row=0 ,column=1)

a.mainloop()
'''
# ==============================================================================
'''
def show():
    s=[]
    for i,j in enumerate(c) :
        if j.get()==1 :
            s.append(lag[i])
    print(s)   

from tkinter import *

a=Tk()
a.title("check button")
a.geometry("600x300")
a.maxsize(600,300)
a.minsize(600,300)

b=Label(text="languages")
b.grid()

lag=["python","java","c","javascript","ruby","c++"]
c=[]

for i in lag :
    var=IntVar()
    chk=Checkbutton(text=i , variable=var)
    chk.grid(sticky=W)
    c.append(var)

btn=Button(text="show select" ,command=show)
btn.grid(pady=10)

a.mainloop()
# '''
# ===========================================================================================
'''

def addi():
    d=b.get()
    b.delete(0,END)
    b.insert(0,int(d)+1)

def subt():
    d=b.get()
    b.delete(0,END)
    b.insert(0,int(d)-1)

from tkinter import *
a=Tk()
a.title("check button")
a.geometry("600x300")
a.maxsize(600,300)
a.minsize(600,300)

b=Entry(a , font=("times new roman" , 20) , justify="right" ,  bg="black" , fg="white" , relief="sunken" , bd=10)
b.grid(row=0 , column=1 , pady=15 )
b.insert(0,0)

btn1=Button(text="+" , command=addi)
btn1.grid(row=1 , column=0 ,pady=10)

btn1=Button(text="-" , command=subt)
btn1.grid(row=1 , column=2 ,pady=10)

a.mainloop()
'''
# ================================================================================================







