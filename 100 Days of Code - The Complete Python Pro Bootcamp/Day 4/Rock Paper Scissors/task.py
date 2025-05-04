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

choices = [rock, paper, scissors]

computers_choice = random.randint(0, 2)
my_choice = int(input('What do you choose? '
                      'Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if my_choice >= 3 or my_choice < 0:
    print("You've chosen an invalid number - Game over")

else:
    print(choices[my_choice])
    print(f"Computer chose:\n{choices[computers_choice]}")

    if computers_choice == my_choice:
        print("Draw")
    elif (my_choice == 0 and computers_choice == 2) or (my_choice == 1 and computers_choice == 0) \
            or (my_choice == 2 and computers_choice == 1):
        print("You win")
    else:
        print("You lose")


