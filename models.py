# flask_graphene_mongo/models.py
from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField, IntField
)


class Department(Document):
    meta = {'collection': 'department'}
    name = StringField()


class Role(Document):
    meta = {'collection': 'role'}
    name = StringField()
    

class Group(Document):
    meta = {'collection': 'group'}
    code = StringField()
    name = StringField()


class Person(Document):
    meta = {'collection': 'person'}
    first_name = StringField()
    last_name = StringField()
    date_of_birth = DateTimeField(default=datetime.now)
    phone_number = StringField()
    hired_on = DateTimeField(default=datetime.now)
    department = ReferenceField(Department)
    role = ReferenceField(Role)


class Case(Document):
    meta = {'collection': 'cases'}
    number = IntField()
    stage = StringField()
    member = ReferenceField(Person)
    analyst = ReferenceField(Person)
    group = ReferenceField(Group)
