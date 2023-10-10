import random
import art
import game_data
import os

print(art.logo)

game_on = True
score = 0

while game_on:
  compA = game_data.data[random.randint(0, len(game_data.data))]
  compB = game_data.data[random.randint(0, len(game_data.data))]
  
  print(f"Compare A: {compA['name']} , a {compA['description']}, from {compA['country']}")
  print(art.vs)
  print(f"Compare B: {compB['name']} , {compB['description']}, {compB['country']}")
  
  choice = input("Who has more followers? type 'A' or 'B': ").upper()
  
  if compA['follower_count'] > compB['follower_count']:
    correct = "A" #A for A is the highest 
  else:
    correct = "B"
  
  if choice == correct:
    os.system('cls')
    print(art.logo)
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    os.system('cls')
    print(art.logo)
    print(f"Sorry, thats wrong. Final score: {score}")
    game_on = False

hold_screen = input("Press any button to exit!")