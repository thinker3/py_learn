#coding=utf8

import sqlalchemy
from sqlalchemy import orm
from datetime import datetime as dt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_connection = 'postgresql:///phy'
engine = create_engine(db_connection)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()


class Person(object):
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(50))
    create_time = sqlalchemy.Column(sqlalchemy.DateTime, default=dt.now())
    modify_time = sqlalchemy.Column(sqlalchemy.DateTime, default=dt.now())

    def __repr__(self):
        return self.name

'''
class TeacherStudent(Base):
    __tablename__ = 'teacher_student'
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    teacher_id = sqlalchemy.Column(
        sqlalchemy.INTEGER,
        sqlalchemy.ForeignKey('teacher.id'),
    )
    student_id = sqlalchemy.Column(
        sqlalchemy.INTEGER,
        sqlalchemy.ForeignKey('student.id'),
    )
'''

teacher_student = sqlalchemy.Table('teacher_student', Base.metadata,
    sqlalchemy.Column(
        'teacher_id',
        sqlalchemy.INTEGER,
        sqlalchemy.ForeignKey('teacher.id'),
    ),
    sqlalchemy.Column(
        'student_id',
        sqlalchemy.INTEGER,
        sqlalchemy.ForeignKey('student.id'),
    )
)


class Teacher(Person, Base):
    __tablename__ = 'teacher'
    subject = sqlalchemy.Column(sqlalchemy.String(50))
    students = orm.relation(
        'Student',
        secondary=teacher_student,
        #backref="teachers",
        backref=orm.backref("teachers", cascade='all'),
    )

    def __repr__(self):
        return '%s_%s' % (self.name, self.subject)


class Student(Person, Base):
    __tablename__ = 'student'


def insert_test():
    tom = Teacher(name='Tom', subject='Physics')
    jack = Teacher(name='Jack', subject='Math')
    session.add(tom)
    session.add(jack)
    lucy = Student(name='Lucy')
    lily = Student(name='Lily')
    session.add(lucy)
    session.add(lily)
    session.commit()
    print tom.students
    print lucy.teachers
    tom.students.append(lucy)
    jack.students.append(lily)
    jack.students.append(lucy)
    session.commit()  # needed
    print tom.students
    print lucy.teachers


def query_test():
    #first = session.query(Student).filter(Student.name == 'Lucy').first()
    first = session.query(Student).filter_by(name='Lucy').first()
    print first.name
    print first.teachers
    #math_teacher = session.query(Teacher).filter(
    #    Teacher.subject == 'Math').first()
    math_teacher = session.query(Teacher).filter_by(subject='Math').first()
    print math_teacher.name
    print math_teacher.students


def update_test():
    # todo
    #first = session.query(Student).first()
    #first.teachers.update(subject='English')

    # TypeError: update() got an unexpected keyword argument 'subject'
    #session.query(Teacher).update(subject='English')
    session.query(Teacher).update(dict(subject='English'))
    session.commit()
    print session.query(Teacher).all()


def delete_test():
    first = session.query(Teacher).get(1)
    print first.name
    session.delete(first)
    session.commit()
    # todo
    #session.query(Student).delete()
    session.commit()
    print session.query(Teacher).all()
    print session.query(Student).all()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    insert_test()
    query_test()
    update_test()
    #delete_test()
    session.execute('drop table student, teacher, teacher_student;')
    session.commit()
