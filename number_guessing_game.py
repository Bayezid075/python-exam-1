import random
random_number = random.randint(1,100)
attempt = 0
while True:
    user_number = input("Your Guessed Number: ")
    valid_number = user_number.isnumeric()
    if not valid_number :
        print(f"Enter a valid Number. --{user_number}-- is not a valid number!!") #error handler
        continue
    else:
        user_number = int(user_number)
    attempt += 1
    if user_number > 100 :
        print("Give the number below 100!")
    elif user_number == random_number :
        print(f"Excellent!! You are guessed right number in {attempt} attempts!!")
        break
    elif user_number > random_number:
        print("Your guessed number is high!!!")
    elif user_number < random_number :
        print("Your guessed number is low !!!")
    else:
        continue
