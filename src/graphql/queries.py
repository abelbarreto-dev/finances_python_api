from ariadne import QueryType

queries = QueryType()


@queries.field("health")
def resolve_health(_, info):
    return "ok"
