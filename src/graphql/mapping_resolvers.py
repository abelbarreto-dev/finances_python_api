from src.resolvers.user_resolver import create_user, delete_user, login_user, update_user

mapping_resolvers = {
    "loginUser": login_user,
    "createUser": create_user,
    "updateUser": update_user,
    "deleteUser": delete_user,
}
