import cv2
import time
from keras.models import load_model
import numpy as np
import random

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
computer_wins = 0
user_wins=0


# get the current time in seconds since the epoch
seconds = time.time()
print("Seconds since epoch =", seconds)	

def count_countdown():
    countdown = 5
    while countdown > 0:
        print(f'{countdown}')
        cv2.waitKey(1000)
        countdown -= 1
    print('Show your hand now') 

def get_computer_choice():
    computer_choice =random.choice(choice_list)
    #print (f'Computer choice is {computer_choice}')
    return computer_choice

def get_winner(computer_choice, user_choice):
    global user_wins, computer_wins
    if user_choice == "Nothing":
        print("Restart, and choose something this time!")
    elif user_choice == computer_choice:
            print("It is a tie!") 
    elif (user_choice == "Rock" and computer_choice== "Scissors") or \
            ( user_choice == "Paper" and computer_choice == "Rock") or \
            ( user_choice == "Scissors" and computer_choice == "Paper"):
        print("You won!")
        user_wins += 1 
    else: 
        print("You lost")
        computer_wins += 1


#user choice
def get_prediction():
    end_time = time.time() + 3
    while end_time > time.time():
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        cv2.imshow('frame', frame)
        prediction = model.predict(data) #prediction contains the output of the model
        #Notice that the prediction is a numpy array with one row and four columns. So first, we need to access the first row, and then get the index of the
        #highest value in the row. 
        choice = choice_list[prediction.argmax()]
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return choice


def play_game():
    while True:
        count_countdown()
        computer_choice = get_computer_choice()
        user_choice = get_prediction()
        get_winner(computer_choice, user_choice)
        print(f"Computer wins: {computer_wins} ---- User wins: {user_wins}")
        if user_wins == 3 or computer_wins == 3:
            print(f"The game is over, Computer won {computer_wins} and you won {user_wins}")
            break
            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__=='__main__':
    choice_list=['Rock', 'Paper', 'Scissors', 'Nothing']
    play_game()

    





