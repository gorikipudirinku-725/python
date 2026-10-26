id = input("Enter student ID: ")

if len(id) == 10 and id.isalnum():
    year = "20" + id[:2]
    branch = id[6:8]
    print("Admission Year:", year)
    print("Branch Code:", branch)
else:
    print("Invalid ID")