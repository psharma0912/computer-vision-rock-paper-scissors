import random

word_list=['rock', 'paper', 'scissor']
word=random.choice(word_list)


def get_computer_choice(user_choice):
    
    if user_choice in word_list:
        #print(word)
        return user_choice

def get_user_choice():
    while True:
        user_choice=input('Enter a choice:')
        print (user_choice)
        
        get_computer_choice(user_choice)

get_user_choice()



   