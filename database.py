import json

def load_students():
    try:
        file = open("students.json", "r", encoding="utf-8")
        students = json.load(file)
        file.close()
        return students

    except FileNotFoundError as e:
        print("File Error:", e)
        return []

    except json.JSONDecodeError as e:
        print("JSON Error:", e)
        return []

def save_students(students):
    try:
        file = open("students.json", "w", encoding="utf-8")
        json.dump(students, file, indent=4)
        file.close()

    except Exception as e:
        print("Error:", e)