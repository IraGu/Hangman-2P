from hmclass import *
from htest import *


print("Welcome to hangman. Please input how many turns per player: ")
turn = turn_test()

user1 = input("Please input name for player 1: ")
user1 = user1.title()
print(f"Welcome {user1}")

user2 = input("Please input name for player 2: ")
user2 = user2.title()
print(f"Welcome {user2}")

my_game = hangman(user1 = user1, user2 = user2, turn = turn)

word = my_game.wordlist()

uword = my_game.unknown_word(word)
uword = list(uword)
print(f"{uword}")

rand = my_game.rand_roll()

flag = True
trigger1, trigger2 = False, False

if rand <= 50:
    print(f"{user1} goes first.")
else:
    print(f"{user2} goes first.")
    flag = False

while True:

    if trigger1 == True and trigger2 == True:
        print("Both Players Loses!")
        break
    if flag == True:
        flag = False
        pturn1 = my_game.turn_count1()
        if pturn1 == 0:
            print(f"{user1} is out of guesses!")
            trigger1 = True
        else:
            print(f"{user1} please enter guess: ")
            guess = guess_test(user1)
            my_game.guess_compare(letter = guess,word = word, uword = uword)
            my_game.stored_guess_1(guess,user1)
        if "-" not in list(uword):
            print(f"{user1} wins!")
            break
    else:
        flag = True
        pturn2 = my_game.turn_count2()
        if pturn2 == 0:
            print(f"{user2} is out of guesses!")
            trigger2 = True
        else:
            print(f"{user2} please enter guess: ")
            guess = guess_test(user2)
            my_game.guess_compare(letter = guess,word = word,uword =uword)
            my_game.stored_guess_2(guess,user2)
        if "-" not in list(uword):
            print(f"{user2} wins!")
            break
    
        
    





