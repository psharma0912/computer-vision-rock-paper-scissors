import random
#word_list=['rock', 'paper', 'scissor']

def get_computer_choice():
   computer_choice=random.choice(['rock', 'paper', 'scissor'])
   print (computer_choice)
   return computer_choice

def get_user_choice():
    user_choice=input('Enter a choice:')
    return user_choice

get_computer_choice()

get_user_choice()
    





   