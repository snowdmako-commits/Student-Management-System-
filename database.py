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