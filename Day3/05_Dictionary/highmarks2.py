from typing import Dict

def find_highest(data):
    high_grade = 0
    high_student = None

    for student in data:
        grade = data[student]
        if grade > high_grade:
            high_grade = grade
            high_student = student
    return high_student

def get_duplicates(gradeData):
    newDict: Dict[int, str] = {}  # create a blank dictionary 'r'

    # create keys -  key is grade
    for studentName in gradeData:
        grade = gradeData[studentName]
        newDict[grade] = ''

    # add students under the grade key
    for studentName in gradeData:
        grade = gradeData[studentName]
        newDict[grade] += studentName + ' '

    return newDict


my_grades: Dict[str, int] = {
    'Jan': 75,
    'Bob': 88,
    'Jil': 52,
    'Dan': 99,
    'Pat': 99
}

highest = find_highest(my_grades)

print('Highest grade is',highest,'with a',my_grades[highest])
print(get_duplicates(my_grades))