from Part_1 import students
import json
import csv
def save_students():
    with open("student.json", "w") as file:
        json.dump(students, file, indent=4)

def load_students_to_csv():
    with open("student.json", "r") as file:
        students_to_upload = json.load(file)
        return students_to_upload

def Load_students():
    with open("student.json", "r") as file:
        students_to_upload = json.load(file)
        return students[students_to_upload]

def export_to_csv():
    students_to_csv = load_students_to_csv()
    with open("report.csv", "w", newline="") as file:
        data = csv.writer(file)
        data.writerow(["Name", "ID", "Academic Year","Courses"])
        for student in students_to_csv:
            data.writerow([
                student["Name"],
                student["ID"],
                student["Academic Year"],
                student["Courses"]
            ])