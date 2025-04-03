import pytest
from sqlalchemy.orm import sessionmaker
from database import engine, Student

# Создание сессии для тестов
Session = sessionmaker(bind=engine)


@pytest.fixture(scope='function')
def session():
    """Создание сессии для тестов."""
    session = Session()
    yield session
    session.rollback()  # Откат изменений после теста
    session.close()


@pytest.fixture(scope='function')
def add_student(session):
    """Фикстура для добавления студента."""
    student = Student(name='1616')
    session.add(student)
    session.commit()
    yield student
    session.delete(student)
    session.commit()


def test_add_student(session):
    """Тест на добавление студента."""
    # Убедимся, что студента с таким именем нет
    existing_student = session.query(Student).filter_by(name='1616').first()
    if existing_student:
        session.delete(existing_student)
        session.commit()

    student = Student(name='1616')
    session.add(student)
    session.commit()

    assert student.id is not None
    assert session.query(Student).filter_by(name='1616').first() is not None


def test_update_student(add_student, session):
    """Тест на изменение студента."""
    add_student.name = '1617'
    session.commit()

    updated_student = session.query(Student).filter_by(id=add_student.id).one()
    assert updated_student.name == '1617'


def test_delete_student(add_student, session):
    """Тест на удаление студента."""
    session.delete(add_student)
    session.commit()

    assert session.query(Student).filter_by(id=add_student.id).first() is None
