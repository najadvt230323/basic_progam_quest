'''
Section 1: Basic File Operations
Open the CSV file using open() in read mode and print its contents.
Count the total number of lines in the file.
Read only the first 5 rows from the file.
Read the file line by line using readline().
Read all lines using readlines() and display them.
Print only the header row of the CSV file.
Check whether the file exists before opening it.
Close the file manually after reading.
Use with statement to open and read the file.
Print file size in bytes.
🔹 Section 2: Working with CSV Data
Read the CSV file using the csv module.
Print all rows as lists.
Print all rows as dictionaries using DictReader.
Extract and print all names from the file.
Extract and print all cities.
Count how many records are there in total.
Print records where Age > 30.
Print records where City = "Kochi".
Count how many people belong to each city.
Find the maximum age in the dataset.
🔹 Section 3: Writing to CSV
Create a new CSV file and write 5 records manually.
Copy contents from original file to a new file.
Append a new record to the existing CSV file.
Write only names and ages to a new file.
Save filtered data (Age > 25) into a new CSV.
Write a CSV file with custom delimiter (e.g., ;).
Write a file with uppercase names.
Remove duplicate rows (if any) and write to new file.
Write sorted data based on Age.
Write data in reverse order.
🔹 Section 4: Data Processing
Calculate average age of all records.
Find youngest person in the dataset.
Find oldest person in the dataset.
Count how many people are from each city.
Display names of people whose age is between 25–30.
Replace all city names "Delhi" with "New Delhi".
Convert all names to lowercase.
Add a new column "Status" (Adult/Young based on age).
Create a new CSV with only unique cities.
Merge two CSV files (create another sample file).
🔹 Section 5: Intermediate Tasks
Search for a record by name.
Update age of a specific person and rewrite file.
Delete a record based on ID.
Sort data by Name alphabetically.
Group data by City and display counts.
Find top 5 oldest people.
Find average age per city.
Validate data (check for missing values).
Handle exceptions while opening file.
Build a menu-driven program:
View records
Add record
Delete record
Search record


'''

# Section 1: Basic File Operations
# ----------------------------------------------------------------------
# Open the CSV file using open() in read mode and print its contents.
'''

with open("sample_data_50.csv","r") as f :
    print(f.read())

'''

# Count the total number of lines in the file.

'''

with open("sample_data_50.csv","r") as f :
    a=f.readlines()
    b=len(a)
    print(f"total number of lines in the file : {b}")

'''

# Read only the first 5 rows from the file.

'''

with open("sample_data_50.csv","r") as f :
    a=f.readlines()
    print(f.tell())
    f.seek(0)
    for i in range(5):
        print(f.readline())

'''

# Read the file line by line using readline().

'''

with open("sample_data_50.csv","r") as f :
    a=f.readlines()
    print(f.tell())
    f.seek(0)
    for i in range(5):
        print(f.readline())

'''

# Read all lines using readlines() and display them.

'''

with open("sample_data_50.csv","r") as f :
    a=f.readlines()
    b=len(a)
    print(f.tell())
    f.seek(0)
    for i in range(b):
        print(f.readline())

'''

# Print only the header row of the CSV file.

'''

with open("sample_data_50.csv","r") as f :
    a=f.readlines()
    b=len(a)
    print(f.tell())
    f.seek(0)
    for i in range(1):
        print(f"the header row of the CSV file : {f.readline()}")

'''
# Check whether the file exists before opening it.


# Close the file manually after reading.

'''
f=open("sample_data_50.csv")
print(f.read())
f.close()

'''

# Use with statement to open and read the file.

'''

with open("sample_data_50.csv","r") as f :
    print(f.read())

'''

# Print file size in bytes.

'''

with open("sample_data_50.csv","a") as f :
    print(f.tell())

'''

# 🔹 Section 2: Working with CSV Data
# Read the CSV file using the csv module.
# Print all rows as lists.
# Print all rows as dictionaries using DictReader.
# Extract and print all names from the file.
# Extract and print all cities.
# Count how many records are there in total.
# Print records where Age > 30.
# Print records where City = "Kochi".
# Count how many people belong to each city.
# Find the maximum age in the dataset.