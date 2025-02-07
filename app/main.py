from fastapi import FastAPI
from app.graphql_schema import routes, graphql_schema
from strawberry.fastapi import GraphQLRouter


app = FastAPI()

graphql_app = GraphQLRouter(graphql_schema)
app.include_router(graphql_app, prefix="/graphql")
app.include_router(routes.router)
@app.get("/")
def root():
    return {"message": "fastapi + postgresql + docker run successfully on port 8000"}





