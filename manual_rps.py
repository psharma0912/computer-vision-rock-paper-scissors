import random

word_list=['rock', 'paper', 'scissor']
print(word_list)

word=random.choice(word_list)
print(word)

user_choice=input('Enter a choice:')

def get_computer_choice():
    if word in word_list:
        print(word)

def get_user_choice():
    return user_choice


