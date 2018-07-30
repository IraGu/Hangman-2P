from hmclass import *


print("Welcome to hangman. Please input how many turns per player: ")

turn = input("Enter number of turns each player has to guess")

user1 = input("Please input name for player 1")
print(f"Welcome {user1}")

user2 = input("Please input name for player 2")
print(f"Welcome {user2}")

my_game = hangman(user1 = user1, user2 = user2, turn = turn)

word = my_game.wordlist()

print(word)
print(len(list(word)))
uword = my_game.unknown_word(word)
uword = list(uword)
print(f"{uword}")

rand = my_game.rand_roll()

flag = True
if rand <= 50:
    print(f"{user1.title()}goes first.")
else:
    print(f"{user2.title()} goes first.")
    flag = False

while True:
    if flag == True:
        guess = input(f"{user1} please enter guess")
        my_game.guess_compare(letter = guess,word = word, uword = uword)
        my_game.stored_guess_1(guess,user1)
        flag = False
        if "-" not in list(uword):
            print(f"{user1} wins")
            break
    else:
        guess = input(f"{user2} please enter guess")
        my_game.guess_compare(letter = guess,word = word,uword =uword)
        my_game.stored_guess_2(guess,user2)
        flag = True
        if "-" not in list(uword):
            print(f"{user2} wins")
            break
    





