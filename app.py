from pathlib import Path

from ariadne import gql, make_executable_schema
from ariadne.asgi import GraphQL
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from src.auth.auth_access import auth_login_user
from src.graphql.mutations import mutations
from src.graphql.queries import queries

all_queries = [queries]
all_mutations = [mutations]

ROOT_DIR = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT_DIR / "src" / "graphql" / "schema.graphql"
type_defs = gql(SCHEMA_PATH.read_text(encoding="utf-8"))

schema = make_executable_schema(type_defs, *all_queries, *all_mutations)

app = FastAPI(title="Finances GraphQL API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/graphql", GraphQL(schema, debug=True))


app.post("/login")


async def login(request: Request):
    return auth_login_user(request)
