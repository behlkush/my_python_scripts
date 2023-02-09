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
    __________
-------'______)_____
              ______)
              _______)
             _______)
-------.__________)
    '''

scissors = '''
    _______
---'   ____)______
          ________)
          )_________
       ______________)
      (_________)
---.__(_______)
'''

smiley = '''
✌(-‿-)✌ ✌(-‿-)✌ ✌(-‿-)✌
'''

sadface = '''
⊂(◉︵◉)つ ⊂(◉︵◉)つ ⊂(◉︵◉)つ 
'''

drawface = '''
(☝ ՞ਊ ՞)☝ (☝ ՞ਊ ՞)☝ (☝ ՞ਊ ՞)☝
'''



def print_win():
    print("Yippie. You WIN!!")
    print(smiley)


def print_loss():
    print("Ouchie ouch. You LOOOSE!")
    print(sadface)


def print_draw():
    print("It is a draw!!")
    print(drawface)

print("Welcome to Rock, Papers and scissors by DB and KB!")
print("Please enter your choice....")
player_choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))

computer_pick = int(random.randint(1, 3))

#Rock beats Scissors, so 1 beats 3
#Paper beats Rock, 2 beats 1
#Scissors beat paper, 3 beats 2

#Cover choice Rock
if player_choice == 1:
    print("Your choice: 1, Rock")
    print(rock)
    if computer_pick == 3:
        print("Computer's choice is: 3, Scissors")
        print(scissors)
        print_win()
    elif computer_pick == 2:
        print("Computer's choice is: 2, Paper")
        print(paper)
        print_loss()
    else:
        #Its a draw case
        print("Computer's choice is: 1, Rock")
        print(rock)
        print_draw()
      
#For Paper
elif player_choice == 2:
    print("Your choice: 2, Paper")
    print(paper)
    if computer_pick == 1:
        print("Computer's choice is: 1, Rock")
        print(rock)
        print_win()
    elif computer_pick == 3:
        print("Computer's choice is: 3, Scissors")
        print(scissors)
        print_loss()
    else:
        #Its a draw case
        print("Computer's choice is: 2, Paper")
        print(paper)
        print_draw()
      
#For Scissors - 3 beats 2
elif player_choice == 3:
    print("Your choice: 3, Scissors")
    print(scissors)
    if computer_pick == 2:
        print("Computer's choice is: 2, Paper")
        print(paper)
        print_win()
    elif computer_pick == 1:
        print("Computer's choice is: 1, Rock")
        print(rock)
        print_loss()
    else:
        #Its a draw case
        print("Computer's choice is: 3, Scissors")
        print(scissors)
        print_draw()
