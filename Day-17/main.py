class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username= username
        self.followers = 0

user_1 = User("206027", "Junaid")
user_2 = User("1206027", "Junaid Khan")
print(user_1.id)
print(user_2.id)



'''
user_1 = User()
user_1.id="206027";
user_1.username= "Junaid"

print(user_1.username)

user_2 = User()
user_2.id="1206027";
user_2.name= "Junaid Khan"

print(user_2.name)
'''
