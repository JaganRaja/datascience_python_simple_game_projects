import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess the number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too Low")
        elif guess > random_number:
            print("Sorry, guess again. Too High")

    print(
        f"congrats! you have guessed the coreect number {random_number} correctly!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(
            f"Is {guess} is too high (H), too Low (L), or COrrect (C) ?? ").lower()
        if feedback == 'h':
            high = guess - 1

        elif feedback == 'l':
            low = guess + 1

    print(f"Computer  guessed your number, {guess}, correctly ")


# guess(10)

computer_guess(10)
