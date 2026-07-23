courses=[]
class Course:
    def __init__(self,name_course,id_course,credit_hours):
        self.name_course=name_course
        self.id_course=id_course
        self.credit_hours=int(credit_hours)
        self.students={}
    def update_course(self):
        print("1.update name")
        print("2.update credit hours")
        print("3.update both")
        choice=(input("enter choice:1/2/3:"))
        if choice=="1" or choice=="3":
            new_name_course=(input("enter new course name:"))
            self.name_course=new_name_course
        if choice=="2" or choice=="3":
            new_credit_hours=int(input("enter new credit hours:"))
            self.credit_hours=new_credit_hours
        print("course update successfully")
    def delete_course(self):
        if self in courses:
            courses.remove(self)
            print("course deleted successfully")
    def add_grade(self):
        student_name=(input("enter student name:"))
        grade=float(input(f"enter grade for {student_name} "))
        self.students[student_name]=grade
    def course_report(self):
        print("=========================COURSE REPORT================================")
        print(f"course name:{self.name_course}")
        print(f"course Id:{self.id_course}")
        print(f"credit hours:{self.credit_hours}")
        print("students grades:")
        if self.students:
            for student,grade in self.students.items():
                print(f"{student}:{grade}")
        else:
            print("no grades recorded yet.")
def add_new_course():
    id_course=(input("enter id of course:"))
    for course in courses:
        if course.id_course==id_course:
            print("course is exists!")
            return
    name_course=(input("enter name of course:"))
    credit_hours=int(input("enter credit hours of course:"))
    new_course=Course(name_course,id_course,credit_hours)
    courses.append(new_course)
    print("course add successfully")
while True:
    print("1.add course")
    print("2.modify/action on course")
    print("3.display all courses")
    print("4.exit")
    choice2=(input("enter your choice 1/2/3/4:"))
    if choice2=="1":
        add_new_course()
    elif choice2=="2":
        if not courses:
            print("not found courses")
            continue
        id=(input("enter the id of course you want to make any modification:"))
        found=False
        for course in courses:
            if course.id_course==id:
                found=True
                choice=input("do you want to update/delete/report/add_grade:")
                if choice=="update":
                    course.update_course()
                elif choice=="delete":
                    course.delete_course()
                elif choice=="report":
                    course.course_report()
                elif choice=="add_grade":
                    course.add_grade()
                else:
                    print("choice is incorrect")
                break
        if not found:
            print("course id not found")
    elif choice2=="3":
        if not courses:
            print("no courses found")
        else:
            for course in courses:
                print(f"==================Course=======================")
                print(f"course_ID:{course.id_course}")
                print(f"course_name:{course.name_course}")
                print(f"credit_hours:{course.credit_hours}")
                print("====================================================")
    elif choice2=="4":
        break
    else:
        print("choice is incorrect")


