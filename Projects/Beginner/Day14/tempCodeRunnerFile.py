    print(f"Compare A: {compA['name']} , a {compA['description']}, from {compA['country']}\n")
    print(f"Compare B: {compB['name']} , {compB['description']}, {compB['country']}")

    answer = input("Who has more followers? type 'A' or 'B': ").upper()

    
    if compA['follower_count'] > compB['follower_count']:
        correct = "A"
    elif compA['follower_count'] < compB['follower_count']:
        correct = "B"
        

    if answer == correct:
        os.system('cls')

        score += 1
        print(f"You're right! Current score: {score}")
    else:
        os.system('cls')
        print(art.logo)
        print(f"Sorry, thats wrong. Final score: {score}")
        game_on = False



