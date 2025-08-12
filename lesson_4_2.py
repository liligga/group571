class User:
    # переменные класса
    total_users = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.total_users += 1

    @classmethod
    def get_total_users(cls):
        return cls.total_users

    @staticmethod
    def validate_email(email):
        return "@" in email

user_igor = User("Igor", "igor@gmail.com")
user_kurmanbek = User("Kurmanbek", "kurmanbek@<EMAIL>")
print(User.total_users)
print(User.get_total_users())
print(User.validate_email("igor#gmail.com"))