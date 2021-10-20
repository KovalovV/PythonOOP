from statistics import mean

class Group():
    def __init__(self, students):
        if not all(isinstance(student, Student) for student in students):
            raise TypeError('Invalid input data type')
        self.students = sorted(students, key = lambda obj: obj.avarage, reverse = True)

    def __str__(self):
        return '\n'.join([f'{self.students[i].name} {self.students[i].surname} {self.students[i].avarage}' for i in range(5)])

class Student():
    def __init__(self, name, surname, record_book_id, grades):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(record_book_id, int) or not isinstance(record_book_id, int) or not all(isinstance(grade, int) for grade in grades):
            raise TypeError('Invalid input data type')
        if not len(name) or not len(surname) or record_book_id <= 0 or not all(0 < grade <= 100 for grade in grades):
            raise ValueError('Incorrect data input values')
        self.name = name
        self.surname = surname
        self.record_book_id = record_book_id
        self.grades = grades
        self.avarage = mean(self.grades)
def main():  
    student1 = Student('Vitala', 'Kovalov', 1, [100, 85, 65, 70, 80])
    student2 = Student('Sergiu', 'Buriakivskyi', 1, [75, 95, 54, 99, 76])
    student3 = Student('Roma', 'Tkachenko', 1, [81, 80, 85, 99, 45])
    student4 = Student('Vasyl', 'Pavliuk', 1, [57, 35, 74, 98, 67])
    student5 = Student('Kolia', 'Sever', 1, [54, 55, 89, 78, 63])
    student6 = Student('Max', 'Kakchenko', 1, [95, 74, 82, 19, 43])
    group = Group([student1, student2, student3, student4, student5, student6])
    print(group)

main()