import json
import os

FILE_NAME = "contacts.json"


# =========================
# File Handling
# =========================

def load_records():
    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except:
            return {}


def save_records(records):
    with open(FILE_NAME, "w") as file:
        json.dump(records, file, indent=4)


# =========================
# Validations
# =========================

def validate_name(name):
    return (
        name.replace(" ", "").isalpha()
        and 3 <= len(name) <= 50
    )


def validate_phone(phone):
    return (
        phone.startswith("+91")
        and len(phone) == 13
        and phone[3:].isdigit()
    )


def validate_email(email):
    return (
        email.endswith("@gmail.com")
        and email.isascii()
        and len(email) < 50
    )


# =========================
# Duplicate Checking
# =========================

def phone_exists(records, phone):
    for data in records.values():
        if phone in data["phones"]:
            return True
    return False


def email_exists(records, email):
    for data in records.values():
        if email in data["emails"]:
            return True
    return False


# =========================
# List Records
# =========================

def list_records(records):
    if not records:
        print("\nNo records found.\n")
        return

    print("\n<----- Contact Records ----->")

    for name, data in records.items():
        print(f"""
Name   : {name}
Phones : {', '.join(data['phones'])}
Emails : {', '.join(data['emails'])}
""")


# =========================
# Add Record
# =========================

def add_record(records):

    while True:
        name = input("Enter Name: ").strip()

        if validate_name(name):
            if name not in records:
                break
            print("Name already exists.")
        else:
            print("Invalid name.")

    # Phone Numbers
    phones = []

    while True:
        phone = input("Enter Phone (+91XXXXXXXXXX): ")

        if validate_phone(phone):
            if not phone_exists(records, phone):
                phones.append(phone)
            else:
                print("Phone already exists.")
        else:
            print("Invalid phone number.")
            continue

        more = input("Add another phone? (y/n): ").lower()

        if more != "y":
            break

    # Emails
    emails = []

    while True:
        email = input("Enter Email: ")

        if validate_email(email):
            if not email_exists(records, email):
                emails.append(email)
            else:
                print("Email already exists.")
        else:
            print("Invalid email.")
            continue

        more = input("Add another email? (y/n): ").lower()

        if more != "y":
            break

    records[name] = {
        "phones": phones,
        "emails": emails
    }

    save_records(records)

    print("\nRecord added successfully 👍")


# =========================
# Edit Record
# =========================

def edit_record(records):

    name = input("Enter Name to Edit: ").strip()

    if name not in records:
        print("Record not found.")
        return

    data = records[name]

    print("""
1. Edit Name
2. Add Phone
3. Edit Phone
4. Delete Phone
5. Add Email
6. Edit Email
7. Delete Email
""")

    choice = input("Enter choice: ")

    # Edit Name
    if choice == "1":

        new_name = input("Enter new name: ")

        if validate_name(new_name):
            records[new_name] = records.pop(name)
            print("Name updated.")
        else:
            print("Invalid name.")

    # Add Phone
    elif choice == "2":

        phone = input("Enter new phone: ")

        if validate_phone(phone) and not phone_exists(records, phone):
            data["phones"].append(phone)
            print("Phone added.")
        else:
            print("Invalid or duplicate phone.")

    # Edit Phone
    elif choice == "3":

        for i, phone in enumerate(data["phones"], start=1):
            print(i, phone)

        index = int(input("Select phone number: ")) - 1

        if 0 <= index < len(data["phones"]):

            new_phone = input("Enter new phone: ")

            if validate_phone(new_phone) and not phone_exists(records, new_phone):
                data["phones"][index] = new_phone
                print("Phone updated.")
            else:
                print("Invalid or duplicate phone.")

    # Delete Phone
    elif choice == "4":

        if len(data["phones"]) == 1:
            print("At least one phone number required.")
            return

        for i, phone in enumerate(data["phones"], start=1):
            print(i, phone)

        index = int(input("Select phone to delete: ")) - 1

        if 0 <= index < len(data["phones"]):
            del data["phones"][index]
            print("Phone deleted.")

    # Add Email
    elif choice == "5":

        email = input("Enter new email: ")

        if validate_email(email) and not email_exists(records, email):
            data["emails"].append(email)
            print("Email added.")
        else:
            print("Invalid or duplicate email.")

    # Edit Email
    elif choice == "6":

        for i, email in enumerate(data["emails"], start=1):
            print(i, email)

        index = int(input("Select email: ")) - 1

        if 0 <= index < len(data["emails"]):

            new_email = input("Enter new email: ")

            if validate_email(new_email) and not email_exists(records, new_email):
                data["emails"][index] = new_email
                print("Email updated.")
            else:
                print("Invalid or duplicate email.")

    # Delete Email
    elif choice == "7":

        if len(data["emails"]) == 1:
            print("At least one email required.")
            return

        for i, email in enumerate(data["emails"], start=1):
            print(i, email)

        index = int(input("Select email to delete: ")) - 1

        if 0 <= index < len(data["emails"]):
            del data["emails"][index]
            print("Email deleted.")

    else:
        print("Invalid option.")

    save_records(records)


# =========================
# Delete Record
# =========================

def delete_record(records):

    name = input("Enter Name to Delete: ").strip()

    if name not in records:
        print("Record not found.")
        return

    confirm = input("Are you sure? (y/n): ").lower()

    if confirm == "y":
        del records[name]
        save_records(records)
        print("Record deleted successfully 👍")


# =========================
# Main Program
# =========================

def main():

    records = load_records()

    while True:

        print("""
<----------- MENU ----------->
1. List Records
2. Add Record
3. Edit Record
4. Delete Record
5. Exit
""")

        choice = input("Enter option: ")

        if choice == "1":
            list_records(records)

        elif choice == "2":
            add_record(records)

        elif choice == "3":
            edit_record(records)

        elif choice == "4":
            delete_record(records)

        elif choice == "5":
            print("Exiting... Thank You 😊")
            break

        else:
            print("Invalid option.")


# =========================
# Run Program
# =========================

if __name__ == "__main__":
    main()