from graphene import ObjectType, String, Schema, List, Int, Field, Boolean, Mutation
from uuid import uuid4


def resolve_full_name(person, info):
    return f"{person.first_name} {person.last_name}"


class CreatePerson(Mutation):
    class Arguments:
        first = String()
        last = String()

    ok = Boolean()
    person = Field(lambda: Person)

    def mutate(root, info, first, last):
        person = Person(first=first, last=last)
        ok = True
        return CreatePerson(person=person, ok=ok)


class MyMutations(ObjectType):
    create_person = CreatePerson.Field()


class Person(ObjectType):
    first_name = String()
    last_name = String()
    id = String()
    full_name = String(resolver=resolve_full_name)

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.id = str(uuid4())


class QueryData(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()
    info = String()
    stuff = List(String, idx=Int(default_value=0))
    person = Field(Person)

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


schema = Schema(query=QueryData, mutation=MyMutations)
