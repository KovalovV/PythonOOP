# A software academy teaches two types of courses: 
# local courses that are held in some of the academy’s 
# local labs and offsite courses held in some other town 
# outside of the academy’s headquarters. Each course has 
# a name, a teacher assigned to teach it and a course 
# program (sequence of topics). Each teacher has a name 
# and knows the courses he or she teaches. Both courses 
# and teachers could be printed in human-readable text form. 
# All your courses should implement ICourse. Teachers should 
# implement ITeacher. Local and offsite courses should implement 
# ILocalCourse and IOffsiteCourse respectively. Courses and teachers 
# should be created only through the 
# ICourseFactory interface implemented by a class named CourseFactory. 
# Write a program that will form courses of software academy.

import json
from abc import ABC, abstractmethod

from const_course import COURSES_JSON, TEACHERS_JSON

class ITeacher(ABC):
    """
    Abstract class ІTeacher, which implements the 
    basic structure of the class Teacher
    """


    with open(TEACHERS_JSON) as courses:
            data_of_teachers = json.load(courses)

    @abstractmethod
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = Teacher.data_of_teachers[f'{self.name} {self.surname}']['courses']

    @abstractmethod
    def __str__(self):
        teacher_name = f'{self.name} {self.surname}'
        array_of_courses = Teacher.data_of_teachers[teacher_name]['courses']
        courses = ', '.join([f'{array_of_courses[i]}' for i in range(len(array_of_courses))])
        return f'Teacher:\n\t{self.name} {self.surname}\n\tCourses: {courses}'

    def __iter__(self):
        return CoursesIterator(self.courses)

    def str_check(self, input_string):
        if not isinstance(input_string, str):
            raise TypeError('Wrong field type, waiting for a string')

        if not len(input_string):
            raise ValueError('Empty field')
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.str_check(name)

        if not Teacher.data_of_teachers.get(name):
            raise ValueError('There is no teacher with this name')

        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.str_check(surname)

        self.__surname = surname

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        if not all(isinstance(course, str) for course in courses):
            raise TypeError('Wrong field type, waiting for a string')

        if not all(course for course in courses):
            raise ValueError('Empty field')

        self.__courses = courses

class CoursesIterator:
    """
    Iterator for Courses in the class
    """


    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.wrapped):
            raise StopIteration()

        self.index += 1
        return self.wrapped[self.index - 1]

class Teacher(ITeacher):
    """
    Class Teacher based on an abstract class. 
    Implements the rest of the structure of this class.
    """


    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return super().__str__()

class ICourse(ABC):
    """
    Abstract class ІCourse, which implements the 
    basic structure of the class Course
    """


    with open(COURSES_JSON) as courses:
            data_of_courses = json.load(courses)

    @abstractmethod
    def __init__(self, name, teachers):
        self.name = name
        self.teachers = teachers

    def __str__(self):
        item_course = ICourse.data_of_courses[self.name]
        item_course_theme = item_course["theme"]
        theme = ', '.join([f'{item_course_theme[i]}' for i in range(len(item_course_theme))])
        teachers = ', '.join([f'\n\t{ self.teachers[i]}' for i in range(len(self.teachers))])
        return f'Course: \n\t{self.name}\n\ttype: {item_course["type"]}\n\ttheme: {theme}\n\tteachers: {teachers}'

    def __iter__(self):
        return TeacherIterator(self.teachers)

    @property
    @abstractmethod
    def name(self):
        pass
    
    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    def teachers(self):
        return self.__teachers

    @teachers.setter
    def teachers(self, teachers):
        if not all(isinstance(teacher, Teacher) for teacher in teachers):
            raise TypeError('Wrong field type, waiting for a Teacher')

        if not (self.name in teacher.courses for teacher in teachers):
            raise KeyError('This teacher does not teach this course')

        self.__teachers = teachers

class TeacherIterator:
    """
    Iterator for Teachers in the class
    """


    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.wrapped):
            raise StopIteration()

        self.index += 1
        return self.wrapped[self.index - 1]

class ILocalCourse(ICourse):
    """
    Abstract class ILocalCourse, which implements the 
    basic structure of the class LocalCourse
    """


    @abstractmethod
    def __init__(self, name, teacher):
        self.name = name
        super(ILocalCourse, self).__init__(self.name, teacher)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Wrong field type, waiting for a string')

        if not len(name):
            raise ValueError('Empty field')

        if not ICourse.data_of_courses.get(name):
            raise ValueError('There is no course with this name')

        if not ICourse.data_of_courses.get(name)["type"] == "local":
            raise ValueError('This is not local course')

        self.__name = name

class LocalCourse(ILocalCourse):
    """
    Class LocalCourse based on an abstract class. 
    Implements the rest of the structure of this class.
    """


    def __init__(self, name, teacher):
        super().__init__(name, teacher)


class IOffsiteCourse(ICourse):
    """
    Abstract class IOffsiteCourse, which implements the 
    basic structure of the class OffsiteCourse
    """


    @abstractmethod
    def __init__(self, name, teacher):
        self.name = name
        super(IOffsiteCourse, self).__init__(self.name, teacher)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Wrong field type, waiting for a string')

        if not len(name):
            raise ValueError('Empty field')

        if not ICourse.data_of_courses.get(name):
            raise ValueError('There is no course with this name')
            
        if not ICourse.data_of_courses.get(name)["type"] == "offsite":
            raise ValueError('This is not offsite course')

        self.__name = name

class OffsiteCourse(IOffsiteCourse):
    """
    Class OffsiteCourse based on an abstract class. 
    Implements the rest of the structure of this class.
    """


    def __init__(self, name, teacher):
        super().__init__(name, teacher)

class ICourseFactory(ABC):
    """
    Abstract Class ICourseFactory. Contains a dictionary where it stores 
    instances of the objects it can create.
    """


    _dict_item = {
        "teacher": Teacher,
        "local course": LocalCourse,
        "offsite course": OffsiteCourse,
    }

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def create_item(self):
        pass

class CourseFactory(ICourseFactory):
    """
    Class CourseFactory. Creates a 
    class instance corresponding to the arguments.
    """


    def __str__(self):
        return f'Course Factory'

    def create_item(self, creating_obj, arg1, arg2):
        if not isinstance(arg1, str) or not isinstance(arg2, (str, list)):
            raise TypeError('Wrong field type, waiting for a string or Teacher to second arg')

        if not CourseFactory._dict_item.get(creating_obj):
            raise ValueError('There is no course with this name')

        return ICourseFactory._dict_item[creating_obj](arg1, arg2)

def main():
    teacher_local = CourseFactory().create_item('teacher', 'Vitala', 'Kovalov')
    print(teacher_local)

    teacher_local1 = CourseFactory().create_item('teacher', 'Vlad', 'Minin')
    print(teacher_local1)

    course_local = CourseFactory().create_item('local course', 'Python 2022 3.0', [teacher_local, teacher_local1])
    print(course_local)

    teacher_offsite = CourseFactory().create_item('teacher', 'Vadym', 'Shpuryk')
    print(teacher_offsite)

    course_offsite = CourseFactory().create_item('offsite course', 'C++ 2022 13.0', [teacher_offsite])
    print(course_offsite)


if __name__ == "__main__":
    main()