from src.domain.entities import Student, Discipline, Grade


class StudentService:
    def __init__(self, repository):
        self.__student_repository = repository

    def add_student(self, student_id, name):
        try:
            if student_id.isnumeric() is not True:
                raise ValueError("Invalid ID")
            student_id = int(student_id)
            if student_id <= 0:
                raise ValueError("Invalid ID")
            ids = self.__student_repository.list_of_ids()
            if student_id in ids:
                raise ValueError('Invalid ID')
            student = Student(student_id, name)
            self.__student_repository.add_student(student)
            return True
        except ValueError:
            return False

    def list_all_students(self):
        return self.__student_repository.list_students()

    def list_ids(self):
        return self.__student_repository.list_of_ids()

    def update_students(self, old_id, new_id, new_name):
        old_id = int(old_id)
        new_id = int(new_id)
        try:
            ids = self.__student_repository.list_of_ids()
            if old_id not in ids:
                raise ValueError('No student to update or duplicate/invalid ID')
            if new_id in ids:
                raise ValueError('No student to update or duplicate/invalid ID')
            if new_id <= 0:
                raise ValueError('No student to update or duplicate/invalid ID')
            if old_id <= 0:
                raise ValueError('No student to update or duplicate/invalid ID')
            self.__student_repository.update_student(old_id, new_id, new_name)
            return True
        except ValueError:
            return False

    def remove_students(self, student_id):
        student_id = int(student_id)
        try:
            ids = self.__student_repository.list_of_ids()
            if student_id not in ids:
                raise ValueError('No student to delete or invalid ID')
            if student_id <= 0:
                raise ValueError('No student to delete or invalid ID')
            self.__student_repository.remove_student(student_id)
            return True
        except ValueError:
            return False

    def search_students(self, parameter):
        if type(parameter) == str:
            list_of_students_found = self.__student_repository.search_student_by_name(parameter)
            for student in list_of_students_found:
                print(str(student.get_id()) + ' ' + student.get_name())
        elif type(parameter) == int:
            list_of_students_found = self.__student_repository.search_student_by_id(parameter)
            for student in list_of_students_found:
                print(str(student.get_id()) + ' ' + student.get_name())

    def get_only_name_list(self, id_list):
        name_list = []
        for student_id in id_list:
            student = self.__student_repository.search_one_student_by_id(student_id)
            name_list.append(student)
        return name_list


class DisciplineService:
    def __init__(self, repository):
        self.__discipline_repository = repository

    def add_discipline(self, discipline_id, name):
        try:
            if discipline_id.isnumeric() is not True:
                raise ValueError("Invalid ID")
            discipline_id = int(discipline_id)
            if discipline_id <= 0:
                raise ValueError("Invalid ID")
            ids = self.__discipline_repository.list_of_ids()
            if discipline_id in ids:
                raise ValueError('Invalid ID')
            discipline = Discipline(discipline_id, name)
            self.__discipline_repository.add_discipline(discipline)
            return True
        except ValueError:
            return False

    def list_all_disciplines(self):
        return self.__discipline_repository.list_disciplines()

    def update_disciplines(self, old_id, new_id, new_name):
        old_id = int(old_id)
        new_id = int(new_id)
        try:
            ids = self.__discipline_repository.list_of_ids()
            if old_id not in ids:
                raise ValueError('No discipline to update or duplicate/invalid ID')
            if new_id in ids:
                raise ValueError('No discipline to update or duplicate/invalid ID')
            if new_id <= 0:
                raise ValueError('No discipline to update or duplicate/invalid ID')
            if old_id <= 0:
                raise ValueError('No discipline to update or duplicate/invalid ID')
            self.__discipline_repository.update_discipline(old_id, new_id, new_name)
            return True
        except ValueError:
            return False

    def remove_disciplines(self, discipline_id):
        discipline_id = int(discipline_id)
        try:
            ids = self.__discipline_repository.list_of_discipline_ids()
            if discipline_id not in ids:
                raise ValueError('No student to delete or invalid ID')
            if discipline_id <= 0:
                raise ValueError('No student to delete or invalid ID')
            self.__discipline_repository.remove_discipline(discipline_id)
            return True
        except ValueError:
            return False

    def search_disciplines(self, parameter):
        if type(parameter) == str:
            list_of_disciplines_found = self.__discipline_repository.search_discipline_by_name(parameter)
            for discipline in list_of_disciplines_found:
                print(str(discipline.get_id()) + ' ' + discipline.get_name())
        elif type(parameter) == int:
            list_of_disciplines_found = self.__discipline_repository.search_discipline_by_id(parameter)
            for discipline in list_of_disciplines_found:
                print(str(discipline.get_id()) + ' ' + discipline.get_name())


