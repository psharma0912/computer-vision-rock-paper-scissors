import random

def get_computer_choice():
    computer_choice =random.choice(['Rock', 'Paper', 'Scissors'])
    return computer_choice

def get_user_choice():
    while True:
        user_choice=input('Rock, Paper or Scissors?:')
        if user_choice in ['Rock', 'Paper', 'Scissors']:
            return user_choice
        else:
            print('Invalid choice. Please try again')
            

