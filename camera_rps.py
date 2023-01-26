import cv2
import time
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# get the current time in seconds since the epoch
seconds = time.time()
print("Seconds since epoch =", seconds)	

def count_countdown():
    countdown = 5
    print("Please prepare to show your choice")
    while countdown > 0:
        print(f'{countdown}')
        cv2.waitKey(1000)
        countdown -= 1
    print('Show your hand now') 


def get_prediction():
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data) #prediction contains the output of the model
        #Notice that the prediction is a numpy array with one row and four columns. So first, we need to access the first row, and then get the index of the
        #highest value in the row. 
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

count_countdown()    

get_prediction()






