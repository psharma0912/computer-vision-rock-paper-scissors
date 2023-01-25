
import cv2
from keras.models import load_model
import numpy as np
# import the time module
import time
import random

# get the current time in seconds since the epoch
seconds = time.time()
print("Seconds since epoch =", seconds)	

class rps: 
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0) #opens the camera
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.computer_wins = 0
        self.user_wins = 0
        #self.computer_choice = random.choice(choice_list)
        #self.user_choice = input('Rock, Paper, or Scissors?: ')
        #print (f'user_choice is {self.user_choice}')

    def count_countdown(self):
        countdown = 5
        print("Please prepare to show your choice")
        while countdown > 0:
            print(f'{countdown}')
            cv2.waitKey(1000)
            countdown -= 1
        print('Show your hand now') 
    
    def get_winner(self,computer_choice, user_choice):
        if user_choice == "Nothing":
            print("Restart, and choose something this time!")
        elif user_choice == computer_choice:
                print("It is a tie!") 
        elif (user_choice == "Rock" and computer_choice== "Scissors") or ( user_choice == "Paper" and computer_choice == "Rock") or ( user_choice == "Scissors" and computer_choice == "Paper"):
            print("You won!")
            self.user_wins += 1
        else: 
            print("You lost!")
            self.computer_wins += 1

    def get_computer_choice(self):
        computer_choice =random.choice(choice_list[:-1])
        #print (f'Computer choice is {computer_choice}')
        return computer_choice

#This is now the user choice
    def get_prediction(self):
        end_time = time.time() + 3
        while end_time > time.time():
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            cv2.imshow('frame', frame)
            prediction = self.model.predict(self.data)
            self.choice = choice_list[prediction.argmax()]
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return self.choice

def play_game():
    game = rps()
    while True:
        game.count_countdown()
        user_choice = game.get_prediction()
        computer_choice = game.get_computer_choice()
        game.get_winner(computer_choice, user_choice)
        print(f"Computer wins: {game.computer_wins} ---- User wins: {game.user_wins}")

        if game.user_wins == 3 or game.computer_wins == 3:
            print(f"The game is over, Computer won {game.computer_wins} and you won {game.user_wins}")
            break

# After the loop release the cap object
    game.cap.release()
# Destroy all the windows
    cv2.destroyAllWindows()


#print the countdown in the webcam display, or include a message like "press c to continue"
    
if __name__ == '__main__':
    choice_list=['Rock', 'Paper', 'Scissors', 'Nothing']
    play_game()