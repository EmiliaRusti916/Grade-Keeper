Add = 1
Remove = 2
Update = 3
List = 4
Grade = 5
Search = 6
GradeSearch = 7
Statistic = 8
StudentMagicNumber = 00
DisciplineMagicNumber = 11
GradeMagicNumber = 10


def print_options():
    print('\nChoose an option.')
    print('1.Add a student or discipline.')
    print('2.Remove a student or discipline.')
    print('3.Update a student or discipline.')
    print('4.List all students or all disciplines or all grades.')
    print('5.Grade student.')
    print('6.Search a student or a discipline.')
    print('7.Search the grades for a student by ID.')
    print('8. Statistic')
    print('Anything else to exit.\n')


class Console:
    def __init__(self, students_service, disciplines_service, grade_service):
        self.__student_service = students_service
        self.__discipline_service = disciplines_service
        self.__grade_service = grade_service

    def menu(self):
        while True:
            print_options()
            option = int(input('Enter number of option: '))
            if option == Add:
                try:
                    print('Enter\n00 for Student\n11 for Discipline')
                    case = int(input())
                    if case == StudentMagicNumber:
                        student_id = input('Enter ID: ')
                        name = input('Enter student name: ')
                        if self.__student_service.add_student(student_id, name) is False:
                            print('Invalid input. Please enter positive integer numbers for ID '
                                  'that have not been entered before.')
                    elif case == DisciplineMagicNumber:
                        discipline_id = input('Enter ID: ')
                        name = input('Enter discipline name: ')
                        if self.__discipline_service.add_discipline(discipline_id, name) is False:
                            print('Invalid input. Please enter positive integer numbers for ID '
                                  'that have not been entered before.')
                    else:
                        raise ValueError('Cannot do this command')
                except ValueError:
                    print('Cannot do this command.')

            elif option == Remove:
                try:
                    print('Enter\n00 for Student\n11 for Discipline')
                    case = int(input())
                    if case == StudentMagicNumber:
                        student_id = input('Enter ID: ')
                        if self.__student_service.remove_students(student_id) is False:
                            print('No student to delete or invalid ID')
                        else:
                            self.__grade_service.remove_grades_for_student(student_id)
                    elif case == DisciplineMagicNumber:
                        discipline_id = input('Enter ID: ')
                        self.__discipline_service.remove_disciplines(discipline_id)
                        if self.__grade_service.remove_grades_for_discipline(discipline_id) is False:
                            print('No discipline to delete or invalid ID')
                    else:
                        raise ValueError('Cannot do this command')
                except ValueError:
                    print('Cannot do this command.')

            elif option == Update:
                try:
                    print('Enter\n00 for Student\n11 for Discipline')
                    case = int(input())
                    if case == StudentMagicNumber:
                        student_id = input('Enter the ID of the student you want to update: ')
                        new_id = input('Enter the new student ID: ')
                        new_name = input('Enter the new student name: ')
                        if self.__student_service.update_students(student_id, new_id, new_name) is False:
                            print('No student to update or duplicate/invalid ID')
                    elif case == DisciplineMagicNumber:
                        discipline_id = input('Enter the ID of the discipline you want to update: ')
                        new_id = input('Enter the new discipline ID: ')
                        new_name = input('Enter the new discipline name: ')
                        if self.__discipline_service.update_disciplines(discipline_id, new_id, new_name) is False:
                            print('No discipline to update or duplicate/invalid ID')
                    else:
                        raise ValueError('Cannot do this command')
                except ValueError:
                    print('Cannot do this command.')

            elif option == List:
                try:
                    print('Enter\n00 for Student\n11 for Discipline\n10 for Grades')
                    case = int(input())
                    if case == StudentMagicNumber:
                        students_list = self.__student_service.list_all_students()
                        for student in students_list:
                            print(str(student.get_id()) + ' ' + student.get_name())
                    elif case == DisciplineMagicNumber:
                        disciplines_list = self.__discipline_service.list_all_disciplines()
                        for discipline in disciplines_list:
                            print(str(discipline.get_id()) + ' ' + discipline.get_name())
                    elif case == GradeMagicNumber:
                        grades_list = self.__grade_service.list_all_grades()
                        for discipline in grades_list:
                            print(str(discipline.get_student_id()) + ' ' + str(
                                discipline.get_discipline_id()) + ' ' + str(discipline.get_grade_value()))
                    else:
                        raise ValueError('Cannot do this command')
                except ValueError:
                    print('Cannot do this command.')

            elif option == Grade:
                    student_id = input('Enter student ID: ')
                    discipline_id = input('Enter discipline ID: ')
                    grade = int(input('Enter grade value from 1 to 10: '))
                    if self.__grade_service.grade_student(student_id, discipline_id, grade) is False:
                        print('Invalid input. Please enter positive numbers')

            elif option == Search:
                try:
                    print('Enter\n00 for Student\n11 for Discipline')
                    case = int(input())
                    if case == StudentMagicNumber:
                        parameter = input("Enter student's ID or Name: ")
                        if parameter.isnumeric() is True:
                            parameter = int(parameter)
                        self.__student_service.search_students(parameter)
                    elif case == DisciplineMagicNumber:
                        parameter = input("Enter student's ID or Name: ")
                        if parameter.isnumeric() is True:
                            parameter = int(parameter)
                        self.__discipline_service.search_disciplines(parameter)
                    else:
                        raise ValueError('Cannot do')
                except ValueError:
                    print('Cannot do this command.')
            elif option == GradeSearch:
                student_id = input("Enter the student's id: ")
                grades_found = self.__grade_service.display_student_grades(student_id)
                for grade in grades_found:
                    print('At discipline ' + str(grade.get_discipline_id()) + ' student ' +
                          str(grade.get_student_id()) + ' has the grades: ' + str(grade.get_grade_value()))
            elif option == Statistic:
                print('\nA.All students failing at one or more disciplines.')
                print('\nB.Students with the best school situation, sorted in descending order'
                      ' of their aggregated average.')
                no, one, more = self.__grade_service.fail_statistic(0, 0, 0)
                list_average = self.__grade_service.student_average_statistic()
                print('\n----- Statistic A. -----')
                print('Students that have not failed any discipline: ' + str(no))
                print('Students that have failed one discipline: ' + str(one))
                print('Students that have failed more than one discipline: ' + str(more))
                print('\n----- Statistic B. -----')
                list_average.sort(reverse=True)
                list_id_average = self.__grade_service.get_only_id_list(list_average)
                list_name_average = self.__student_service.get_only_name_list(list_id_average)
                print(list_average)
                print(list_name_average)
            else:
                break
