#!/usr/bin/python3
import os
import subprocess
from datetime import datetime

LOG_FILE = "/home/joeo/output.txt"


def log_action(action_message):
    with open(LOG_FILE, "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {action_message}\n")


def add_user():
    username = input("Enter the username to add: ")
    os.system(f"sudo adduser {username}")
    log_action(f"Attempted to add user: {username}")

    passwd = input(f"Enter password for user {username}: ")
    command = f"echo '{username}:{passwd}' | sudo chpasswd"
    subprocess.run(command, shell=True, check=True)
    log_action(f"Password set for user: {username}")

    print(f"User {username} has been added successfully")


def modify_user():
    username = input("Enter the username to modify: ")
    print("Choose an option to modify:")
    print("1. Change shell")
    print("2. Change home directory")
    print("3. Set expiration date")
    print("4. Add user to a group")
    choice = input("Enter your choice: ")

    if choice == '1':
        new_shell = input("Enter the new shell (e.g., /bin/bash): ")
        os.system(f"sudo usermod -s {new_shell} {username}")
        log_action(f"Modified shell for user {username} to: {new_shell}")
        print(f"Shell for user {username} changed successfully")
    elif choice == '2':
        new_home = input("Enter the new home directory: ")
        os.system(f"sudo usermod -d {new_home} --move-home {username}")
        log_action(f"Changed home directory for user {username} to: {new_home}")
        print(f"Home directory for user {username} changed successfully")
    elif choice == '3':
        expiration_date = input("Enter the expiration date (YYYY-MM-DD): ")
        os.system(f"sudo usermod -e {expiration_date} {username}")
        log_action(f"Set expiration date for user {username} to: {expiration_date}")
        print(f"Expiration date for user {username} set successfully")
    elif choice == '4':
        group = input("Enter the group to add the user to: ")
        os.system(f"sudo usermod -aG {group} {username}")
        log_action(f"Added user {username} to group: {group}")
        print(f"User {username} added to group {group} successfully")
    else:
        print("Invalid choice")


def delete_user():
    username = input("Enter the username to delete: ")
    os.system(f"sudo userdel --force --remove {username}")
    log_action(f"Attempted to delete user: {username}")
    print(f"User {username} has been deleted successfully")


def list_users():
    print("Current system users:")
    os.system("cut -d: -f1 /etc/passwd")
    log_action("Listed system users")


def add_group():
    groupname = input("Enter the group name to add: ")
    os.system(f"sudo groupadd {groupname}")
    log_action(f"Attempted to add group: {groupname}")
    print(f"Group {groupname} has been added successfully")


def modify_group():
    groupname = input("Enter the group name to modify: ")
    print("Choose an option to modify:")
    print("1. Change group name")
    print("2. Add user to group")
    choice = input("Enter your choice: ")

    if choice == '1':
        new_groupname = input("Enter the new group name: ")
        os.system(f"sudo groupmod -n {new_groupname} {groupname}")
        log_action(f"Renamed group {groupname} to {new_groupname}")
        print(f"Group {groupname} renamed to {new_groupname} successfully")
    elif choice == '2':
        username = input("Enter the username to add to the group: ")
        os.system(f"sudo usermod -aG {groupname} {username}")
        log_action(f"Added user {username} to group {groupname}")
        print(f"User {username} added to group {groupname}")
    else:
        print("Invalid choice")


def delete_group():
    groupname = input("Enter the group name to delete: ")
    os.system(f"sudo groupdel {groupname}")
    log_action(f"Attempted to delete group: {groupname}")
    print(f"Group {groupname} has been deleted successfully")


def list_groups():
    print("Current system groups:")
    os.system("cut -d: -f1 /etc/group")
    log_action("Listed system groups")


def disable_user():
    username = input("Enter the username to disable: ")
    os.system(f"sudo usermod -L {username}")
    log_action(f"Disabled user: {username}")
    print(f"User {username} has been disabled successfully")


def enable_user():
    username = input("Enter the username to enable: ")
    os.system(f"sudo usermod -U {username}")
    log_action(f"Enabled user: {username}")
    print(f"User {username} has been enabled successfully")


def change_password():
    username = input("Enter the username to change password: ")
    os.system(f"sudo passwd {username}")
    log_action(f"Password changed for user: {username}")
    print(f"Password for user {username} has been changed successfully")


def about():
    print("This project was made by Youssef Ahmed under the supervision of Amira Abdel-Hady in ITI.")
    log_action("Displayed about information")


def main():
    while True:
        print("\nMain Menu")
        print("1. Add User              Add a user to the system.")
        print("2. Modify User           Modify an existing user.")
        print("3. Delete User           Delete an existing user.")
        print("4. List Users            List all users on the system.")
        print("5. Add Group             Add a user group to the system.")
        print("6. Modify Group          Modify a group and its list of members.")
        print("7. Delete Group          Delete an existing group.")
        print("8. List Groups           List all groups on the system.")
        print("9. Disable User          Lock the user account.")
        print("10. Enable User          Unlock the user account.")
        print("11. Change Password      Change Password of a user.")
        print("12. About                Information about this program.")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            modify_user()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            list_users()
        elif choice == '5':
            add_group()
        elif choice == '6':
            modify_group()
        elif choice == '7':
            delete_group()
        elif choice == '8':
            list_groups()
        elif choice == '9':
            disable_user()
        elif choice == '10':
            enable_user()
        elif choice == '11':
            change_password()
        elif choice == '12':
            about()
        elif choice == '0':
            log_action("Exited the program")
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
