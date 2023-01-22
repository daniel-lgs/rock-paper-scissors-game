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

arts = [rock, paper, scissors]
user_choice = int(input("Chose your number option:\n1 - Rock\n2 - Paper\n3 - Scissors\n")) - 1
computer_choice = random.randint(0, 2)

if (user_choice == computer_choice):
    print(f"Your choice:\n{arts[user_choice]}\nComputer choice:\n{arts[computer_choice]}\nIt was a draw!")
elif (user_choice == 0 and computer_choice == 2):
    print(f"Your choice:\n{arts[user_choice]}\nComputer choice:\n{arts[computer_choice]}\nYou won!")
elif (user_choice == 1 and computer_choice == 0):
    print(f"Your choice:\n{arts[user_choice]}\nComputer choice:\n{arts[computer_choice]}\nYou won!")
elif (user_choice == 2 and computer_choice == 1):
    print(f"Your choice:\n{arts[user_choice]}\nComputer choice:\n{arts[computer_choice]}\nYou won!")
else:
    print(f"Your choice:\n{arts[user_choice]}\nComputer choice:\n{arts[computer_choice]}\nYou lose!")
