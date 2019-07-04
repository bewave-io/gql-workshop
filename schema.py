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


class MyMutations(ObjectType):
    update_person = UpdatePerson.Field()


class QueryData(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()
    info = String()
    stuff = List(String, idx=Int(default_value=0))
    #person = Field(Person)
    node = Node.Field()
    all_persons = MongoengineConnectionField(Person)
    all_role = MongoengineConnectionField(Role)
    role = Field(Role)

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'

    def resolve_info(root, info):
        return info.schema

    def resolve_stuff(root, info, idx):
        return [["1", "2", "3"][idx]]

    def resolve_person(root, info):
        return Person("Jo", "Bin")


schema = Schema(query=QueryData, mutation=MyMutations,
                types=[Department, Person, Role])
