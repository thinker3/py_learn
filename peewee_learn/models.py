# !/usr/bin/env python
# coding=utf8

import peewee

db = peewee.SqliteDatabase('school.db')


class Teacher(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = db


class Student(peewee.Model):
    name = peewee.CharField()
    teacher = peewee.ForeignKeyField(Teacher, related_name='students')

    class Meta:
        database = db
