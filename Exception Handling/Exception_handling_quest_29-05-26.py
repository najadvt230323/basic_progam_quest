# ========================================================================
#         PYTHON EXCEPTION HANDLING PRACTICAL QUESTIONS
#                  (Beginner to Intermediate)
# ========================================================================

# Topics Covered:
# - try
# - except
# - else
# - finally

# ========================================================================
# BEGINNER LEVEL
# ========================================================================

# 1. DIVISION PROGRAM
# -------------------
# Write a program to:
# - Take two numbers from the user
# - Divide them
# - Handle division by zero error
# - Print "Division Successful" using else block
# - Print "Program Ended" using finally block


# 2. INTEGER INPUT CHECKER
# ------------------------
# Write a program that:
# - Takes age from the user
# - Converts it into integer
# - Handles invalid input errors
# - Prints a success message using else
# - Prints "Thank You" using finally


# 3. LIST INDEX ACCESS
# --------------------
# Create a list with 5 fruits.
# Ask the user to enter an index.
# Display the fruit at that index.

# Handle:
# - Invalid index
# - Invalid input type

# Use finally block to print:
# "List operation completed"


# 4. SIMPLE CALCULATOR
# --------------------
# Create a calculator using:
# - Addition
# - Subtraction
# - Multiplication
# - Division

# Handle:
# - Invalid number input
# - Division by zero

# Use else and finally blocks properly.


# 5. FILE READING PROGRAM
# -----------------------
# Write a program to:
# - Open and read a text file
# - Handle file not found error
# - Print "File Read Successfully" in else
# - Close message in finally


# 6. PASSWORD LENGTH CHECK
# ------------------------
# Ask the user to enter a password.
# If the length is less than 5, display a normal message.

# Handle:
# - Any unexpected errors

# Use finally block to print:
# "Validation Completed"


# 7. NUMBER EVEN OR ODD
# ---------------------
# Write a program to:
# - Accept a number from the user
# - Check whether it is even or odd

# Handle invalid input using exception handling.

# Use:
# - else block for successful execution
# - finally block for completion message


# 8. MARK LIST ACCESS
# -------------------
# Create a list of student marks.

# Ask the user to:
# - Enter position number
# - Display the mark

# Handle:
# - IndexError
# - ValueError

# Use finally block.


# ========================================================================
# BEGINNER TO INTERMEDIATE LEVEL
# ========================================================================

# 9. MULTIPLE EXCEPTION HANDLING
# ------------------------------
# Write a program that:
# - Takes two numbers
# - Divides them
# - Stores result in a list index given by user

# Handle:
# - ZeroDivisionError
# - ValueError
# - IndexError

# Use else and finally.


# 10. ATM WITHDRAWAL SIMULATION
# -----------------------------
# Create a simple ATM program:
# - User enters withdrawal amount
# - Balance is 10000

# Handle:
# - Invalid input
# - Division-like logical errors if needed

# Use:
# - else for successful withdrawal
# - finally for transaction completion message


# 11. STUDENT MARK ANALYZER
# -------------------------
# Store marks in a dictionary.

# Ask user to enter student name.
# Display the mark.

# Handle:
# - KeyError
# - Invalid input

# Use finally block.


# 12. FILE WORD COUNTER
# ---------------------
# Write a program to:
# - Open a text file
# - Count total words

# Handle:
# - File not found error

# Use:
# - else for successful counting
# - finally for closing message


# 13. LOGIN SYSTEM
# ----------------
# Create a login system:
# - Username: admin
# - Password: 1234

# Handle:
# - Invalid input type
# - Any unexpected errors

# Use else block for successful login.
# Use finally block for:
# "Login Process Completed"


# 14. SHOPPING CART PROGRAM
# -------------------------
# Create a product list.

# Ask user to:
# - Select product using index
# - Enter quantity

# Handle:
# - Invalid index
# - Invalid quantity input

# Use else and finally.


# 15. TEMPERATURE CONVERTER
# -------------------------
# Create a program to convert:
# - Celsius to Fahrenheit

# Formula:
# F = (C * 9/5) + 32

# Handle:
# - Invalid numeric input

# Use else and finally.


# ========================================================================
# INTERMEDIATE LEVEL
# ========================================================================

# 16. NESTED TRY PROGRAM
# ----------------------
# Write a program with nested try blocks:
# - Outer block handles menu choice
# - Inner block handles division

# Use:
# - except
# - else
# - finally

# for both levels.


# 17. BANK ACCOUNT SIMULATION
# ---------------------------
# Create a bank program with:
# - Deposit
# - Withdraw
# - Balance Check

# Handle:
# - Invalid amount input
# - Invalid menu choice
# - Insufficient balance using normal conditions

