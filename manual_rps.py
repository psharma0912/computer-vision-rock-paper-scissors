import random


# computer randomly selects a choice   
def get_computer_choice():
    computer_choice =random.choice(['Rock','Paper','Scissors'])
    print (f'comp_choice is {computer_choice}')
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
    if user_choice == computer_choice:
        print("It is a tie!") 
    elif (user_choice == "Rock" and computer_choice== "Scissors") or ( user_choice == "Paper" and computer_choice == "Rock") or ( user_choice == "Scissors" and computer_choice == "Paper"):
        print("You won!")
    else: 
        print("You lost!")

def play(get_computer_choice, get_user_choice, get_winner):
    return get_computer_choice, get_user_choice, get_winner
    
        
get_computer_choice()

get_user_choice() 

get_winner(get_computer_choice, get_user_choice)

play(get_computer_choice, get_user_choice, get_winner)
 





  





