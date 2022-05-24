# class User:
#     pass
#
#
# user_1 = User()
# user_1.id = '001'
# user_1.username = 'Vishal'
#
# print(user_1.username)
# we havent created the attributes in the class but we have created the attribute outside class but still
# it works

# Using CONSTRUCTOR

# class User:
#
#     def __init__(self, user_id, username):
#
#         self.id = user_id
#         self.username = username
#         #print("New user being constructed...")
#
#
# user_1 = User('001', 'Vishal')
# user_2 = User('002', "Pappu")
#
# print(user_1.id, user_1.username)
# print(user_2.id, user_2.username)

# Giving default arguments to the constructor parameter

# class User:
#     def __init__(self,user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#
#
# user_1 = User('001', 'Vishal')
# print(user_1.followers)

# Here we have no need to give the followers has another parameter becoz followers always start from 0 for every account
# in case of instagram. So simply we define a variable name followers in __init__ with default value of zero.


# creating a method in the class

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', "Vishal")
user_2 = User('002', "Pappu")

user_2.follow(user_1)
print(user_1.followers)
print(user_2.following)




























