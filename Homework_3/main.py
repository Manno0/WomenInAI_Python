students = [("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 85), ("Eve", 78), ("Frank", 85), ("Mark", 50), ("George", 21)]

def uniqueNames(names):
    uniquenscores = set()
    for name in names:
        uniquenscores.add(name[1])
    print(f"Uniques Scores :  {uniquenscores}")

def highestScore(students):
    besttoworst = sorted(students, key = lambda student: student[1], reverse = True)
    beststudents = []
    for i in range(2):
        beststudents.append(besttoworst[i][0])
    print(f"Best students : {beststudents}")

def failedStudents(students):
    failedstudents = list(filter(lambda student : student[1]<51, students))
    failedstudentsnames = []
    for failedstudent in failedstudents:
        failedstudentsnames.append(failedstudent[0])
    print(f"Failed students : {failedstudentsnames}")

uniqueNames(students)
highestScore(students)
failedStudents(students)