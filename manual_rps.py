import random
#choice_list = ['rock','paper','scissors']

# computer randomly selects a choice   
def get_computer_choice():
    choice_list = ['rock','paper','scissors']
    computer = random.choice(choice_list)
    print(f'computer choice is {computer}')
    return computer
   
# user is asked to input their choice  
def get_user_choice():
    while True:
        player = input('rock, paper, or scissors?: ').lower()
        if player in ['rock','paper','scissors']:
            return player
        else:
            print('Invalid choice. Please try again')


get_computer_choice()

get_user_choice()


