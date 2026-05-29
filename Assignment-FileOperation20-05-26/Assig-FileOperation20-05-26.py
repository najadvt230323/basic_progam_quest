
# 1. Main Menu

a=True
while a :
    print('''
<---------------- Menu ------------------->
1. List all records
2. Add Record
3. Edit Record
4. Delete Record
5. Exit
          ''')

    op=input("Enter your opstion : ")
    print()
    # file reding
    # ===============
    a1={}
    import ast
    with open("assig.txt")as new:
        read_file=new.readlines()
        try :
            for i in read_file:
                # print(f"{i[:-1]}")
                # result.update(ast.literal_eval(item))           
                a1.update(ast.literal_eval(i))
            # print(a1)
        except :
            print("file was empty.")
    if op.isdigit() :
        op=int(op)

        if op == 1 :
            print("<---------------1. List all records-------------->")

        # 1. List all records
        # ======================
            for k,v in a1.items():
                print(f'''
name : {k}  
phon no : {v[0]}  
email : {v[1]}
''' )

        elif op == 2 :
            print("<---------------2. Add Record-------------->")
            # Enter name
            # =================
            # '''
            h=True
            while h:
                name=input("Enter name: ")
                if name.isalpha() and len(name)<60 and len(name)>=4:
                    h=False
                else:
                    print("Enter valide name (\"not use spce\" , \"not use num\").")


            # '''
            # Enter Phone number (+91XXXXXXXXXX)
            # =====================================
            # '''
            phon=[]
            f=True
            while f:
                b=input("Enter Phone number (+91XXXXXXXXXX) : ")
                if len(b)==13 or len(b)==10 and b[1:].isdecimal() :
                    if b.startswith("+91") and len(b)==13 :
                        l=0
                        for k,v in a1.items():
                            for i in range(len(v[0])):
                                if b==v[0][i]:
                                    l=1
                        if l==1:
                            print("phon number aready existed.")
                        else:                                   
                            phon.append(b)
                            g=True
                            while g:
                                c=input("Add more phone? 1-Yes / 0-No: ")
                                if c.isdigit() :
                                    c=int(c)
                                    if c==1:
                                        b=input("Enter Phone number (+91XXXXXXXXXX) : ")
                                        if len(b)==13 or len(b)==10 and b[1:].isdecimal() :
                                            if b.startswith("+91") and len(b)==13 :
                                                l=0
                                                for k,v in a1.items():
                                                    for i in range(len(v[0])):
                                                        if b==v[0][i]:
                                                            l=1
                                                if l==1:
                                                    print("phon number aready existed.")
                                                else:                                   
                                                    phon.append(b)
                                                    g=False
                                                    f=False
                                            else:
                                                print("phon number start with \"+91\"")
                                        else:
                                            print("Enter validen phon number.") 
                                    elif c==0:
                                        print()
                                        g=False
                                        f=False
                                    else:
                                        print("Enter validen opstion")
                                else:
                                    print("Enter validen opstion")
                    else:
                        print("phon number start with \"+91\"")
                else:
                    print("Enter validen phon number.\n")  

            # Enter email id
            # ===============
            email=[]
            d=True
            while d:
                b=input("Enter email id : ")
                if b.endswith("@gmail.com") and len(b)>12 and b.isascii() and len(b)<50:
                    l=0
                    for k,v in a1.items():
                        for i in range(len(v[1])):
                            if b==v[1][i]:
                                l=1
                    if l==1:
                        print("This email aready existed.")
                    else:
                        email.append(b)
                        e=True
                        while e :
                            c=input("Add more email? 1-Yes / 0-No: ")
                            if c.isdigit():
                                c=int(c)
                                if c==1:
                                    b=input("Enter email id : ")
                                    if b.endswith("@gmail.com") and len(b)>13 and b.isascii() and len(b)<50:
                                        l=0
                                        for k,v in a1.items():
                                            for i in range(len(v[1])):
                                                if b==v[1][i]:
                                                    l=1
                                        if l==1:
                                            print("This email aready existed.")
                                        else:
                                            email.append(b)
                                            e=False
                                            d=False
                                    else:
                                        print("Enter validen email")
                                elif c==0:
                                    print()
                                    d=False
                                    e=False
                                else:
                                    print("Enter validen opstion")
                            else:
                                print("Enter validen opstion")                       
                else:
                    print("Enter validen email")
            # '''
            file_name={}
            file_name.update({name:[phon,email]})
            for k,v in file_name.items():
                print(f'''
name : {k}  
phon no : {v[0]}  
email : {v[1]}
''' )
            with open("assig.txt","a+") as new :
                # print(new.read())
                new.write(f"{str(file_name)}\n")
            

            print("\nRecord added successfully 👍")
        
            # '''
        elif op == 3 :
            print("<---------------3. Edit Record-------------->")
            h=True
            f=False
            while h:
                name1=input("Enter name: ")
                for k,v in a1.items():
                    o=0
                    if k==name1:
                        h=False
                        f=True
                        o=1
                if o==1:
                    pass           
                else:
                    print("Name not in record,Enter valide name.")

            while f:
                b=input("Enter Phone number (+91XXXXXXXXXX) : ")
                if len(b)==13 or len(b)==10 and b[1:].isdecimal() :
                    if b.startswith("+91") and len(b)==13 :
                        f=False
                        for k,v in a1.items():
                            o=0
                            if k==name1:
                                o=1
                                for i in range(len(v[0])):
                                    n=0
                                    if v[0][i]==b:
                                        n=1
                                        print(f'''
name : {k}  
phon no : {v[0]}  
email : {v[1]}
''')
                                        print("Which recoted do you need to edit?")
                                        p=True
                                        while p :
                                            m=input("1. phon number 2. email id \nEnter your option : ")
                                             #1. phon number edit
                                            #  ======================
                                            if m=="1" :
                                                q=True
                                                if len(v[0])==1:
                                                    while q :
                                                        r=input("1. Add phon number 2. Edit phon number \nEnter your option : ")
                                                        if r=="1":
                                                            u=True
                                                            while u :
                                                                s=input("Adding phon number \nEnter phone numer (+91XXXXXXXXXX) : ")
                                                                if len(s)==13 or len(s)==10 and s[1:].isdecimal() :
                                                                    if s.startswith("+91") and len(s)==13 :
                                                                        l=0
                                                                        for w,x in a1.items():
                                                                            for i in range(len(x[0])):
                                                                                if s==x[0][i]:
                                                                                    l=1
                                                                        if l==1:
                                                                            print("Phon number aready existed.")
                                                                        else:                                   
                                                                            v[0].append(s)
                                                                            # print(v[0])
                                                                            with open("assig.txt","w") as new :
                                                                                for k,v in a1.items():
                                                                        # {'najadvt': [['+919562020209'], ['najadvt@gmail.com']]}
                                                                                    t="{"+f"\'{k}\': {v}"+"}"+"\n"
                                                                                    new.write(t)
                                                                            print("Adding phon number successfully 👍")
                                                                            p=False
                                                                            q=False
                                                                            u=False
                                                                    else:
                                                                        print("Phon number start with \"+91\"")
                                                                else:
                                                                    print("Enter validen phon number.\n")
                                                        elif r=="2":
                                                            u=True
                                                            while u :
                                                                s=input("Editig phon number \nEnter phone numer (+91XXXXXXXXXX) : ")
                                                                if len(s)==13 or len(s)==10 and s[1:].isdecimal() :
                                                                    if s.startswith("+91") and len(s)==13 :
                                                                        l=0
                                                                        for w,x in a1.items():
                                                                            for i in range(len(x[0])):
                                                                                if s==x[0][i]:
                                                                                    l=1
                                                                        if l==1:
                                                                            print("phon number aready existed.")
                                                                        else:                                   
                                                                            v[0][0]=s
                                                                            with open("assig.txt","w") as new :
                                                                                for k,v in a1.items():
                                                                                    t="{"+f"\'{k}\': {v}"+"}"+"\n"
                                                                                    new.write(t)
                                                                            print("Editing phon number successfully 👍")
                                                                            p=False
                                                                            q=False
                                                                            u=False
                                                                    else:
                                                                        print("phon number start with \"+91\"")
                                                                else:
                                                                    print("Enter validen phon number.\n")
                                                        else:
                                                            print("Enter validen opstion.")
                                                elif len(v[0])==2:
                                                    q=True
                                                    while q:
                                                        r=input("1. Deleat phon no 2.Edit phon number \nEnter your option : ")
                                                        if r=='1':
                                                            s=input(f"1 . {v[0][0]} 2 . {v[0][1]}\nWhich number should be deleted? :  ")
                                                            if s=='1':
                                                                del v[0][0]
                                                                with open("assig.txt","w") as new :
                                                                    for k,v in a1.items():
                                                                        t="{"+f"\'{k}\': {v}"+"}"+"\n"
                                                                        new.write(t)
                                                                print("delete phon number successfully 👍")
                                                                p=False
                                                                q=False
                                                            elif s=='2':
                                                                del v[0][1]
                                                                with open("assig.txt","w") as new :
                                                                    for k,v in a1.items():
                                                                        t="{"+f"\'{k}\': {v}"+"}"+"\n"
                                                                        new.write(t)
                                                                print("delete phon number successfully 👍")
                                                                p=False
                                                                q=False
                                                            else:
                                                                print("Enter validen opstion.")
                                                        elif r=='2':
                                                            u=True
                                                            while u:
                                                                s=input(f"1 . {v[0][0]} 2 . {v[0][1]}\nWhich number should be Edit? :  ")
                                                                if s=='1':
                                                                    b=input("Enter Phone number (+91XXXXXXXXXX) : ")
                                                                    if len(b)==13 or len(b)==10 and b[1:].isdecimal() :
                                                                        if b.startswith("+91") and len(b)==13 :
                                                                            l=0
                                                                            for w,x in a1.items():
                                                                                for i in range(len(x[0])):
                                                                                    if b==x[0][i]:
                                                                                        l=1
                                                                            if l==1:
                                                                                print("phon number aready existed.")
                                                                            else: 
                                                                                v[0][0]=b
                                                                                with open("assig.txt","w") as new :
                                                                                    for k,v in a1.items():
                                                                                        t="{"+f"\'{k}\': {v}"+"}"+"\n"
                                                                                        new.write(t)
                                                                                p=False
                                                                                q=False
                                                                                u=False
                                                                                print("Edit phon number successfully 👍")
                                                                        else:
                                                                            print("phon number start with \"+91\"")
                                                                    else:
                                                                        print("Enter validen phon number.\n")
                                                                    
                                                                elif s=='2':
                                                                    b=input("Enter Phone number (+91XXXXXXXXXX) : ")
                                                                    if len(b)==13 or len(b)==10 and b[1:].isdecimal() :
                                                                        if b.startswith("+91") and len(b)==13 :
                                                                            l=0
                                                                            for w,x in a1.items():
                                                                                for i in range(len(x[0])):
                                                                                    if b==x[0][i]:
                                                                                        l=1
                                                                            if l==1:
                                                                                print("phon number aready existed.")
                                                                            else: 
                                                                                v[0][1]=b
                                                                                with open("assig.txt","w") as new :
                                                                                    for k,v in a1.items():
                                                                                        t="{"+f"\'{k}\': {v}"+"}"+"\n"
                                                                                        new.write(t)
                                                                                p=False
                                                                                q=False
                                                                                u=False
                                                                                print("Edit phon number successfully 👍")
                                                                        else:
                                                                            print("phon number start with \"+91\"")
                                                                    else:
                                                                        print("Enter validen phon number.\n")
                                                        else:
                                                            print("Enter validen opstion.")                                                                 
                                            elif m=="2":
                                            #2. email edit
                                            #  ======================
                                                q=True
                                                if len(v[1])==1:
                                                    while q :
                                                        r=input("1. Add email id 2. Edit email id \nEnter your option : ")
                                                        if r=="1":
                                                            u=True
                                                            while u :
                                                                s=input("Enter email id : ")
                                                                if s.endswith("@gmail.com") and len(s)>12 and s.isascii() and len(s)<50:
                                                                    l=0
                                                                    for w,x in a1.items():
                                                                        for i in range(len(x[1])):
                                                                            if s==x[1][i]:
                                                                                l=1
                                                                    if l==1:
                                                                        print("Email id aready existed.")
                                                                    else:                                   
                                                                        v[1].append(s)
                                                                        with open("assig.txt","w") as new :
                                                                            for k,v in a1.items():
                                                                                t="{"+f"\'{k}\': {v}"+"}"+"\n"
                                                                                new.write(t)
                                                                        print("Adding email id successfully 👍")
                                                                        p=False
                                                                        q=False
                                                                        u=False
                                                                
                                                                else:
                                                                    print("Enter validen email id.\n")
                                                        elif r=="2":
                                                            u=True
                                                            while u :
                                                                s=input("Editig email id \nEnter new email id :")
                                                                if s.endswith("@gmail.com") and len(s)>12 and s.isascii() and len(s)<50:
                                                                    l=0
                                                                    for w,x in a1.items():
                                                                        for i in range(len(x[1])):
                                                                            if s==x[1][i]:
                                                                                l=1
                                                                    if l==1:
                                                                        print("Email id aready existed.")
                                                                    else:                                   
                                                                        v[1][0]=s
                                                                        with open("assig.txt","w") as new :
                                                                            for k,v in a1.items():
                                                                                t="{"+f"\'{k}\': {v}"+"}"+"\n"
                                                                                new.write(t)
                                                                        print("Editing phon number successfully 👍")
                                                                        p=False
                                                                        q=False
                                                                        u=False
                                                                else:
                                                                    print("Enter validen email id.\n")
                                                        else:
                                                            print("Enter validen opstion.")
                                                elif len(v[0])==2:
                                                    q=True
                                                    while q:
                                                        r=input("1. Deleat email id 2.Edit email id \nEnter your option : ")
                                                        if r=='1':
                                                            s=input(f"1 . {v[1][0]} 2 . {v[1][1]}\nWhich email should be deleted? :  ")
                                                            if s=='1':
                                                                del v[1][0]
                                                                with open("assig.txt","w") as new :
                                                                    for k,v in a1.items():
                                                                        t="{"+f"\'{k}\': {v}"+"}"+"\n"
                                                                        new.write(t)
                                                                print("delete email id successfully 👍")
                                                                p=False
                                                                q=False
                                                            elif s=='2':
                                                                del v[1][1]
                                                                with open("assig.txt","w") as new :
                                                                    for k,v in a1.items():
                                                                        t="{"+f"\'{k}\': {v}"+"}"+"\n"
                                                                        new.write(t)
                                                                print("delete email successfully 👍")
                                                                p=False
                                                                q=False
                                                            else:
                                                                print("Enter validen opstion.")
                                                        elif r=='2':
                                                            u=True
                                                            while u:
                                                                s=input(f"1 . {v[1][0]} 2 . {v[1][1]}\nWhich number should be Edit? :  ")
                                                                if s=='1':
                                                                    s=input("Enter new email id : ")
                                                                    if s.endswith("@gmail.com") and len(s)>12 and s.isascii() and len(s)<50:
                                                                        l=0
                                                                        for w,x in a1.items():
                                                                            for i in range(len(x[1])):
                                                                                if s==x[1][i]:
                                                                                    l=1
                                                                        if l==1:
                                                                            print("email id aready existed.")
                                                                        else: 
                                                                            v[1][0]=s
                                                                            with open("assig.txt","w") as new :
                                                                                for k,v in a1.items():
                                                                                    t="{"+f"\'{k}\': {v}"+"}"+"\n"
                                                                                    new.write(t)
                                                                            p=False
                                                                            q=False
                                                                            u=False
                                                                            print("Edit email id successfully 👍")             
                                                                    else:
                                                                        print("Enter validen email.\n")
                                                                    
                                                                elif s=='2':
                                                                    s=input("Enter new email id : ")
                                                                    if s.endswith("@gmail.com") and len(s)>12 and s.isascii() and len(s)<50:
                                                                        l=0
                                                                        for w,x in a1.items():
                                                                            for i in range(len(x[1])):
                                                                                if s==x[1][i]:
                                                                                    l=1
                                                                        if l==1:
                                                                            print("email id aready existed.")
                                                                        else: 
                                                                            v[1][1]=s
                                                                            with open("assig.txt","w") as new :
                                                                                for k,v in a1.items():
                                                                                    t="{"+f"\'{k}\': {v}"+"}"+"\n"
                                                                                    new.write(t)
                                                                            p=False
                                                                            q=False
                                                                            u=False
                                                                            print("Edit email id successfully 👍")             
                                                                    else:
                                                                        print("Enter validen email.\n")
                                                        else:
                                                            print("Enter validen opstion.")
                                            else :
                                                print("Enter validen opstion.")

                                if n==0:
                                    o=0
                                    print("Enterd phone number not in file.")
                        if o==0:
                            print("Enterd email id not in file.")


                    else:
                        print("phon number start with \"+91\"")
                else:
                    print("Enter validen phon number.\n")  

            # phon1=input("Enter Phone number (+91XXXXXXXXXX) : ")


        elif op == 4 :
            print("<---------------4. Delete Record-------------->")
            h=True
            f=False
            while h:
                name1=input("Enter name: ")
                for k,v in a1.items():
                    o=0
                    if k==name1:
                        h=False
                        f=True
                        o=1
                if o==1:
                    pass           
                else:
                    print("Name not in record,Enter valide name.")

            while f:
                b=input("Enter Phone number (+91XXXXXXXXXX) : ")
                if len(b)==13 or len(b)==10 and b[1:].isdecimal() :
                    if b.startswith("+91") and len(b)==13 :
                        f=False
                        for k,v in a1.items():
                            o=0
                            if k==name1:
                                o=1
                                for i in range(len(v[0])):
                                    n=0
                                    if v[0][i]==b:
                                        n=1
                                        print(f'''
name : {k}  
phon no : {v[0]}  
email : {v[1]}
''')
                                        print("Delete Record?")
                                        p=True
                                        while p :
                                            m=input("1. yes 2. No \nEnter your option : ")
                                            if m=='1':
                                                print("delete record successfully 👍")
                                                f=False
                                                p=False
                                            elif m=="2":
                                                print("Record as not delete.")
                                                f=False
                                                p=False
                                            else:
                                                print("Enter validen opstion")
                        if m=='1':
                            del a1[name1]
                            with open("assig.txt","w") as new :
                                for k,v in a1.items():
                                    t="{"+f"\'{k}\': {v}"+"}"+"\n"  
                                    new.write(t)                                           
        elif op == 5 :
            print("Exiting... Thank You 😊")
            a=False
    
        else :
            print("Enter validen opstion")
    
    else:
        print("Enter validen opstion")
