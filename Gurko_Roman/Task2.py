class User():
    def __init__(self, age, name, user_type):
        self.age = age
        self.name = name
        self.user_type = user_type

    def access_database(self):
        if self.user_type == "superuser":
            return "Access granted!"
        return "Access denied!"


class SuperUser(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_type = "superuser"

