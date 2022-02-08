# Hangman day 6 project
import random

word_list = ["ardvark", "baboon", "camel"]
#word = word_list[random.randint(0,2)]
word = random.choice(word_list)

print(f"Pssst, the solution is {word}.")

display = []

for i in range(len(word)):
    display.append('_')

print(display)

#guess = input("Guess a letter: ")

#for i in word:
#    if i == guess:
#        print("Right")
#    else:
#        print("Wrong")