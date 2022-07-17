import os     # deal with file

path = r"C:\Users\XaveF\Documents"

print("\n== File Detection ==")
print("1. Display path")
print("2. Check file existence")
print("3. Check file type")
print("E. Exit")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\nFile location: ", path)
    elif choice == '2':
        if os.path.exists(path):
            print("\nFile exists")
        else:
            print("\nFile does not exist")
    elif choice == '3':
        if os.path.isdir(path):
            print("\nFile is a directory")
        else:
            print("\nFile is not a directory")
    else:
        print("\n[ Invalid choice ]")

    print("\n== File Detection ==")
    print("1. Display path")
    print("2. Check file existence")
    print("3. Check file type")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")