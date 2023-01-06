import random
choice_list=['rock', 'paper', 'scissors']

# def get_computer_choice():
#    computer_choice=random.choice(choice_list)
#    print(computer_choice)
#    return computer_choice.lower()

# def get_user_choice():
#     user_choice=input('Enter a choice:').lower()
#     print (user_choice)
#     return user_choice

# get_computer_choice()

# get_user_choice()

def get_computer_choice():
    #choice_list = ['Rock','Paper','Scissors']
    computer_choice = random.choice(choice_list).lower()
    print(computer_choice)
    return computer_choice


def get_user_choice():
    while True:
        user_choice = input('Please choose Rock, Paper or Scissors:').lower()
        if user_choice == 'rock' or user_choice == 'scissors' or user_choice == 'paper':
            return user_choice

get_computer_choice()

get_user_choice()
           