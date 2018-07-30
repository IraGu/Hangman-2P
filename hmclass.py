from random import randint

class hangman():

    def __init__(self,user1,user2,turn):
        self.user1 = user1
        self.user2 = 4
        self.stored_list1 = []
        self.stored_list2 = []
        self.guess1 = []
        self.guess2 = []
        self.player_turn1 = int(turn)
        self.player_turn2 = int(turn)
        

    def rand_roll(self):
        int = randint(1,101)
        return int

    
    def wordlist(self):
        wlist = ['guess','time','random']
        int = randint(0,len(wlist) - 1)
        s = wlist[int]
        return list(s)

    
    def unknown_word(self,word):
        return ("-" * int(len(word)))


    def guess_compare(self,letter,word,uword):
        if letter in list(word):
            list1 = [position for position, char in enumerate(word) if char == letter]
            print(list1)
            for p in list1:
                uword[p] = letter
                print(f"{uword}")
        else: 
            print(f"{letter} is incorrect guess.")
            print(f"{uword}")


    def stored_guess_1(self,guess,user1):
        self.stored_list1.append(guess)
        self.player_turn1 -= 1
        print(f"{user1} has {self.player_turn1} turns left")
        print(f"{user1} has guessed: {self.stored_list1}")


    def stored_guess_2(self,guess,user2):
        self.stored_list2.append(guess)
        self.player_turn2 -= 1
        print(f"{user2} has {self.player_turn2} turns left")
        print(f"{user2} has guessed: {self.stored_list2}")


