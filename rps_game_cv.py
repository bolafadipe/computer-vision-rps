import random #for computer choice
import cv2 #to leverage camera
from keras.models import load_model #to run the  model
import numpy as np #for arrays for interpretting the image
import time



class CvRps:

    choice_list = ['rock', 'paper', 'scissors'] #declared this outside the init without self
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    start_time = time.time()
    seconds = 10

    def __init__(self):
        pass

    def get_prediction(self):

        while True: 
            current_time = time.time()
            elapsed_time = current_time - CvRps.start_time
            ret, frame = CvRps.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            CvRps.data[0] = normalized_image
            cv2.imshow('frame', frame)
            prediction = CvRps.model.predict(CvRps.data)

            # Press q to close the window
            
            if elapsed_time > CvRps.seconds:
                self.stop_camera()#call the method to stop the camera
                self.get_user_choice(prediction)#call the convert the array to a choice
                

        
    def stop_camera(self):
        CvRps.cap.release()# After the loop release the cap object
        cv2.destroyAllWindows()# Destroy all the windows
        pass   

    def get_user_choice(self, prediction):
        np.array(prediction) #convert to array
        idx_max = prediction.argmax() #find the max value
        choices = ["rock", "paper", "scissors", "nothing"]
        user_camera_choice = choices[idx_max]
        print(f'cv_choice var prints: {user_camera_choice}') #just testing to see if it makes it here
        self.get_computer_choice(user_camera_choice) 

    def get_computer_choice(self,user_choice):
        computer_choice = random.choice(CvRps.choice_list)
        print(f"You picked: {user_choice}. The computer picked {computer_choice}") #just testing to see if it makes it here
        self.get_winner(user_choice, computer_choice)

    def get_winner(self, user_choice, computer_choice):
        if computer_choice == user_choice:
            print("It's a draw!")
        elif computer_choice == 'rock' and user_choice == 'scissors':
            print('You lost')
        elif computer_choice == 'rock' and user_choice == 'paper':
            print('You Won')
        elif computer_choice == 'paper' and user_choice == 'rock':
            print('You lost')
        elif computer_choice == 'paper' and user_choice == 'scissors':
            print('You won')
        elif computer_choice == 'scissors' and user_choice == 'rock':
            print('You won')
        elif computer_choice == 'scissors' and user_choice == 'paper':
            print('You lost')
        else:
            print('No Result: Seems to be an error somewhere')

def play_rps():
    game = CvRps()
    game.get_prediction()
