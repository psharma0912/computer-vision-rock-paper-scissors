import random
choice_list=['rock', 'paper', 'scissor']

# def get_computer_choice():
#    computer_choice=random.choice(choice_list)
#    print (computer_choice)
#    return computer_choice

# def get_user_choice():
#     user_choice=input('Enter a choice:')
#     print (user_choice)
#     return user_choice

# get_computer_choice()

# get_user_choice()

def get_computer_choice():
        ## This functions randomly picks a choice for computer
        return random.choice(choice_list).lower()
    
def get_user_choice():
        ## This functions asks the user for a choice to start the game
    user_input = input('Please pick one of Rock Paper or Scissor -> ').lower()
    # while user_input not in ['rock', 'paper', 'scissor']:
    #     user_input = input('Your choice should be one of Rock Paper or Scissor -> ')
    return user_input.lower()
        





   