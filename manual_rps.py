import random
#choice_list = ['rock','paper','scissors']

# computer randomly selects a choice   
def get_computer_choice():
    return random.choice(['rock','paper','scissors'])
      
# user is asked to input their choice  
def get_user_choice():
    while True:
        player = input('rock, paper, or scissors?: ')
        if player in ['rock','paper','scissors']:
            return player
        else:
            print('Invalid choice. Please try again')


#get_computer_choice()

#get_user_choice()


