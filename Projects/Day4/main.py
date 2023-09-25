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

#Write your code below this line 👇

player=int(input("What do you player? Type 0 for rock, 1 for paper or 2 for scissors\n"))

list=[0,1,2]

computer=random.choice(list)


if player==0:
    print(rock)
elif player==1:
  print(paper)
elif player==2:
  print(scissors)

print("Computer Chose:")
if computer==0:
    print(rock)
elif computer==1:
  print(paper)
elif computer==2:
  print(scissors)

if (player==0 and computer==0) or (player==1 and computer==1) or (player==2 and computer==2):
  print("Its a tie")
  #player wins
elif (player==0 and computer==2) or (player==1 and computer == 0) or (player==2 and computer==1):
  print("You win")
elif player >2 or player<0:
  print("Invalid coice, you lose")
else:
  print("You lose")
