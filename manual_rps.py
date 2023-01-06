import random
choice_list=['rock', 'paper', 'scissors']

def get_computer_choice():
    #choice_list = ['Rock','Paper','Scissors']
    computer_choice = random.choice(choice_list)
    return computer_choice.lower()



def get_user_choice():
    while True:
        user_choice = input('Please choose Rock, Paper or Scissors:').lower()
        if user_choice == 'rock' or user_choice == 'scissors' or user_choice == 'paper':
            return user_choice
        else:
            print('Please choose one of the options selected')

        