import random

num = random.randint(0,10)
count = 0

while count < 5:
    
    guess = int(input("Guess the number between 0-10: "))

    if guess>num:
        print("Try Lower")
    elif guess<num:
        print("Try higher")
    else:
        print("Hoorah You Won")
        break
    
    count += 1

