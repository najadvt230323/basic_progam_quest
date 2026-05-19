class Bang:
    name = "canara bang"

    def __init__(self, a, b, d, c=0, ifse=1001):
        self.name = a
        self.acc_no = b
        self.ifse = ifse
        self.balns = c
        self.age=d

    def display(self):
        print(f"""
name     : {self.name}
ifsc     : {self.ifse}
acc no   : {self.acc_no}
balance  : {self.balns}
age      : {self.age}
""")

    def deposit(self, a):
        self.balns += a
        print(f"{a} rs deposited")
        print(f"balance : {self.balns}")

    def withdrawal(self, a):
        if self.balns >= a:
            self.balns -= a
            print(f"{a} rs withdrawn")
            print(f"balance : {self.balns}")
        else:
            print("Insufficient balance")


# ---------------- MAIN PROGRAM ----------------

a = "y"

# dictionary to store account objects
accounts = {}

acno = 2001

print("----------------- CANARA BANK -----------------")

while a.lower() == "y":

    c = int(input("""
1. New account create
2. Deposit
3. Withdrawal
4. Details

Enter your option : """))

    if c == 1:

        name = input("Enter the name : ")
        age = int(input("Enter the age : "))
        bal = int(input("Enter the bank balance : "))

        obj = Bang(name, acno, age, bal)

        # store object using name as key
        accounts[name] = obj

        obj.display()

        acno += 1

    elif c == 2:

        d = input("Enter your name : ")

        if d in accounts:

            e = int(input("Enter deposit amount : "))

            accounts[d].deposit(e)

        else:
            print("Account not found")

    elif c == 3:

        d = input("Enter your name : ")

        if d in accounts:

            e = int(input("Enter withdrawal amount : "))

            accounts[d].withdrawal(e)

        else:
            print("Account not found")

    elif c == 4:

        d = input("Enter your name : ")

        if d in accounts:

            accounts[d].display()

        else:
            print("Account not found")

    else:
        print("Invalid option")

    a = input('Continue ("y" or "n") : ')

    print(accounts)