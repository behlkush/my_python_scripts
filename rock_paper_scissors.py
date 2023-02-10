import random

rock = ''' ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
  '''

paper = ''' PAPER
    __________
-------'______)_____
              ______)
              _______)
             _______)
-------.__________)
    '''

scissors = ''' SCISSOR
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

my_arts = [rock, paper, scissors]


#Write your code below this line 👇
print("Welcome to Rock, Papers and scissors by DB and KB!")
print("Please enter your choice....")


player_choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))




if player_choice <= 0 or player_choice > 3:
  print("You made an invalid choice. Defaulting to a random choice")
  player_choice = int(random.randint(1, 3))

index_corrected_choice = player_choice - 1
print(f"Your Choice is: {player_choice}")
print(my_arts[index_corrected_choice])

computer_pick = int(random.randint(1, 3))
index_corrected_comp = computer_pick - 1

print(f"Computer choice is: {computer_pick}")
print(my_arts[index_corrected_comp])

def print_win():
    print("Yippie. You WIN!!")
    print(smiley)


def print_loss():
    print("Ouchie ouch. You LOOOSE!")
    print(sadface)


def print_draw():
    print("It is a draw!!")
    print(drawface)


#Rock beats Scissors, so 1 beats 3
#Paper beats Rock, 2 beats 1
#Scissors beat paper, 3 beats 2

#Cover choice Draw
if player_choice == computer_pick:
  print_draw()
# Case Rock and Scissors
elif player_choice == 1 and computer_pick == 3:
  print_win()
# Case Scissors and Rock 
elif player_choice == 3 and computer_pick == 1:
  print_loss()
#For Paper
elif computer_pick > player_choice:
  print_loss()
else:
  print_win()
