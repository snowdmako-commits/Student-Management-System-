from database import load_students, save_students

def add_student():

    try:
        students = load_students()

        name = input("enter student name: ")
        age = int(input("enter student age: "))

        student_id = max([s["id"] for s in students], default=0) + 1

        student = {
            "id": student_id,
            "name": name,
            "age": age
        }

        students.append(student)
        save_students(students)

        print("student added successfully")

    except ValueError as e:
        print("value error:", e)

    except Exception as e:
        print("error:", e)

def show_students():

    try:
        students = load_students()

        if not students:
            print("student list is empty")
            return

        for student in students:
            print("--------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])

    except Exception as e:
        print("error:", e)

def update_student():

    try:
        students = load_students()

        student_id = int(input("enter student ID: "))

        for student in students:

            if student["id"] == student_id:
                student["name"] = input("enter new name: ")
                student["age"] = int(input("enter new age: "))

                save_students(students)
                print("student updated")
                return

        print("student not found")

    except ValueError as e:
        print("value Error:", e)

    except Exception as e:
        print("error:", e)

