from graphene import ObjectType, String, Schema, List, Int


class QueryData(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()
    info = String()
    stuff = List(String, idx=Int(default_value=0))

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


schema = Schema(query=QueryData)
