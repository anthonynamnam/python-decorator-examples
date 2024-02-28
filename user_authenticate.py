def user_authenticate(func):
    def wrapper(user, *args, **kwargs):
        if user.login:
            return func(user, *args, **kwargs)
        else:
            raise PermissionError("User is not authenticated")
    return wrapper

@user_authenticate
def access_id(user):
    return "Personal Information: ID: 019238241"

# User Class
class User:
    def __init__(self, login):
        self.login = login


user_1 = User(login=True)
print(access_id(user_1))
print("--------------------")
user_2 = User(login=False)
print(access_id(user_2))