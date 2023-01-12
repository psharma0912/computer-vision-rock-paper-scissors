import random


# computer randomly selects a choice   
def get_computer_choice():
    comp_choice =random.choice(['Rock','Paper','Scissors'])
    #print (f'comp_choice is {comp_choice}')
    return comp_choice
       
      
# user is asked to input their choice  
def get_user_choice():
    while True:
        user_choice = input('Rock, Paper, or Scissors?: ')
        print (f'user_choice is {user_choice}')
        if user_choice in ['Rock','Paper','Scissors']:
            return user_choice
        else:
            print('Invalid choice. Please try again')

def get_winner(get_computer_choice, get_user_choice):
    if 'Rock' in get_computer_choice() and 'Scissors' in get_user_choice():
        print ('You lost!')
    elif 'Rock' in get_computer_choice() and 'Paper' in get_user_choice():
        print ('You won!')
    else:
        print ('Its a tie!')



#     get_computer_choice()

#     get_user_choice()

# get_winner(get_computer_choice, get_user_choice)



