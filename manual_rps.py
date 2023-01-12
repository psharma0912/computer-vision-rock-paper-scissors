import random


# computer randomly selects a choice   
def get_computer_choice():
    computer_choice =random.choice(['Rock','Paper','Scissors'])
    #print (f'comp_choice is {comp_choice}')
    return computer_choice
       
      
# user is asked to input their choice  
def get_user_choice():
    while True:
        user_choice = input('Rock, Paper, or Scissors?: ')
        print (f'user_choice is {user_choice}')
        if user_choice in ['Rock','Paper','Scissors']:
            return user_choice
        else:
            print('Invalid choice. Please try again')

def get_winner(computer_choice, user_choice):
    if user_choice == 'Rock' and computer_choice == 'Paper':
        print ('You lost!')
    elif user_choice == 'Rock' and computer_choice == 'Scissors':
        print('You win!')
    elif user_choice == 'Paper' and computer_choice == 'Scissors':
        print('You lost!')
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        print('You win!')   
    elif user_choice == 'Scissors' and computer_choice == 'Rock':
        print('You lost!')   
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        print('You win!')
    else:
        print ('It is a tie!')




  

#get_winner(get_computer_choice, get_user_choice)



