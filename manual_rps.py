import random


user_choice=input('Enter a choice:')

def get_computer_choice():
    word_list=['rock', 'paper', 'scissor']
    word=random.choice(word_list)
    if word in word_list:
        print(word)

def get_user_choice():
    return user_choice




#Check if the guessed chacter is in the word
# import random


# word_list=['apple', 'banana', 'orange', 'mango', 'grapes']
# word=random.choice(word_list)
# #print(word)

# def check_guess(guess):
#     guess=guess.lower()

#     if guess in word:
#         print(f"Good guess! {guess} is in the word {word}.")
#     else:
#         print(f"Sorry, {guess} is not in the word. Try again.")   

# def ask_for_input():
#     while True:
#         guess=input('Enter a character from the user:')
#         if guess.isalpha()==True and len(guess)==1:
#             print('good guess')
#         else:
#             print('Invalid letter. Please, enter a single alphabetical character.')
    
#         check_guess(guess)
    
# ask_for_input()