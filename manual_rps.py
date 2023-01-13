import random

choice_list=['Rock', 'Paper', 'Scissors']

def get_computer_choice():
    computer_choice =random.choice(choice_list)
    return computer_choice

def get_user_choice():
    while True:
        user_choice=input('Rock, Paper or Scissors?:')
        if user_choice in choice_list:
            return user_choice
        else:
            print('Invalid choice. Please try again')
            return user_choice

