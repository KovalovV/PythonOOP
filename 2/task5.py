from statistics import mean

MAX_STUDENT = 20
TOP = 8
AMOUNT_LESSONS = 5

class Student():
    """
    Class Student. Accepts name, surname, number of record book,
    student grades. Controls input and reports errors.
    """

    def __init__(self, name = None, surname = None, record_book_id = None, grades = []):
        self.name = name
        self.surname = surname
        self.grades = grades
        self.record_book_id = record_book_id
        self.avarage = mean(self.__grades)

    def count_avarage(self):
        """
        Method count_avarage().
        Calculates and sets a new average student score when calling set_grades(grades) 
        """

        self.avarage = mean(self.__grades)

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def grades(self):
        return self.__grades
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Invalid input data type')
        if not len(name):
            raise ValueError('Incorrect data input values')
        self.__name = name

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError('Invalid input data type')
        if not len(surname):
            raise ValueError('Incorrect data input values')
        self.__surname = surname

    @grades.setter
    def grades(self, grades):
        if not all(isinstance(grade, int) for grade in grades):
            raise TypeError('Invalid input data type')
        if not all(0 < grade <= 100 for grade in grades) or  len(grades) != 5:
            raise ValueError('Incorrect data input values')
        self.__grades = grades
        self.count_avarage()


class Group():
    """
    Class Group. Accepts an array of students in the group,
    controls that there are no students with the same name and surname.
    Displays the top 5 students in the group.
    """

    
    def __init__(self, students = []):
        self.group_student = []
        for student in students:
            if f'{student.name} {student.surname}' in self.group_student:
                raise ValueError('Same students')
            self.group_student.append(f'{student.name} {student.surname}')
        self.__students = students

    def __str__(self):
        return '\n'.join([f'{self.students[i].name} {self.students[i].surname} {self.students[i].avarage}' for i in range(TOP)])
    
    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, student):
        if not isinstance(student, Student):
            raise TypeError('Invalid input data type')

        if f'{student.name} {student.surname}' in self.group_student:
            raise ValueError('Same students')
        self.group_student.append(f'{student.name} {student.surname}')
        self.__students.append(student)

        if len(self.group_student) + 1 > MAX_STUDENT:
            raise ValueError('Large group, maximum 20 students')

        self.__students = sorted(self.__students, key = lambda obj: obj.avarage, reverse = True)
    
def main():  
    student1 = Student('Vitala', 'Kovalov', 1, [100, 85, 65, 70, 99])
    student2 = Student('Sergiu', 'Buriakivskyi', 1, [75, 95, 54, 99, 76])
    student3 = Student('Roma', 'Tkachenko', 1, [81, 80, 85, 99, 45])
    student4 = Student('Vasyl', 'Pavliuk', 1, [57, 35, 74, 98, 67])
    student5 = Student('Kolia', 'Sever', 1, [54, 55, 89, 78, 63])
    student6 = Student('Max', 'Kakchenko', 1, [95, 100, 82, 90, 98])
    student7 = Student('Maaax', 'Kakchenko', 1, [95, 74, 82, 19, 43])

    group = Group([student1, student2, student3, student4, student5, student6, student7])

    student8 = Student('Gleb', 'Karik', 1, [85, 100, 87, 91, 87])
    student9 = Student('Max', 'Kakchenko', 1, [80, 75, 63, 46, 57])

    group.students = student9
    print(group)


main()