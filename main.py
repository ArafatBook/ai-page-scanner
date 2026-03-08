import json
import os
from getpass import getpass

FILE = "passwords.json"

def load_passwords():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_passwords(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_account():
    data = load_passwords()
    account = input("Account name: ")
    username = input("Username: ")
    password = getpass("Password: ")

    data[account] = {
        "username": username,
        "password": password
    }

    save_passwords(data)
    print("✅ Account saved")

def view_accounts():
    data = load_passwords()

    if not data:
        print("No accounts saved")
        return

    for acc in data:
        print(f"\nAccount: {acc}")
        print("Username:", data[acc]["username"])
        print("Password:", data[acc]["password"])

def delete_account():
    data = load_passwords()
    acc = input("Account name to delete: ")

    if acc in data:
        del data[acc]
        save_passwords(data)
        print("🗑 Deleted")
    else:
        print("Account not found")

def menu():
    while True:
        print("\n--- Password Manager ---")
        print("1. Add account")
        print("2. View accounts")
        print("3. Delete account")
        print("4. Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_account()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            delete_account()
        elif choice == "4":
            break
        else:
            print("Invalid option")

menu()
