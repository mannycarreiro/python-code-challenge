# ==================================================
# DAY 17 = OOP (OBJECT ORIENTED PROGRAMMING <START>
# ==================================================

# class User:
#     pass
#
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "manny"
#
# print(user_1.username)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# CONSTRUCTOR
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# class User:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0  # SET DEFAULT VALUE FOR ATTRIBUTE
#
#
# user_1 = User("001", "Manny")
# print(user_1.id)
# print(user_1.username)
# print(user_1.followers)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ADD METHOD TO CLASS
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# WHEN A FUNCTION IS ATTACHED TO AN OBJECT, IT IS CALLED A METHOD!!

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # SET DEFAULT VALUE FOR ATTRIBUTE
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Manny")
user_2 = User("002", "Jessica")

user_1.follow(user_2)
