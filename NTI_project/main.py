import os
blue   = "\033[94m"
yellow = "\033[93m"
cyan   = "\033[96m"
red    = "\033[91m"
green  = "\033[92m"
c_reset = "\033[0m"
def showMenu(selected):
    os.system("cls")
    options = [
        "Add Course",
        "Add Student",
        "Register Grade",
        "Print Student GPA",
        "Print Course Report",
        "Save Database",
        "Load Database",
        "Export Course CSV",
        "Edit name of student",
        "Print Student Report",
        "Delete Student",
        "Delete Course",
        "Edit Course",
        "Search Student by Name",
        "Course Average",
        "Best & Worst Students",
        "Exit"
    ]
    print(blue + "\n--- Student & Course Management System ---" + c_reset)
    for i, opt in enumerate(options):
        optionId = 0 if i == 16 else i + 1
        if optionId == selected:
            print(yellow + " -> " + cyan + opt + c_reset)
        else:
            print("    " + opt)
    print(blue + "------------------------------------------" + c_reset)
    print(yellow + "Use numbers and press Enter" + c_reset)

def main():
    students = []
    courses = []
    try:
        loadDatabase(students, courses, "database.txt")
    except Exception as e:
        print(red + "Warning:", e, c_reset)

    currentSelection = 1
    while True:
        showMenu(currentSelection)
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            continue
        try:
            if choice == 1:
                print(blue + "Add Course" + c_reset)
                addCourse(courses)
            elif choice == 2:
                print(blue + "Add Student" + c_reset)
                addStudent(students, courses)
            elif choice == 3:
                print(blue + "Register Grade" + c_reset)
                recordGrade(courses, students)
            elif choice == 4:
                print(blue + "Print Student GPA" + c_reset)
                printStudentGPA(students, courses)
            elif choice == 5:
                print(blue + "Print Course Report" + c_reset)
                printCourseReport(courses, students)
            elif choice == 6:
                print(blue + "Save Database" + c_reset)
                saveDatabase(students, courses, "database.txt")
                print(green + "Data saved successfully!" + c_reset)
            elif choice == 7:
                print(blue + "Load Database" + c_reset)
                loadDatabase(students, courses, "database.txt")
                print(green + "Data loaded successfully!" + c_reset)
            elif choice == 8:
                print(blue + "Export Course CSV" + c_reset)
                id = getStringInput("Enter Course ID to export (or type exit): ")
                if id != "exit":
                    c = findCourseById(courses, id)
                    if c:
                        exportCourseCSVToFile(c, students)
                    else:
                        print(red + "Course not found!" + c_reset)
            elif choice == 9:
                print(blue + "Edit name of student" + c_reset)
                Edit_Student_name(students)
            elif choice == 10:
                print(blue + "Print Student Report" + c_reset)
                studentReport(students, courses)
            elif choice == 11:
                print(blue + "Delete Student" + c_reset)
                deleteStudent(students)
            elif choice == 12:
                print(blue + "Delete Course" + c_reset)
                deleteCourse(courses)
            elif choice == 13:
                print(blue + "Edit Course" + c_reset)
                editCourse(courses)
            elif choice == 14:
                print(blue + "Search Student by Name" + c_reset)
                searchStudentByName(students)
            elif choice == 15:
                print(blue + "Course Average" + c_reset)
                courseAverage(courses)
            elif choice == 16:
                print(blue + "Best & Worst Students" + c_reset)
                bestWorstStudents(students, courses)
            elif choice == 0:
                saveDatabase(students, courses, "database.txt")
                print(yellow + "Data saved. Exiting program..." + c_reset)
                break
            else:
                print(red + "Invalid selection!" + c_reset)
        except Exception as e:
            print(red + "System Error:", e, c_reset)
        input(cyan + "\nPress Enter to return to menu..." + c_reset)
if __name__ == "__main__":
    main()
