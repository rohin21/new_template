from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.applications import Starlette

import graphene

app = Starlette()

class CreateNewPost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
    ok = graphene.Boolean()

class PostMutations(graphene.ObjectType):
    create_new_post = CreateNewPost.Field()



app.mount("/graphql",GraphQLApp(schema=graphene.Schema(),on_get=make_graphiql_handler()))

