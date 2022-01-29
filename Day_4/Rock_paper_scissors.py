# Rock Paper Scissors day 4 project

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line

hands = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
ai_choice = random.randint(0, 2)

print(hands[choice])
print("\n")
print("Computer chose:\n")
print(hands[ai_choice])
print("\n")
if choice == 0 and ai_choice == 1:
    print("You lose.")
elif choice == 0 and ai_choice == 2:
    print("You win.")
elif choice == 1 and ai_choice == 2:
    print("You lose.")
elif choice == 1 and ai_choice == 0:
    print("You win.")
elif choice == 2 and ai_choice == 0:
    print("You lose.")
elif choice == 2 and ai_choice == 1:
    print("You win.")
else:
    print("It`s a draw")

