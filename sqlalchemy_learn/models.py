# coding=utf8

import sqlalchemy
from sqlalchemy import orm
from datetime import datetime as dt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# sqlalchemy.exc.OperationalError: (OperationalError) fe_sendauth: no password supplied
'''
db_connection = 'postgresql://phy:@localhost:5432/phy'
db_connection = 'postgresql://phy@localhost:5432/phy'
db_connection = 'postgresql://localhost:5432/phy'
'''

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

    @classmethod
    def drop_table(cls):
        # not working
        cls.__table__.drop(bind=engine)


'''
class Teacher(Person, Base):
    __tablename__ = 'teacher'
    subject = sqlalchemy.Column(sqlalchemy.String(50))
    students = orm.relation(
        'Student', backref="head_teacher", cascade="all")


class Student(Person, Base):
    __tablename__ = 'student'
    head_teacher_id = sqlalchemy.Column(
        sqlalchemy.INTEGER, sqlalchemy.ForeignKey('teacher.id'))
'''


'''
class Teacher(Person, Base):
    __tablename__ = 'teacher'
    subject = sqlalchemy.Column(sqlalchemy.String(50))
    students = orm.relation(
        # no cascade effect
        # 'Student', backref="head_teacher",
        'Student', backref="head_teacher", passive_deletes=True,
    )


class Student(Person, Base):
    __tablename__ = 'student'
    head_teacher_id = sqlalchemy.Column(
        sqlalchemy.INTEGER,
        # DETAIL:  Key (id)=(1) is still referenced from table "student".
        # sqlalchemy.ForeignKey('teacher.id'))
        sqlalchemy.ForeignKey('teacher.id', ondelete='CASCADE'))
'''


'''
class Teacher(Person, Base):
    __tablename__ = 'teacher'
    subject = sqlalchemy.Column(sqlalchemy.String(50))


class Student(Person, Base):
    __tablename__ = 'student'
    head_teacher_id = sqlalchemy.Column(
        sqlalchemy.INTEGER,
        # ondelete='CASCADE' has no effect
        # sqlalchemy.ForeignKey('teacher.id', ondelete='CASCADE'))
        sqlalchemy.ForeignKey('teacher.id')
    head_teacher = orm.relation(
        'Teacher',
        # backref=orm.backref('students'),  # no cascade effect
        backref=orm.backref('students', cascade='all'),
    )
'''


class Teacher(Person, Base):
    __tablename__ = 'teacher'
    subject = sqlalchemy.Column(sqlalchemy.String(50))
    students = orm.relation(
        'Student', backref="head_teacher", cascade='delete')


class Student(Person, Base):
    __tablename__ = 'student'
    head_teacher_id = sqlalchemy.Column(
        sqlalchemy.INTEGER,
        sqlalchemy.ForeignKey('teacher.id'))
Base.metadata.create_all(engine)  # must after class definition
