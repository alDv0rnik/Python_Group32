class User:

    def __init__(self, age, name, user_type):
        self.age = age
        self.name = name
        self.user_type = user_type

    def access_database(self):
        if self.user_type == "superuser":
            print("access granted")
        else:
            print("access denied")

class SuperUser(User):
    def __init__(self, user_type):
        self.user_type = user_type

    def access_database(self):
        if self.user_type == "superuser":
            print(f"You are welcome")
        else:
            print(f"Need to gain access")


user = User(age=35, name="Sasha", user_type="superuser")
user.access_database()
superUser = SuperUser(user_type="superuser")
superUser.access_database()
