import random

def get_computer_choice():
    word_list=['rock', 'paper', 'scissor']
    computer_choice=random.choice(word_list)
    return computer_choice

def get_user_choice():
    while True:
        user_choice=input('Enter a choice:')
        return user_choice
    #get_computer_choice()





   