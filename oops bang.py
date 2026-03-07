class bang:
    def details(self,name,age,balanc):
        self.n=name
        self.a=age
        self.b=balanc
    def deposit(self,deposit):
        self.b=self.b+deposit
        return self.b
    def withdraw(self,wedroval):
        self.b=self.b-wedroval
        return self.b
    def displya(self):
        print("name : ",self.n)
        print("age : ",self.a)
        print("balanc : ",self.b)


name=input("enter the name : ")
age=int(input("enter the age : "))
bal=int(input("enter the bang balans : "))

ban=bang()
ban.details(name,age,bal)
ban.displya()

a=input("do you want to withdraw or deposit mony (y/n) : ")
while a=="y":
    b=int(input("1.withdraw mony or 2.deposit mony (1/2) : "))
    if b==1:
        c=int(input("how much monydo you need to withdraw? : "))
        if c<=bal:
            ban.withdraw(c)
            print("your withdrawal is successfully complrte.")
        else:
            print("you don't have this amount in your account.")
    elif b==2:
        d=int(input("how much monydo you need to deposit?:"))
        ban.deposit(d)
    else:
        print("wrong choice")
    ban.displya()

    a=input("do you want to agin withdraw or deposit mony (y/n) : ")


  
 
