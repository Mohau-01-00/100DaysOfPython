from art import logo
import random
print(logo)

num=random.randrange(1,100)
print(num)




def clue():
    if num<answer:
        print("Too High")
    elif num>answer:
        print("Too Low")
  

#create a dictionary to use later
chances={"easy":10,"hard":5}





print("Welcome to the number guessing game!")


wrong_input=True
while wrong_input:
    difficulty=input("Choose a difficulty.Type 'easy' or 'hard':").lower()
    if difficulty!="easy" and difficulty!="hard":
               print("Wrong Input")
    else:
        wrong_input=False
     

answer=int(input("I'm thinking of a number between 1 to 100:"))


num_chances=chances[difficulty]

should_continue=True
while should_continue:
    
    
    if num!=answer and num_chances!=1:
        num_chances=num_chances-1
       
        clue()
        
        print(f"{num_chances} chances left")
        answer=int(input("Guess again:"))
   

    elif answer==num:
         should_continue=False
         print(f"You got it! the answer was {num}")
    elif num_chances==1:
        should_continue=False
        print("You've run out of guesses, you lose")


      


