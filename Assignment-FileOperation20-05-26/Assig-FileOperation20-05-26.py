
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
        for i in read_file:
            # print(f"{i[:-1]}")
            # result.update(ast.literal_eval(item))           
            a1.update(ast.literal_eval(i))
        # print(a1)
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


        elif op == 4 :
            pass

        elif op == 5 :
            print("Exiting... Thank You 😊")
            a=False
    
        else :
            print("Enter validen opstion")
    
    else:
        print("Enter validen opstion")










