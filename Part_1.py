students=[]
class Student():
    def __init__(self,name,id,year):
        self.courses = []
        self.name= name
        self.id = id
        self.year = year
        self.student = {"Name": self.name, "ID": self.id, "Academic Year": self.year}
        if self.id in students :
            print("The ID is used before.")
        else:
            students.append(self.student)
    def del_update(self):
        students.remove(self.student)
        print("The student has been deleted!")
    def student_course(self):

        while True:
            course =input ("Enter the name of the course:")
            if course in self.courses :
                print("You have already registered for this course")
            else:
                self.courses.append(course)
            condition = input("Do you want to add another course(Yes/No): ").lower()
            if condition == "yes" :
                continue
            else:
                break
    def display(self):
        print("Here is your Report")
        print(f"Name: {self.name} " )
        print(f"ID: {self.id}")
        print(f"Academic year: {self.year}")
        print(f"Courses: {self.courses}")
        print(students)
    def update_student(self):
        update = input("What do you want to update (Name/ID/Year): ").lower()
        if update == "name":
            id1=input("Enter the id: ")
            for student in students:
                if student["ID"] == id1:
                    self.name = input("Enter the new name: ")
                    student["Name"] = self.name
                    break
        elif update == "id":
            name1 = input("Enter the name: ")
            for student in students:
                if student["Name"] == name1:
                    self.id = input("Enter the new ID: ")
                    student["ID"]=self.id
                    break
        elif update == "year":
            id1 = input("Enter the id: ")
            for student in students:
                if student["ID"] == id1:
                    self.year=input("Enter the new Academic Year: ")
                    student["Academic Year"]=self.year
                    break
def Input():
    Name = input("Enter the Name:")
    ID = input("Enter the ID: ")
    year = input("Enter the Academic Year: ")
    info=[Name,ID,year]
    return info


info1=Input()
student1=Student(*info1)

student1.update_student()
# student1.update_student()
student1.display()
# student1.student_course()
# student1.display()
#print(students)
info2=Input()
student2 = Student(*info2)

#student2.del_update()

