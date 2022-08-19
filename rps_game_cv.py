import random #for computer choice
import cv2 #to leverage camera
from keras.models import load_model #to run the  model
import numpy as np #for arrays for interpretting the image
import time



class CvRps:

    choice_list = ['rock', 'paper', 'scissors'] #declared this outside the init without self
    start_time = time.time()
    seconds = 3 #set how many seconds to run the camera 


    def __init__(self,rounds):
        self.rounds = 1
        self.computer_wins = 0
        self.user_wins = 0

    def get_prediction(self, rounds):        
        
        
        # while self.user_wins < 4 and self.computer_wins < 4:
        while True:

            if self.user_wins ==3 or self.computer_wins == 3:
                print(f" GAME ENDING:.... user score: {self.user_wins} ||| Computer score: {self.computer_wins}")
                break
            else: 
                print(f'----------Round: {self.rounds}-------------')
                self.rounds = self.rounds +1
                pass 
            
            print(f"user score: {self.user_wins} ||| Computer score: {self.computer_wins}")
            model = load_model('keras_model.h5')
            cap = cv2.VideoCapture(0)
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            cv2.imshow('frame', frame)
            print('Ok the camera is now on. Show me your choice')
            prediction = model.predict(data)

            print(prediction) #test to see if the values are changing - REMOVE

            current_time = time.time()
            elapsed_time = current_time - CvRps.start_time
            if elapsed_time > CvRps.seconds:
                self.stop_camera(cap)#call the method to stop the camera
                self.get_user_choice(prediction)#call the convert the array to a choice
        
        else: 
            print('hit the last else') 
                

        
    def stop_camera(self, cap):
        print('...camera now stopping') #just a test - REMOVE 
        cap.release()# After the loop release the cap object
        cv2.destroyAllWindows()# Destroy all the windows
        print('...camera stopped') #just a test - REMOVE 
        pass   

    def get_user_choice(self, prediction):
        np.array(prediction) #convert to array
        idx_max = prediction.argmax() #find the max value
        choices = ["rock", "paper", "scissors", "nothing"]
        user_camera_choice = choices[idx_max]
        print(f'...You chose {user_camera_choice}')
        self.get_computer_choice(user_camera_choice) 

    def get_computer_choice(self,user_choice):
        computer_choice = random.choice(CvRps.choice_list)
        print(f'...The computer chose {computer_choice}')
        self.get_winner(user_choice, computer_choice)

    def get_winner(self, user_choice, computer_choice):
        print(f"...You picked: {user_choice}. The computer picked {computer_choice}") #just testing to see if it makes it here
        print(f'...checking result:')
        stars = '**********'
        if computer_choice == user_choice:
            print(f"{stars} It's a draw! {stars}")
        elif computer_choice == 'rock' and user_choice == 'scissors':
            self.computer_wins += 1
            print(f'{stars} You lost {stars}')
        elif computer_choice == 'rock' and user_choice == 'paper':
            print(f'{stars} You won {stars} ')
            self.user_wins += 1
        elif computer_choice == 'paper' and user_choice == 'rock':
            print(f'{stars} You lost {stars}')
            self.computer_wins += 1
        elif computer_choice == 'paper' and user_choice == 'scissors':
            print(f'{stars} You won {stars} ')
            self.user_wins += 1
        elif computer_choice == 'scissors' and user_choice == 'rock':
            print(f'{stars} You won {stars} ')
            self.user_wins += 1
        elif computer_choice == 'scissors' and user_choice == 'paper':
            print(f'{stars} You lost {stars}')
            self.computer_wins += 1
        else:
            print('No Result: Seems to be an error somewhere')

def play_rps():
    game = CvRps(3)
    game.get_prediction(3)
    print('game end')
    print()
    cv2.VideoCapture(0).release()# After the loop release the cap object
    cv2.destroyAllWindows()# Destroy all the windows


# play_rps()