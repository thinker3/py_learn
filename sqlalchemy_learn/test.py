# coding=utf8
# from datetime import datetime
from models import Teacher, Student, session
from sqlalchemy.orm.session import Session
assert isinstance(session, Session)


def insert_test():
    tom = Teacher(name='Tom', subject='Physics')
    session.add(tom)
    session.commit()
    lucy = Student(name='Lucy', head_teacher_id=tom.id)
    session.add(lucy)
    session.commit()


def query_test():
    first = session.query(Student).first()
    print first.name
    print first.head_teacher.id
    print first.head_teacher.subject


def update_test():
    tom = session.query(Teacher).get(1)  # not get(id=1)
    tom.subject = 'Math'
    session.commit()


def delete_test():
    tom = session.query(Teacher).get(1)
    print tom.students
    session.delete(tom)
    # lucy = session.query(Student).get(1)
    # session.delete(lucy)
    session.commit()
    print session.query(Teacher).all()
    print session.query(Student).all()


if __name__ == '__main__':
    insert_test()
    query_test()
    update_test()
    query_test()
    delete_test()
    session.execute('drop table student, teacher;')  # need to commit
    # Student.drop_table()  # not working, make this file running forever!!!
    session.commit()
