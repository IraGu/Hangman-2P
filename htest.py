def guess_test(user):
    while True:
        letter = input(">>> ")
        if letter.isalpha() and len(letter) == 1:
            print(f"{user.title()} has guessed the letter: {letter.lower()}!")
            return(letter)
        else:
            print('Please only enter a single letter!')
            continue


def turn_test():
    while True:
        turn = input(">>> ")
        if turn.isnumeric() and int(turn) <= 10:
            print(f"Each player will have {turn} guesses.")
            return(turn)
        elif turn.isnumeric() and int(turn) > 10:
            print('Maximum turns allowed per user is 10!')
            continue
        else:
            print("Please enter an integer!")
            continue




