import random
def guess_the_number():
    number_to_guess=random.randint(1,50)
    while True:
        user_guess=int(input('Guess the number between 1 and 50:'))
        if user_guess==number_to_guess:
            print(f"wow! You gussed the number.The number was {number_to_guess}")
            break
        else:
            print(f'Your guess is wrong!The number was {number_to_guess} Try again.')
guess_the_number()








