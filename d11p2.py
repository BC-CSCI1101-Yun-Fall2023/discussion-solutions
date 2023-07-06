def read_user(prompt, followers):
    user = input(prompt).lower()
    if user not in followers:
        print(f"Note: adding user {user}")
        followers[user] = []
    return user

def follow(followers):
    user = read_user("Enter user to follow: ", followers)
    follower = read_user("Enter follower: ", followers)
        
    if user == follower:
        print(f"Error, user can't follow themselves!")
        return
    
    if follower in followers[user]:
        print(f"Error, {follower} already following {user}!")
        return
    
    followers[user].append(follower)

def print_user(followers, user):
    if len(followers[user]) == 0:
        print(f"{user} has no followers")
    else:
        print(f"{user}'s followers: ", end="")
        for follower in followers[user]:
            print(f"{follower} ", end="")
        print()

def show(followers):
    if len(followers) == 0:
        print("No users!")
    for user in sorted(followers):
        print_user(followers, user)

print("Social Media Tracker")
print("Commands: follow, show, quit")
print()

followers = {}

command = input("What next? ").lower()
while command != "quit":
    if command == "follow":
        follow(followers)
    elif command == "show":
        show(followers)
    else:
        print("Invalid command")
    print()
    command = input("What next? ").lower()
