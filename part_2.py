courses=[]
class Course:
    def __init__(self,name_course,id_course,credit_hours):
        self.name_course=name_course
        self.id_course=id_course
        self.credit_hours=credit_hours
        self.students={}
        self.course={}
        self.course["course name"]=self.name_course
        self.course["course Id"]=self.id_course
        self.course["credit hours"]=self.credit_hours
        if not courses:
            courses.append(self.course)
            print("course add successfully")
        else:
            exists=False
            for course in courses:
                if course["course Id"]==self.id_course:
                    exists=True
                    break
            if exists:
                print("course Id is already exists")
            else:
                courses.append(self.course)
                print("course add successfully")
    def update_course(self):
        while True:
            update=(input("do you want update yes/no?"))
            if update=="yes":
                self.name_course=(input("enter new course name:"))
                self.credit_hours=(input("enter new credit hours:"))
                self.course["course name"]=self.name_course
                self.course["credit hours"]=self.credit_hours
                print("course updated successfully")
            else:
                break
    def delete_course(self):
        if self.course in courses:
            courses.remove(self.course)
            print("course delete successfully")
        else:
            print("not found course")
    def course_report(self):
        print("====================COURSE REPORT==============================")
        print(f"course name is:{self.name_course}")
        print(f"course Id is:{self.id_course}")
        print(f"credit hours is:{self.credit_hours}")

objects=[]
num=int(input("How many courses do you want add?"))
for i in range(num):
    course_name=(input("enter name of course:"))
    course_id=(input("enter id of course:"))
    credit_hours=int(input("enter credit hours of course:"))
    course=Course(course_name,course_id,credit_hours)
    objects.append(course)
print(f"courses is:{courses}")
while True:
    ask=(input("do you want to make any modification yes/no?"))
    if ask=="yes":
        id=(input("enter the id of course:"))
        choice=(input("do you want to update/delete/report:"))
        found=False
        for object in objects:
            if object.id_course==id:
                found=True
                if choice=="update":
                    object.update_course()
                elif choice=="delete":
                    object.delete_course()
                elif choice=="report":
                    object.course_report()
                break
        if not found:
            print("course Id not found")
    else:
        print(f"courses after modification:{courses}")
        break

