correct_pw = "mac"
count = 0

while True:
    input_pw = input("Enter Password:")

    if input_pw == correct_pw:
        print("Access Granted.")
        break
    else:
        count = count + 1
        print("Access Denied. Fail Count:", count)

        if count >= 3:
            print("System Locked.")
            break