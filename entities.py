class Student:
    def __init__(self, student_id: int, name: str):
        self.__student_id = int(student_id)
        self.__name = name

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def set_id(self, new_id):
        self.__student_id = new_id

    def set_name(self, new_name):
        self.__name = new_name


class Discipline:
    def __init__(self, discipline_id: int, name: str):
        self.__discipline_id = int(discipline_id)
        self.__name = name

    def get_id(self):
        return self.__discipline_id

    def get_name(self):
        return self.__name

    def set_id(self, new_id):
        self.__discipline_id = new_id

    def set_name(self, new_name):
        self.__name = new_name


class Grade:
    def __init__(self, student_id, discipline_id, grade_value: list):
        self.__student_id = student_id
        self.__discipline_id = discipline_id
        self.__grade_value = grade_value

    def get_discipline_id(self):
        return self.__discipline_id

    def get_student_id(self):
        return self.__student_id

    def get_grade_value(self):
        return self.__grade_value

    def set_grade_value(self, new_value):
        self.__grade_value = new_value
