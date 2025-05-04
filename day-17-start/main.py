

class User:
    _USER_COUNTER = 0

    def __init__(self, username):
        User._USER_COUNTER += 1
        self.user_id = self._USER_COUNTER
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        print(f"{self.username} is now following {user.username}.")
        user.followers += 1
        self.following += 1



user1 = User("Kate")
user2 = User("Jack")
user1.follow(user2)

print(user1.user_id)
print(user2.user_id)

print(user1.following)
print(user2.followers)