class GradeService:
    def __init__(self, repository):
        self.__grade_repository = repository

    def list_all_grades(self):
        return self.__grade_repository.list_grades()

    def list_student_ids(self):
        return self.__grade_repository.get_list_of_student_ids()

    def list_discipline_ids(self):
        return self.__grade_repository.get_list_of_discipline_ids()

    def add_student(self, student_id):
        self.__grade_repository.add_student(student_id)

    def remove_grades_for_student(self, student_id):
        student_id = int(student_id)
        try:
            ids = self.__grade_repository.get_list_of_student_ids()
            if student_id not in ids:
                raise ValueError('No student to delete or invalid ID')
            if student_id <= 0:
                raise ValueError('No student to delete or invalid ID')
            self.__grade_repository.remove_grade_for_student(student_id)
        except ValueError:
            return

    def remove_grades_for_discipline(self, discipline_id):
        discipline_id = int(discipline_id)
        try:
            ids = self.__grade_repository.get_list_of_discipline_ids()
            if discipline_id not in ids:
                raise ValueError('No discipline to delete or invalid ID')
            if discipline_id <= 0:
                raise ValueError('No discipline to delete or invalid ID')
            self.__grade_repository.remove_grade_for_discipline(discipline_id)
        except ValueError:
            return

    def display_student_grades(self, student_id):
        student_id = int(student_id)
        try:
            ids = self.__grade_repository.get_list_of_student_ids()
            if student_id not in ids:
                raise ValueError('Invalid ID')
            if student_id <= 0:
                raise ValueError('Invalid ID')
            grades_found = self.__grade_repository.search_student_grades(student_id)
            return grades_found
        except ValueError:
            return

    def display_discipline_grades(self, discipline_id):
        discipline_id = int(discipline_id)
        try:
            ids = self.__grade_repository.get_list_of_discipline_ids()
            if discipline_id not in ids:
                raise ValueError('Invalid ID')
            if discipline_id <= 0:
                raise ValueError('Invalid ID')
            grades_found = self.__grade_repository.search_discipline_grades(discipline_id)
            return grades_found
        except ValueError:
            return

    def grade_student(self, student_id, discipline_id, grade_value):
        try:
            if student_id.isnumeric() is not True:
                raise ValueError("Invalid ")
            student_id = int(student_id)
            if student_id <= 0:
                raise ValueError("Invalid ")
            if discipline_id.isnumeric() is not True:
                raise ValueError("Invalid ")
            discipline_id = int(discipline_id)
            if discipline_id <= 0:
                raise ValueError("Invalid ")
            discipline_ids = self.__grade_repository.get_list_of_discipline_ids()
            if discipline_id not in discipline_ids:
                raise ValueError('Invalid')
            if grade_value <= 0 or grade_value > 10:
                raise ValueError("Invalid ")
            self.__grade_repository.add_grade(student_id, discipline_id, grade_value)
            return True
        except ValueError:
            return False

    # def validate_discipline(self, discipline_id):
    #     if discipline_id.isnumeric() is not True:
    #         return False
    #     discipline_id = int(discipline_id)
    #     if discipline_id <= 0:
    #         return False
    #     discipline_ids = self.__grade_repository.get_list_of_discipline_ids()
    #     if discipline_id not in discipline_ids:
    #         return False
    #     return True
    #
    # def grade_every_student(self, student_id, discipline_id, grade):
    #     try:
    #         if grade <= 0:
    #             raise ValueError("Invalid")
    #         self.__grade_repository.add_grade(student_id, discipline_id, grade)
    #     except ValueError:
    #         print('Please enter a grade between 0 and 10.')

    def fail_statistic(self, one_failure, more_failures, no_failures):
        students_ids = self.__grade_repository.get_list_of_student_ids()
        for student in students_ids:
            failures = self.__grade_repository.get_fails_student(student)
            if failures == 0:
                no_failures += 1
            elif failures == 1:
                one_failure += 1
            else:
                more_failures += 1
        return no_failures, one_failure, more_failures

    def student_average_statistic(self):
        list_averages = []
        students_ids = self.__grade_repository.get_list_of_student_ids()
        for student in students_ids:
            average = self.__grade_repository.get_average_student(student)
            list_averages.append(average)
        return list_averages

    def get_only_id_list(self, average_list):
        id_list = []
        for average in average_list:
            id_list.append(average[1])
        return id_list
