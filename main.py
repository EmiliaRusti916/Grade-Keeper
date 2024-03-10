from src.repository.repository import StudentRepository, DisciplineRepository, GradeRepository
from src.services.student_service import StudentService, DisciplineService, GradeService
from src.ui.console import Console

student_repository = StudentRepository()
discipline_repository = DisciplineRepository()
grade_repository = GradeRepository()
student_service = StudentService(student_repository)
discipline_service = DisciplineService(discipline_repository)
grade_service = GradeService(grade_repository)
console = Console(student_service, discipline_service, grade_service)
console.menu()
