print("Welcome to Library Management")
print("Write 'ADD' to add a data.")
print("Write 'VIEW' to view whole data")
print("Write 'SEARCH' to search a data")
print("Write 'EXIT' to exit.")

input1 = input(">>> ")

def add():
    import datetime
    dt = datetime.datetime.now().strftime("%d-%m-%Y") 
    name = input("Enter your name: ")
    class_ = input("Enter your class: ")
    roll = input("Enter your roll: ")
    book = input("Enter the book name: ")
    File_object = open(r'C:\Users\HP\OneDrive\Desktop\PROJECTS\Beginner Projects\Lib Software\data.txt', "a")
    File_object.write(f"Date: {dt}" + "\n")
    File_object.write(f"Name: {name}" + "\n")
    File_object.write(f"Class: {class_}" + "\n")
    File_object.write(f"Roll Number: {roll}" + "\n")
    File_object.write(f"Book: {book}" + "\n")
    File_object.close()
    print("Data added.")

def search():
    search = input("Enter the name of the student: ")
    file = open(r'C:\Users\HP\OneDrive\Desktop\PROJECTS\Beginner Projects\Lib Software\data.txt', "r")
    for line in file:
        if search in line:
            print(line)
            print(file.readline())
            print(file.readline())
            print(file.readline())
    file.close()

def view():
    File_object = open(r'C:\Users\HP\OneDrive\Desktop\PROJECTS\Beginner Projects\Lib Software\data.txt', "r")
    for line in File_object:
        print(line)
    File_object.close()

while True:
    if input1 == "ADD" or input1 == "add" or input1 == "Add":
        add()
        
    elif input1 == "SEARCH" or input1 == "search" or input1 == "Search":
        search()

    elif input1 == "VIEW" or input1 == "view" or input1 == "View":
        view()
    elif input1 == "EXIT" or input1 == "exit" or input1 == "Exit":
        exit()
    else:
        print("Please enter a valid command.")
    input1 = input(">>> ")