
"""
Module overview:
    Creates a function called: "play_rps" which gets passed a "choiceList" (which is assigned in "manual_rps" file)

    Creates a class instance called "Rps" with three methods and one initialized attribute:
        Initialized attribute:
            choiceList (passed via the class parameters)
        Methods:
            get_computer_choice
            get_user_choice
            get_winner

Module behaviour:
    "play_rps" function is created and passed the "choiceList" 
        "game" object is created as an instance of the "Rps" class and is passed the "choiceList"
        "game.get_user_choice" method is called
            "get_user_choice" method asks the user for an input and assigns it to the variable 'userChoice'
            "get_user_choice" method then typecasts & lowers the "userChoice" variable (with basic error handling)
            "get_user_choice" method then calls the "get_computer_choice" method and passes the 'userChoice' variable along with it as "userChoice"
                "get_computer_choice" runs with the "userChoice" variable renamed as "userChoice1" (renamed to avoid confusion)
                "get_computer_choice" method then assigns a random option from the "choicelist" to the variable "computerChoice"
                "get_computer_choice" method then calls the "get_winner" method and passes it the "userChoice1" and "computerChoice" 
                    "get_winner" method runs and recieves the two args renamed as "userChoice2" and "computerChoice2" (renamed to avoid confusion)
                    "get_winner" method then prints the "userChoice2" and "computerChoice2" variables
                    "get_winner" method then checks uses if-else to check which player wins the game 
                    "get_winner" method then prints the result


"""


import random



class Rps:

    choice_list = ['rock', 'paper', 'scissors'] #declared this outside the init without self

    def __init__(self):
        pass
        
        

    def get_computer_choice(self,user_choice):
        computer_choice = random.choice(Rps.choice_list)
        print(f"You picked: {user_choice}. The computed picked {computer_choice}")
        self.get_winner(user_choice, computer_choice)

        

    def get_user_choice(self):
        while True:
            user_choice = str(input('please select Rock, Paper or Scissors or type "End Game" to end the game. Your choice: '))
            user_choice = user_choice.lower()
            if user_choice == 'end game':
                break
            elif user_choice not in Rps.choice_list:
                print('error, please try again: ')
            else:
                self.get_computer_choice(user_choice)



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
    game = Rps()
    game.get_user_choice()



