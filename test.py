import random
def guess_num():
    random_num = random.randint(0, 100)

    while True:
        user_input = input("Guess the number [q]: ").strip()

        if user_input.lower() == 'q':
            break
        user_input = int(user_input)

        if user_input > random_num:
            print("Guess is too high try again. ")
        elif    user_input < random_num:
            print("Guess is too low try again. ")

        else:
            print("You have guessed the correct number, Congratulations")
            break
guess_num()