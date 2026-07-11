from ariadne import MutationType

from src.graphql.mapping_resolvers import mapping_resolvers

mutations = MutationType()


@mutations.field("createUser")
async def resolve_create_user(_, info, user):
    return await mapping_resolvers["createUser"](user)


@mutations.field("updateUser")
async def resolve_update_user(_, info, user):
    return await mapping_resolvers["updateUser"](user)


@mutations.field("deleteUser")
async def resolve_delete_user(_, info, id):
    return await mapping_resolvers["deleteUser"](id)
