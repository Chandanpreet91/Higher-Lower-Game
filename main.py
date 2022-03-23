from art import logo, vs
from game_data import data
import random

print(logo)
should_continue = True
while should_continue:
    new_data = data[random.randint(0,len(data)- 1)]
    name = new_data["name"]
    followers_A = new_data["follower_count"]
    description = new_data["description"]
    country =new_data["country"]
    print(f"Compare A:  a {name}, a {description} from {country}" )

    print(vs)

    other_data = data[random.randint(0,len(data)-1)]
    other_name = other_data["name"]
    followers_B = other_data["follower_count"]
    other_description = other_data["description"]
    other_country =other_data["country"]
    print(f"Against B : a {other_name}, {other_description} from {other_country}")
    answer = input("Who has more followers? Type 'A' or 'B' ")
    score = 0

    if followers_A > followers_B and answer == "A" :
            score += 1
            print(f'You\'re right! Current Score : {score}')  
    elif followers_B > followers_A and answer == "B":
            score += 1
            print(f'You\'re right! Current Score : {score}')   
    else:
        print(f'Sorry, that\'s wrong, your final score is {score}')
        should_continue = False