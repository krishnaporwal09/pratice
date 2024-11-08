#!/usr/bin/python3

import os
import sys
import datetime

def show_menu():
    print("\nSimple Linux Tool - Choose an option:")
    print("1. Display current date and time")
    print("2. List files in the current directory")
    print("3. Show system information")
    print("4. Create a new file")
    print("5. Exit")

def display_date_time():
    now = datetime.datetime.now()
    print(f"\nCurrent Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def list_files():
    print("\nFiles in the current directory:")
    for file in os.listdir('.'):
        print(file)

def show_system_info():
    print("\nSystem Information:")
    os.system('uname -a')

def create_new_file():
    filename = input("\nEnter the name of the new file: ")
    with open(filename, 'w') as f:
        content = input("Enter content for the file: ")
        f.write(content)
    print(f"File '{filename}' created successfully!")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            display_date_time()
        elif choice == '2':
            list_files()
        elif choice == '3':
            show_system_info()
        elif choice == '4':
            create_new_file()
        elif choice == '5':
            print("\nExiting the program. Goodbye!")
            sys.exit()
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
