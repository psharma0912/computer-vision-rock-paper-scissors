import random
choice_list=['rock', 'paper', 'scissor']

def get_computer_choice():
   computer_choice=random.choice(choice_list)
   print (computer_choice)
   return computer_choice

def get_user_choice():
    user_choice=input('Enter a choice:')
    print (user_choice)
    return user_choice

get_computer_choice()

get_user_choice()
    





   