# Use finally block after every transaction.


# 18. CSV FILE READER
# -------------------
# Read data from a CSV file.

# Handle:
# - File not found
# - Invalid formatting issues

# Use:
# - else block for successful reading
# - finally block for completion


# 19. ONLINE EXAM SYSTEM
# ----------------------
# Create a simple quiz system:
# - Ask 5 questions
# - Store score

# Handle:
# - Invalid option input
# - Unexpected errors

# Use finally block to display:
# "Exam Finished"


# 20. MENU DRIVEN CALCULATOR
# --------------------------
# Create a menu-driven calculator using loop.

# Menu:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Exit

# Handle:
# - Invalid menu choice
# - Invalid number input
# - Division by zero

# Use:
# - else block for successful operations
# - finally block after each operation


# 21. EMPLOYEE RECORD SEARCH
# --------------------------
# Store employee details in a dictionary.

# Ask user for employee ID.
# Display employee details.

# Handle:
# - KeyError
# - Invalid input

# Use finally block.


# 22. DYNAMIC LIST OPERATION
# --------------------------
# Create an empty list.

# Allow user to:
# - Insert element
# - Delete element using index
# - View elements

# Handle:
# - Invalid index
# - Invalid input

# Use finally block after every operation.


# 23. SIMPLE FILE WRITER
# ----------------------
# Write a program to:
# - Take text from user
# - Save it into a file

# Handle:
# - File-related exceptions
# - Invalid input

# Use:
# - else for successful writing
# - finally for completion message


# 24. ELECTRICITY BILL GENERATOR
# ------------------------------
# Create a bill generator:
# - Units entered by user
# - Calculate amount

# Handle:
# - Invalid numeric input

# Use:
# - else for successful calculation
# - finally for ending message


# 25. STUDENT RESULT PROCESSOR
# ----------------------------
# Take marks of 5 subjects from user.
# Calculate:
# - Total
# - Average

# Handle:
# - Invalid numeric inputs

# Use:
# - else for successful result generation
# - finally for result processing completion


# ========================================================================
# MINI CHALLENGE QUESTIONS
# ========================================================================

# 26. CREATE A SAFE CALCULATOR USING FUNCTIONS
# --------------------------------------------
# Create separate functions for:
# - Addition
# - Subtraction
# - Multiplication
# - Division

# Use exception handling in each function.


e=True
while e:
    try:
        a=int(input("enter 1st number : "))
        b=int(input("enter 2nd number : "))
        print('''
            
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
5 - exit
Enter your choice : 
''')
        c=input()
        if c=="1":
            print("Addition : ",a+b)
        elif c=="2":
            print("Subtraction : ",a-b)
        elif c=="3":
            print("Multiplication : ",a*b)
        elif c=="4":
            print("Division : ",a/b)
        elif c=="5":
            e=False
        else:
            print("enter a valid option")

    except ValueError as a:
        print(a)
        f=True
        while f:
            d=input("try again yes:\'y\' , no :\'n\' : ")
            if d.lower()=="y":
                e=True
                f=False
            elif d.lower()=="n":
                e=False
                f=False
            else :
                print("enter a valid option")
    except ZeroDivisionError as a:
        print(a)
        f=True
        while f:
            d=input("try again yes:\'y\' , no :\'n\' : ")
            if d.lower()=="y":
                e=True
                f=False
            elif d.lower()=="n":
                e=False
                f=False
            else :
                print("enter a valid option")
    else:
        f=True
        while f:
            d=input("try again yes:\'y\' , no :\'n\' : ")
            if d.lower()=="y":
                e=True
                f=False
            elif d.lower()=="n":
                e=False
                f=False
            else :
                print("enter a valid option")
    finally:
        print("\ntha code as must ren\n")



# 27. SAFE FILE COPY PROGRAM
# --------------------------
# Copy contents from one file to another.

# Handle:
# - Missing source file
# - Permission issues

# Use finally block.


# 28. USER DATA COLLECTION SYSTEM
# -------------------------------
# Collect:
# - Name
# - Age
# - Salary

# Handle invalid numeric inputs.
# Store valid data in dictionary.


# 29. MOVIE TICKET BOOKING
# ------------------------
# Create a ticket booking system.

# Handle:
# - Invalid seat number
# - Invalid input
# - Already booked seats using conditions


# 30. INVENTORY MANAGEMENT SYSTEM
# -------------------------------
# Create a simple inventory system using dictionary.

# Features:
# - Add product
# - Remove product
# - Search product

# Handle:
# - Key errors
# - Invalid input
# - Menu errors

# Use else and finally properly.


# ========================================================================
# END OF PRACTICAL QUESTIONS
# ========================================================================