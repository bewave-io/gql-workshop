# flask_graphene_mongo/database.py
from mongoengine import connect

from models import Department, Person, Role, Group, Cases

# You can connect to a real mongo server instance by your own.
connect('revelio', host='localhost', alias='default')


def init_db():
    # Create the fixtures
    engineering = Department(name='Invalidité')
    engineering.save()

    manager = Role(name='Gestionnaire')
    manager.save()

    engineer = Role(name='Analyste')
    engineer.save()

    peter = Person(first_name='Peter', last_name='Parker',
                   department=engineering, role=engineer)
    peter.save()

    roy = Person(first_name='Bruce', last_name='Banner',
                 department=engineering, role=engineer)
    roy.save()

    tracy = Person(first_name='Tony', last_name='Stark',
                   department=engineering, role=manager)
    tracy.save()

    cases = Ca


init_db()
