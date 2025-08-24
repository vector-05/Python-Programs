# Word guessing game
import random
import time

words = ["beautiful","yummy","hello","world","home","game","music","operation","water","air","ship","submarine","nice","computer","dog","cat","tiger","lion"]
user_chances = 0

game_word = random.choice(words)
game_word_len = len(game_word)

if game_word_len < 4:
    user_chances = 12
elif game_word_len > 3 and game_word_len < 10:
    user_chances = 20
elif game_word_len > 9:
    user_chances = 25

def welcome():
    print("|| Welcome to word guessing ||")
    user_name = input("Your Name | ")
    print("Directions |",f"1-- The length of the word is {game_word_len}",f"2 -- You will get {user_chances} chances to guess the word","3 -- All characters are small case","4 -- You can only enter one character at a time | You will loose chances for wrong inputs","5 -- No letter is repeated",sep="\n")
    print(f"Good luck {user_name}")
    print("Ready")
    time.sleep(1)
    print("Set")
    time.sleep(1)
    print("Go")
    time.sleep(1)

correct_word = list("_" * game_word_len)

def game():
    for i in range(1,user_chances+1):
        a = input("Your character ")
        if len(a) == 1:
            if a in game_word:
                word_location = game_word.index(a)
                correct_word[word_location] = a
                correct_word_str = ""
                for z in correct_word:
                    correct_word_str += z
                print(correct_word_str)
                print(f"You have {user_chances - i} chances left")
                if correct_word_str == game_word:
                    print(f"You have won | The correct word was {game_word}")
                    break
                else:
                    continue
            elif a not in game_word:
                print(f"You have {user_chances - i} chances left")
                print(f"{a} is not in the word")
        else:
            print("Wrong input")
            continue
        
welcome()
game()
