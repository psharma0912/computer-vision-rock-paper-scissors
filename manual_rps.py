import random

class rps: 
    def __init__(self, choice_list):
        self.computer_choice = random.choice(choice_list)
        self.user_choice = input('Rock, Paper, or Scissors?: ')
        print (f'user_choice is {self.user_choice}')

# computer randomly selects a choice   
    def get_computer_choice(self):
        print (f'comp_choice is {self.computer_choice}')
        return self.computer_choice
        
# user is asked to input their choice  
    def get_user_choice(self):
        if self.user_choice in choice_list:
            return self.user_choice
        else:
            print('Invalid choice. Please try again')

    def get_winner(self, computer_choice, user_choice):
        if user_choice == computer_choice:
            print("It is a tie!") 
        elif (user_choice == "Rock" and computer_choice== "Scissors") or \
        ( user_choice == "Paper" and computer_choice == "Rock") or \
        ( user_choice == "Scissors" and computer_choice == "Paper"):
            print("You won!")
        else: 
            print("You lost!")

def play(choice_list):
    game = rps(choice_list)
    computer= game.get_computer_choice()
    user = game.get_user_choice()
    game.get_winner(user, computer)

if __name__ == '__main__': 
    choice_list=['Rock','Paper','Scissors'] 
    play(choice_list)
        

