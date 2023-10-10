
from game_data import data
# print(data)
import random

name=[d['name'] for d in data]
uniq=[d['description'] for d in data]
origin=[d['country'] for d in data]
fan_count=[d['follower_count'] for d in data]

#keep the score
score = 0

#for the loop, will use it to break from the loop once the user gets an answer wrong
keep_playing = True

while keep_playing:

    random_a=random.randint(0,len(data))
    random_b=random.randint(0,len(data))

    print(f"Compare A: {name[random_a]}, a {uniq[random_a]},from {origin[random_a]}\n")
    print(f"Against B: {name[random_b]}, a {uniq[random_b]},from {origin[random_b]}")

    compare={"a":fan_count[random_a],"b":fan_count[random_b]}

    answer=input("Who has more followers? Type 'A' or 'B':").lower()
    fcount=compare[answer]

    #variable for the correct answer the user must guess
    correct = ""

    #check correct answer
    if compare["a"] > compare["b"]:
        correct = "a"
    else:
        correct = "b"

    #check if the provided answer is correct
    if answer == correct:
        score +=1
        print(f"\n\n\n\nYou are right! current score {score}")
    else:
        print(f"\n\n\n\nSorry, that's wrong. Final Score: {score}")
        keep_playing = False

    # print(fcount)

c = input("Press any key to close")