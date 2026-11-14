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

