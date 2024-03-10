from src.domain.entities import Student, Discipline, Grade


class StudentRepository:
    def __init__(self):
        self.__list_of_students = [Student(11, 'Alice'), Student(13, 'Ana'), Student(14, 'Kate'), Student(17, 'Jason'),
                                   Student(21, 'Alex'), Student(22, 'Mia'), Student(24, 'Mary'), Student(26, 'Lexie'),
                                   Student(29, 'Louis'), Student(30, 'Charles'), Student(33, 'Tim'),
                                   Student(38, 'Noah'), Student(41, 'Chris'), Student(45, 'Harry'), Student(47, 'Tom')]
        self.__list_of_student_ids = []

    def list_of_ids(self):
        for student in self.__list_of_students:
            self.__list_of_student_ids.append(Student.get_id(student))
        return self.__list_of_student_ids

    def add_student(self, student):
        self.__list_of_students.append(student)
        self.__list_of_student_ids.append(Student.get_id(student))

    def list_students(self):
        return self.__list_of_students

    def update_student(self, old_id, new_id, new_name):
        for student in self.__list_of_students:
            if Student.get_id(student) == old_id:
                student.set_id(new_id)
                student.set_name(new_name)

    def remove_student(self, student_id):
        for student in self.__list_of_students:
            if Student.get_id(student) == student_id:
                self.__list_of_students.remove(student)

    def search_student_by_id(self, student_id):
        students_found = []
        for student in self.__list_of_students:
            if Student.get_id(student) == student_id:
                students_found.append(student)
        return students_found

    def search_student_by_name(self, name):
        students_found = []
        for student in self.__list_of_students:
            student_name = Student.get_name(student)
            if name.lower() in student_name.lower():
                students_found.append(student)
        return students_found

    def search_one_student_by_id(self, student_id):
        for student in self.__list_of_students:
            if Student.get_id(student) == student_id:
                return Student.get_name(student)


class DisciplineRepository:
    def __init__(self):
        self.__list_of_disciplines = [Discipline(101, 'Algebra'), Discipline(102, 'Analysis'), Discipline(103, 'PE'),
                                      Discipline(104, 'Geography'), Discipline(105, 'Biology'),
                                      Discipline(106, 'Physics'), Discipline(107, 'Computer Science'),
                                      Discipline(108, 'History'), Discipline(109, 'Foreign Languages')]
        self.__list_of_discipline_ids = []

    def list_of_discipline_ids(self):
        for discipline in self.__list_of_disciplines:
            self.__list_of_discipline_ids.append(Discipline.get_id(discipline))
        return self.__list_of_discipline_ids

    def add_discipline(self, discipline):
        self.__list_of_disciplines.append(discipline)
        self.__list_of_discipline_ids.append(Discipline.get_id(discipline))

    def list_disciplines(self):
        return self.__list_of_disciplines

    def update_discipline(self, old_id, new_id, new_name):
        for discipline in self.__list_of_disciplines:
            if Discipline.get_id(discipline) == old_id:
                discipline.set_id(new_id)
                discipline.set_name(new_name)

    def remove_discipline(self, discipline_id):
        for discipline in self.__list_of_disciplines:
            if Discipline.get_id(discipline) == discipline_id:
                self.__list_of_disciplines.remove(discipline)

    def search_discipline_by_name(self, name):
        disciplines_found = []
        for discipline in self.__list_of_disciplines:
            discipline_name = Discipline.get_name(discipline)
            if name.lower() in discipline_name.lower():
                disciplines_found.append(discipline)
        return disciplines_found

    def search_discipline_by_id(self, discipline_id):
        disciplines_found = []
        for discipline in self.__list_of_disciplines:
            if Discipline.get_id(discipline) == discipline_id:
                disciplines_found.append(discipline)
        return disciplines_found


