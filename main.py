# this project is about guessing the secret no to the users which is already been stored
# and asking them to guess it in 3 trial.

secret_number = 9

guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("guess: "))
    guess_count += 1
    if guess == secret_number:
        print("you won!")
        break

else:
    print("sorry you guessed all wrong!")

