from graphene import ObjectType, String, Schema, List, Int, Field, Boolean, Mutation
from uuid import uuid4
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Department as DepartmentModel
from models import Person as PersonModel
from models import Role as RoleModel


class Department(MongoengineObjectType):

    class Meta:
        model = DepartmentModel
        interfaces = (Node,)


class Role(MongoengineObjectType):

    class Meta:
        model = RoleModel
        interfaces = (Node,)


class Person(MongoengineObjectType):

    class Meta:
        model = PersonModel
        interfaces = (Node,)


class UpdatePerson(Mutation):
    class Arguments:
        first = String()
        last = String()
        id = String()

    person = Field(lambda: Person)

    def mutate(root, info, first, last=None, id=None):
        person = PersonModel(id=id, first_name=first, last_name=last)
        person.save()
        return UpdatePerson(person=person)


class RemovePerson(Mutation):
    class Arguments:
        id = String()

    person = Field(lambda: Person)

    def mutate(root, info, id):
        person = PersonModel(id=id)
        person.delete()
        return RemovePerson(person=person)


class Mutation(ObjectType):
    update_person = UpdatePerson.Field()
    remove_person = RemovePerson.Field()


class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    people = MongoengineConnectionField(Person)
    roles = MongoengineConnectionField(Role)


schema = Schema(query=Query, mutation=Mutation,
                types=[Department, Person, Role])
