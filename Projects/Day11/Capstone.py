
import random



#deck of cards and below is the chosen card
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]



def outcome():
    if sum_c>sum_p or sum_p>21:
        print("Sorry You Lost")
    elif sum_c<sum_p or sum_c>21:
        print("You win")
    elif sum_c==sum_p:
        print("Its a tie")



should_continue=True
sum_c=0
sum_p=0

while should_continue:

    play=input("Enter y to pick a card and any key to quit:").lower()
    if play=="y":
        
        person=random.choice(cards)
        print(f"Chosen card is {person}")
        computer=random.choice(cards)
        print(f"The computer chose {computer}")
        sum_c+=computer
        sum_p+=person
    else:
        should_continue=False
        print("Ended")
        
      

print(f"The computer score is {sum_c}") 
print(f"Your score is {sum_p}")   

outcome()



 

   


# second_card=input("Enter y to pick another card and any key to quit:").lower()
# chosen_card=random.choice(cards)

# if second_card =="y":
#     print(f"Chosen card is {chosen_card}")
# else:
#     print("Exiting") 


