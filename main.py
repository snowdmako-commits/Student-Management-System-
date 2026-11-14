from students import add_student, show_students, update_student, delete_student, search_student

while True:
    print("""
    ===== STUDENT MANAGEMENT SYSTEM =====

    1. Add Student
    2. Show Students
    3. Update Student
    4. Delete Student
    5. Search Student
    6. Exit
    """)

    try:
        choice = int(input("enter choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            show_students()

        elif choice == 3:
            update_student()

        elif choice == 4:
            delete_student()

        elif choice == 5:
            search_student()

        elif choice == 6:
            print("Goodbye!")
            break
        
        else:
            print("invalid choice")

    except ValueError:
        print("please enter a number")
