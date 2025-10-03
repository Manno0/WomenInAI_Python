class Student :
    def __init__(self,name, grades):
        self.name = name
        if type(grades) is list :
            self.grades = grades
        else :
            self.grades = [grades]

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)
    def __str__(self):
        return f"Name : {self.name} , Grades : {self.grades}, Average Grade : {self.get_average_grade()}"

class Classroom :
    def __init__(self, students):
        self.students = students
    def add_student(self,student):
        self.students.append(student)
    def get_top_students(self):
        sorted_students = sorted(self.students, key = lambda student : student.get_average_grade(), reverse=True)
        top_students = []
        for i in range(3):
            top_students.append(sorted_students[i].name)
        return f"Top 3 students : {top_students}"
    def get_failed_students(self):
        failed_students = filter(lambda student: student.get_average_grade() < 51, self.students)
        failed_students_names = []
        for student in failed_students:
            failed_students_names.append(student.name)
        return f"Failed Students : {failed_students_names}"
    def __str__(self):
        names = []
        for students in self.students:
            names.append(students.name)
        return f"Classroom : {names}"

ika = Student("Ika", [100,84,52])
mariam = Student("Mariam", 87)
ana = Student("Ana",[99,45,75,100,20] )
lizi = Student("Lizi", [40,84,52,20,10,24])
keti = Student("Keti", [10,20,20,40,80])
nini = Student("Nini",[99,70,90,100,100] )
sopo = Student("Sopo", [100,84,80,52])
salo = Student("Salome", 50)
john = Student("John",[100,99,98] )

ika.add_grade(100)
mariam.add_grade(100)
salo.add_grade(20)
lizi.add_grade(40)

classroom = Classroom([ika, mariam, ana, lizi,keti, sopo, salo])
classroom.add_student(john)
classroom.add_student(nini)
print(classroom)

print(classroom.get_top_students())
print(classroom.get_failed_students())