class GradeRepository:

    def __init__(self):
        self.__list_of_grades = [Grade(11, 103, [2]), Grade(47, 101, [9]), Grade(11, 109, [10, 8]),
                                 Grade(30, 102, [3]), Grade(38, 105, [7, 10]), Grade(26, 103, [8, 9]),
                                 Grade(29, 107, [9.25, 8.75]), Grade(30, 101, [7, 1])]
        self.__list_of_student_ids = []
        self.__list_of_discipline_ids = []

    def get_list_of_student_ids(self):
        for grade in self.__list_of_grades:
            if Grade.get_student_id(grade) not in self.__list_of_student_ids:
                self.__list_of_student_ids.append(Grade.get_student_id(grade))
        return self.__list_of_student_ids

    def get_list_of_discipline_ids(self):
        for grade in self.__list_of_grades:
            self.__list_of_discipline_ids.append(Grade.get_discipline_id(grade))
        return self.__list_of_discipline_ids

    def list_grades(self):
        return self.__list_of_grades

    def remove_grade_for_student(self, student_id):
        for grade in self.__list_of_grades:
            if Grade.get_student_id(grade) == student_id:
                self.__list_of_grades.remove(grade)

    def remove_grade_for_discipline(self, discipline_id):
        for grade in self.__list_of_grades:
            if Grade.get_discipline_id(grade) == discipline_id:
                self.__list_of_grades.remove(grade)

    def search_student_grades(self, student_id):
        grades_found = []
        for grade in self.__list_of_grades:
            if Grade.get_student_id(grade) == student_id:
                grades_found.append(grade)
        return grades_found

    def search_discipline_grades(self, discipline_id):
        grades_found = []
        for grade in self.__list_of_grades:
            if Grade.get_discipline_id(grade) == discipline_id:
                grades_found.append(grade)
        return grades_found

    def add_grade(self, student_id, discipline_id, grade_value):
        found = 0
        for existing_grade in self.__list_of_grades:
            if student_id == Grade.get_student_id(existing_grade) and discipline_id ==\
                    Grade.get_discipline_id(existing_grade):
                grade = Grade(student_id, discipline_id, grade_value)
                Grade.get_grade_value(existing_grade).append(Grade.get_grade_value(grade))
                found = 1
        if found == 0:
            new_grade = []
            grade_value = int(grade_value)
            new_grade.append(grade_value)
            grade = Grade(student_id, discipline_id, new_grade)
            self.__list_of_grades.append(grade)
            self.__list_of_student_ids.append(Grade.get_student_id(grade))
            self.__list_of_discipline_ids.append(Grade.get_discipline_id(grade))

    def average_grade(self, grade):
        grade_sum = 0
        number = 0
        for i in range(len(grade)):
            grade_sum = grade_sum + grade[i]
            number += 1
        return float(grade_sum // number)

    def get_fails_student(self, student_id):
        fail = 0
        for student in self.__list_of_grades:
            if Grade.get_student_id(student) == student_id:
                average_at_discipline = self.average_grade(Grade.get_grade_value(student))
                if average_at_discipline < 5:
                    fail += 1
        return fail

    def get_average_student(self, student_id):
        current_student = [0] * 2
        total_average = 0
        number_of_disciplines = 0
        for student in self.__list_of_grades:
            if Grade.get_student_id(student) == student_id:
                average_at_discipline = self.average_grade(Grade.get_grade_value(student))
                total_average += average_at_discipline
                number_of_disciplines += 1
        total_average = total_average // number_of_disciplines
        current_student[1] = student_id
        current_student[0] = total_average
        return current_student

    def get_average_discipline(self, discipline_id):
        current_discipline = [0] * 2
        total_average = 0
        for student in self.__list_of_grades:
            if Grade.get_discipline_id(student) == discipline_id:
                average_at_discipline = self.average_grade(Grade.get_grade_value(student))
                total_average += average_at_discipline
        current_discipline[1] = discipline_id
        current_discipline[0] = total_average
        return current_discipline
