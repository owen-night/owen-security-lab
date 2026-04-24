allowed_users = ["elon", "tony", "peter"]
correct_pw = "001001"

user_id = input("Enter ID:")
user_pw = input("Enter PW:")

if user_id in allowed_users and user_pw == correct_pw:
    print(f"Access Granted. System online, {user_id}.")
else:
    print("Access Denied. Intruder Alert.")