# encoding: utf-8
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from mongoengine import connect

# You can connect to a real mongo server instance by your own.
connect('test', host='localhost', alias='default')

app = Flask(__name__)
app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
