# !/usr/bin/env python
# coding=utf8

from models import Teacher, Student


def create_table_test():
    Teacher.create_table()
    Student.create_table()


def create_instance_test():
    t1 = Teacher.create(name='t1')
    t2 = Teacher.create(name='t2')
    s1 = Student.create(name='s1', teacher=t1)
    s2 = Student.create(name='s2', teacher=t1)
    s3 = Student.create(name='s3', teacher=t2)
    s4 = Student.create(name='s4', teacher=t2)


def query_test():
    t1 = Teacher.get(name='t1')
    print(t1)
    print(t1.students.count())
    for one in t1.students:
        print(one.name)


if __name__ == '__main__':
    query_test()
