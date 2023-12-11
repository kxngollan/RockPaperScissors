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

import random

selection = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

computer = random.randint(0, 2)
if computer == 0:
   computer = rock 
elif computer == 1:
   computer = paper
else:
   computer = scissors

print(computer)

if selection == 0:
   selection = rock 
elif selection == 1:
   selection = paper
else:
   selection = scissors

print(selection)

print(f"You choose:\n {selection}")
print(f"Computer choose:\n {computer}")
if computer == selection:
   print("Draw!")
elif computer == rock and selection == paper:
   print("You Win!")
elif computer == paper and selection == scissors:
   print("You Win!")
elif computer == scissors and selection == rock:
   print("You Win!")
else:
   print("You Lose!")