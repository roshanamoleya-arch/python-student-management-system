students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = input("Enter Student ID:40 ")
        name = input("Enter Name:A.Roshana ")
        age = input("Enter Age: 19")
        course = input("Enter Course:BCA(GEN AI) ")
        marks = input("Enter Marks:92 ")

        students[sid] = {
            "Name": name,
            "Age": age,
            "Course": course,
            "Marks": marks
        }

        print("Student added successfully!")

    elif choice == "2":
        if students:
            for sid, data in students.items():
                print("\nStudent ID:", sid)
                for key, value in data.items():
                    print(f"{key}: {value}")
        else:
            print("No student records found.")

    elif choice == "3":
        sid = input("Enter Student ID: ")
        if sid in students:
            print(students[sid])
        else:
            print("Student not found.")

    elif choice == "4":
        sid = input("Enter Student ID: ")
        if sid in students:
            students[sid]["Name"] = input("New Name: ")
            students[sid]["Age"] = input("New Age: ")
            students[sid]["Course"] = input("New Course: ")
            students[sid]["Marks"] = input("New Marks: ")
            print("Record updated successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        sid = input("Enter Student ID: ")
        if sid in students:
            del students[sid]
            print("Student record deleted.")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")