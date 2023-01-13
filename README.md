# Computer Vision RPS
# Introduction

Rock Paper Scissors is a hand game usually played between two people. In this game, scissors can beat paper, paper can beat rock, and rock can beat scissors. 


We are creating the Rock Paper Scissor game using the Computer Vision. A web based model called Teachable machine is used to create the model. It lets you train models entirely in the browser with no coding required. Four classes called Rock, Paper, Scissor and Nothing are created where user is showing image of each class to the computer and each class is getting trained. The "Nothing" class represents the lack of option in the image. Note  that the more images you train with, the more accurate the model will be.

Once the images are trained, the model is downloaded from the "Tensorflow" tab in Teachable-Machine. The model is named keras_model.h5 and the text file containing the labels is named labels.txt.

The files that are downloaded contain the structure and the parameters of a deep learning model. They are not files that can be run, and they do not contain anything readable if we look inside. Later, these files will be downloaded into our Python application in the next milestone.

# Milestone 1
- ## Creation of the image project model: 
Four different classes called, Rock, Paper, Scissors and Nothing were used to create the model. Each class is trained with images of yourself showing each option to the camera. The "Nothing" class represents the lack of option in the image. Note that the more images you train with, the more accurate the model will be. This model was created using [Teachable Machine](https://teachablemachine.withgoogle.com/). Image samples for the four different classes were added using the webcam. Each of the class contained atleast 1000 samples. The model was then trained and the output obtained. The output was then exported and downloaded.

# Milestone 2

- ## Downloading the model

The model was downloaded from the "Tensorflow" tab in Teachable-Machine and called keras_model.h5. The text file containing the labels is named  as labels.txt.

Note that the files which are downloaded contain the structure and the parameters of a deep learning model. They are not files that can be run, and they do not contain anything readable if you look inside. Later, these will be loaded into Python application in the next milestone.

- ## Installing the dependencies

In order for the model to work there are a few dependencies (opencv-python, tensorflow, and ipykernel) that needed to be installed. For this, a virtual environment was created which helps to keep dependencies required by different projects separate.

To create a new environment use the command:
```
conda create -n my_env python=3.8
```
Activate the environment using:
```
conda activate my_env
```
Tthen install pip by running the following command in the terminal:
```
conda install pip
```
Then, to install the rest of the libraries, run 
```
pip install <library>
```
Once the libraries are installed create a requirements.txt file by running the following command:
```
pip list > requirements.txt
```
This file enables any other user that wants to use your computer to easily install these exact dependencies by running pip install requirements.txt.

```
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```
# Milestone 3

- ## Manual Version RPS
In this task a file called  manual_rps.py is created which stores the user's and computer's choices. Two functions called
get_computer_choice and get_user_choice are created.
The first function will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice.
The second function will ask the user for an input and return it.

```
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def get_user_choice(self):
    while True:
        user_choice = input('Rock, Paper, or Scissors?: ')
        if user_choice in ['Rock', 'Paper', 'Scissors']:
            return user_choice
        else:
            print('Invalid choice. Please try again')
```
The function get_winner() is then used which takes into account the if-elif-else statements, and chooses a winner based on the classic rules of Rock-Paper-Scissors.

For example, if the computer chooses rock and the user chooses scissors, the computer wins.

```
def get_winner(computer_choice, user_choice):
        if user_choice == computer_choice:
            print("It is a tie!") 
        elif (user_choice == "Rock" and computer_choice== "Scissors") or \
        ( user_choice == "Paper" and computer_choice == "Rock") or \
        ( user_choice == "Scissors" and computer_choice == "Paper"):
            print("You won!")
        else: 
            print("You lost!")
```