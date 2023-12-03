from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship

from database import Base


# Таблица студентов
class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    class_number = Column(String, nullable=False)
    school_number = Column(Integer, nullable=False)
    phone_number = Column(String)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)

# Таблица студентов
class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    subject_name = Column(String, nullable=False)
    school_number = Column(Integer, nullable=False)
    phone_number = Column(String)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)

# Таблица карт пользователя
class Subject(Base):
    __tablename__ = 'subject'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    card_number = Column(Integer, nullable=False, unique=True)
    balance = Column(Float, default=0)
    exp_date = Column(Integer, nullable=False)
    card_name = Column(String)

    user_fk = relationship(Student, Teacher,  lazy='subquery')

# Таблица перевода - Transfers
class Transfer(Base):
    __tablename__ = 'transfers'
    transfer_id = Column(Integer, primary_key=True, autoincrement=True)
    card_from_id = Column(Integer, ForeignKey('cards.card_id'))
    card_to_id = Column(Integer, ForeignKey('cards.card_id'))
    amount = Column(Float)

    status = Column(Boolean, default=True)

    transaction_date = Column(DateTime)

    card_from_fk = relationship(UserCard, foreign_keys=[card_from_id], lazy='subquery')
    card_to_fk = relationship(UserCard, foreign_keys=[card_to_id], lazy='subquery')
