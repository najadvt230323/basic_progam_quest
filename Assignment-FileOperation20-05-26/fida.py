def Add_record():
    with open('file.txt','a+') as file:
        data=file.read()
        names=[]
    while True:
        
             name=input("Enter Your Name : ")
             if name not in data:
            
                 names.append(name)
                 break
             else:
                 print("Please Enter Valid Name")

    phones=[]
    while True:
        phone=input("Enter Phone number (+91XXXXXXXXXX): ")
        if phone[:3]=='+91' and len(phone)==13:
            if phone not in data:
                phones.append(phone)
                n=int(input("Add more phone? 1-Yes / 0-No : "))
                if n==0:
                    break
            else:
                print("Phone number already exists")
        else:
            print("Please Enter Valid Number")

    emails=[]
    while True:
        email=input("Enter Your Email : ")
        if email.endswith("@gmail.com"):
            if  email not in data:
                emails.append(email)
                n=int(input("Add more email? 1-Yes / 0-No : "))
                if n==0:
                    break
            else:
                print("Email already exists")
        else:
            print("Please Enter Valid Email")
    with open('file.txt','a') as file:
        file.write('Name :'+name+' | '+'Phone :'+str(phones)+' | '+'Email :'+str(emails)+'\n')
        print("Added Record Successfully!")

def View_record():
    with open('file.txt','r') as file:
        data=file.readlines()
        for d in data:
            print(d)



def Edit_record():
    print('1.Edit Name\n2.Add Phone\n3.Add Email\n4.Edit Phone\n5.Edit Email\n0.Back')
    while True:
     op=int(input("Enter Which One You Wanna Edit : "))
    
     match op:
        case 1 :
            with open('file.txt','r') as file:
                data=file.readlines()
                n=input("Enter Your Current Name :")
                found=False
                for i in range(len(data)):
                    if n in data[i]:
                        s=input("Enter The New Name :")
                        data[i]=data[i].replace(n,s)
                        found=True
                        break
                if found==False:
                    print("Not Found")
                else:
                    with open('file.txt','w') as file:
                       file.writelines(data)
                       print("Name is Changed Successfully !")
            
        case 2:
             with open('file.txt','r') as file:
                 data=file.readlines()
             n=input("Enter Your Number : ")
             for i in range(len(data)):
                 if n in data[i]:
                    nmbr=input("Enter Your New Number : ")
                    if nmbr[:3]=='+91' and len(nmbr)==13:
                       parts=data[i].split('|')
                       phone=parts[1]
                       if nmbr not in phone:
                           phone=phone.replace("']","', '"+nmbr+"']")
                           parts[1]=phone
                           data[i]="|".join(parts)
                           print("Phone number Added")
                       else:
                           print("The Number is Already Exiting... ")
                           nmbr=input("Enter Your New Number : ")

             with open('file.txt','w') as file:
                    file.writelines(data) 

           
        case 3:
             with open('file.txt','r') as file:
                 data=file.readlines()
             n=input("Enter Your Name : ")
             eml=input("Enter Your New Email : ")
             if eml.endswith('@gmail.com') :
                 for i in range(len(data)):
                    if n in data[i]:
                      parts=data[i].split('|')
                      email=parts[2]
                      if eml not in email:
                         email=email.strip()
                         email=email.replace("']","', '"+eml+"']")
                         parts[2]=email
                         data[i]="|".join(parts)+'\n'
                         print("Email Added")
                 with open('file.txt','w') as file:
                    file.writelines(data)
             else:
                 print("Invalid Email")
        case 4:
             with open('file.txt','r') as file:
                 data=file.readlines()
                 p=input("Enter Phone Number You Want to Change :")
                 n=input("Enter the new number :")
                 for i in range(len(data)):
                     if p in data[i]:
                         if n[:3]=='+91' and len(n)==13:
                            data[i]=data[i].replace(p,n)
                            print("The Number is Updated!")
                         else:
                             print("Number Not in Correcct format")
                
                 with open('file.txt','w') as file:
                      file.writelines(data)

        case 5:
               with open('file.txt','r') as file:
                 data=file.readlines()
                 p=input("Enter Email You Want to Change :")
                 n=input("Enter the new Email :")
                 for i in range(len(data)):
                     if p in data[i]:
                         if n.endswith('@gmail.com'):
                            data[i]=data[i].replace(p,n)
                            print("The Email is Updated!")
                         else:
                             print("Email Not in Correct format")
                
                 with open('file.txt','w') as file:
                      file.writelines(data)
        case 0:
            print('Exiting')
            exit()
        case _:
            print("Invalid Choice..Plese enter Again")
            op=int(input("Enter Which One You Wanna Edit : "))

def delete_record():
    print("1.Delete Entire Record\n2.Delete Phone\n3.Delete Email\n4.Exit")
    
    while True:
       ch=int(input("Enter Your Choice :"))
       match ch:
        case 1:
             with open('file.txt','r') as file:
                data=file.readlines()
                n=input("Enter Name ,That You wanna Delete The All Details :")
                for i in range(len(data)):
                       if n in data[i]:
                          del(data[i])
                          print('Datas are Deleted ')
                          break
                else:
                   print("The name Not present in the List")
             with open('file.txt','w') as file:
                 file.writelines(data)
        case 2:
            with open('file.txt','r') as file:
                data=file.readlines()
                n=input("Enter Phone Number That You wanna Delete :")
                for i in range(len(data)):
                    if n in data[i]:
                        parts=data[i].split('|')
                        phone=eval(parts[1].replace(" Phone :",""))
                        phone.remove(n)
                        parts[1]='Phone :'+str(phone)
                        data[i]='|'.join(parts)
                        print("Phone Number is Deleted ! ")
                        break
                    else:
                        print("Number not present in Contact  List")
            with open('file.txt','w') as file:
                 file.writelines(data)
        case 3:
             with open('file.txt','r') as file:
                data=file.readlines()
                n=input("Enter Email That You wanna Delete :")
                for i in range(len(data)):
                    if n in data[i]:
                        parts=data[i].split('|')
                        email=eval(parts[2].replace(" Email :",""))
                        email.remove(n)
                        parts[2]='Email :'+str(email)
                        data[i]='|'.join(parts)+'\n'
                        print("Email is Deleted ! ")
                        break
                    else:
                        print("Email not present in Contact  List")
             with open('file.txt','w') as file:
                 file.writelines(data)
        case 4:
            print("Exiting...")
            break
        case _:
            print("Invalid choice..Please Enter Valid One..")
            ch=int(input("Enter Your Choice :"))
while True:
    print("Contact Management System")
    print('-------------------------')
    print('1. List all records\n2. Add Record\n3. Edit Record\n4. Delete Record\n5. Exit')
    ch = int(input("Enter Your Choice :"))
    match(ch):
        case 1:
            View_record()
        case 2:
            Add_record()
        case 3:
            Edit_record()
        case 4:
            delete_record()
        case 5:
            print("Thank you")
            exit()
        case _:
            print("Please Enter Valid Choice...")