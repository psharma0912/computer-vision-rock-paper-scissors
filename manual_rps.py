import random


user_choice=input('Enter a choice:')

def get_computer_choice():
    word_list=['rock', 'paper', 'scissor']
    word=random.choice(word_list)
    if word in word_list:
        print(word)

def get_user_choice():
    return user_choice




