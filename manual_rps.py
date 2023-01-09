import random


# computer randomly selects a choice   
def get_computer_choice():
    return random.choice(['Rock','Paper','Scissors'])
      
# user is asked to input their choice  
def get_user_choice():
    while True:
        player = input('Rock, Paper, or Scissors?: ')
        if player in ['Rock','Paper','Scissors']:
            return player
        else:
            print('Invalid choice. Please try again')


#get_computer_choice()

#get_user_choice()


