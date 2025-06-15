from app.models import Group, Student, Teacher, Subject, Grade, engine
from sqlalchemy.orm import Session
from faker import Faker
import random

fake = Faker("en_US")

subjects_names = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology",
    "History",
    "English"
]

with Session(engine) as session:
    # Створюємо групи
    groups = []
    for name in ["Group A", "Group B", "Group C"]:
        group = Group(name=name)
        session.add(group)
        groups.append(group)

    # Створюємо викладачів
    teachers = []
    for _ in range(5):
        teacher = Teacher(full_name=fake.name())
        session.add(teacher)
        teachers.append(teacher)

    # Створюємо предмети
    subject_names = ["Mathematics", "Physics", "Chemistry", "Biology", "History", "English"]
    subjects = []
    for name in subject_names:
        subject = Subject(name=name, teacher=random.choice(teachers))
        session.add(subject)
        subjects.append(subject)

    # Створюємо студентів
    students = []
    for _ in range(30):
        student = Student(
            full_name=fake.name(),
            group=random.choice(groups)
        )
        session.add(student)
        students.append(student)

    session.commit()

    # Створюємо оцінки
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(5, 20)):
                grade = Grade(
                    student=student,
                    subject=subject,
                    grade=random.randint(1, 12),
                    date_received=fake.date()
                )
                session.add(grade)
    session.commit()