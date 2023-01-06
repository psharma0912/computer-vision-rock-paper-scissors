import random


def get_computer_choice():
    word_list=['rock', 'paper', 'scissor']
    word=random.choice(word_list)

    if word in word_list:
        print(word)
    return word

def get_user_choice():
    while True:
        user_choice=input('Enter a choice:')
        return user_choice

get_computer_choice()

get_user_choice()





