# Computer Vision RPS
# Introduction

Rock Paper Scissors is a hand game usually played between two people. In this game, scissors can beat paper, paper can beat rock, and rock can beat scissors. 


We are creating the Rock Paper Scissor game using the Computer Vision. A web based model called Teachable machine is used to create the model. It lets you train models entirely in the browser with no coding required. Four classes called Rock, Paper, Scissor and Nothing are created where user is showing image of each class to the computer and each class is getting trained. The "Nothing" class represents the lack of option in the image. Note  that the more images you train with, the more accurate the model will be.

Once the images are trained, the model is downloaded from the "Tensorflow" tab in Teachable-Machine. The model is named keras_model.h5 and the text file containing the labels is named labels.txt.

The files that are downloaded contain the structure and the parameters of a deep learning model. They are not files that can be run, and they do not contain anything readable if we look inside. Later, these files will be downloaded into our Python application in the next milestone.