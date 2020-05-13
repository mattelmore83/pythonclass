def find_highest(data):
    highGrade = 0
    highStudent = None

    for student in data:
        grade = data[student]
        if grade>highGrade:
            highGrade = grade
            highStudent = student
    return highStudent

my_grades = {
    'Jan': 75,
    'Bob': 88,
    'Jil': 52,
    'Dan': 99,
    'Pat': 99
}

highest = find_highest(my_grades)

print('Highest grade is',highest,'with a',my_grades[highest])