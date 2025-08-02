class User():
    def __init__(self, username, email):
        self.username = username
        self.email = email


class AdminUser(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role
        self. is_admin = True


my_admin = AdminUser('admin123', 'admin@admin.com', 'Administrator')
print(my_admin)
print(type(my_admin))
print(isinstance(my_admin, AdminUser))
print(isinstance(my_admin, User))
print(isinstance(my_admin, object))

print(my_admin.__dict__)

my_user = User('bob234', 'bob@bob.com')

print(my_user)

print(User.__subclasses__())
