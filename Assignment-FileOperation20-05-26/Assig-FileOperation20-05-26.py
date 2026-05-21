with open("assig.txt file","a+")as new:
    pass

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
    if op.isdigit() :
        op=int(op)

        if op == 1 :
            print("5656521")
            with open("assig.txt file")as new:
                read_file=new.readlines()
                print(read_file)
        elif op == 2 :
            print("<---------------2. Add Record-------------->")

            # Enter Phone name
            # =================
            '''
            name=input("Enter name: ")

            '''
            # Enter Phone number (+91XXXXXXXXXX)
            # =====================================
            '''
            phon=[]
            b=input("Enter Phone number (+91XXXXXXXXXX) : ")
            phon.append(b)
            c=input("Add more phone? 1-Yes / 0-No: 0")
            if c.isdigit() :
                c=int(c)
                if c==1:
                    b=input("Enter Phone number (+91XXXXXXXXXX) : ")
                    phon.append(b)
                elif c==2:
                    print()
                else:
                    print("Enter validen opstion")
            else:
                print("Enter validen opstion")
                
            '''

            # Enter email id
            # ===============
            email=[]
            b=input("Enter email id : ")
            if b.endswith("@gmail.com") and :
                email.append(b)
            else:
                print("Invalid email id.")

            c=input("Add more email? 1-Yes / 0-No: 0")
            if c.isdigit() :
                c=int(c)
                if c==1:
                    b=input("Enter email id : ")
                    email.append(b)
                elif c==2:
                    print()
                else:
                    print("Enter validen opstion")
            else:
                print("Enter validen opstion")

            print("Record added successfully 👍")

        elif op == 3 :
            pass

        elif op == 3 :
            pass

        elif op == 4 :
            pass

        elif op == 5 :
            print("Exiting... Thank You 😊")
            a=False
    
        else :
            print("Enter validen opstion")
    
    else:
        print("Enter validen opstion")










