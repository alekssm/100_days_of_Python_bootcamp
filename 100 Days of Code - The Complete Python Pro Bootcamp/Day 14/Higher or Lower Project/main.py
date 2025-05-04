import game_data
import random
import art

"""The variable names refer to a person, since it was build with the assumption that we are comparing only 
famous people, not places, events, websites, etc."""


def choose_person(people, current_person):
    """Chooses a person from the data pool as dict with all of their information"""
    person = random.choice(people)
    while current_person == person:
        person = random.choice(people)
    return person

def get_person_info(person):
    """Unpacks the person's information and prints everything except follow count - returns follower count"""
    name, follower_count, description, country = person.values()
    print(f"{name}, a {description}, from {country}.")
    return follower_count

def check_answer(a_count, b_count):
    """Takes user's guess and checks if it's correct, returns 0 if correct and 1 if incorrect"""
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    while user_choice != 'a' and user_choice != 'b':
        user_choice = input("Invalid choice - Who has more followers? Type 'A' or 'B': ").lower()

    if user_choice == 'a' and a_count > b_count:
        return 0
    elif user_choice == 'b'and b_count > a_count:
        return 0
    else:
        return 1



a = {}
score = 0

while True:

    print(art.logo)
    #Checks if it's a new game or continue the current one - if a is empty - then a new game ahs started
    if not a:
        a = choose_person(game_data.data, a)
    b = choose_person(game_data.data, a)

    print(f"Compare A:", end=" ")
    a_f_count = get_person_info(a)

    print(f"\n{art.vs}")

    print(f"Against B:", end=" ")
    b_f_count = get_person_info(b)

    guess = check_answer(a_f_count, b_f_count)

    #Check if the answer is wrong and if it is, ends the game printing the final score
    if guess == 1:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break

    a = b




