from email.utils import parseaddr
import random


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





class Rps:

    def __init__(self, choiceList):
        self.choiceList = choiceList

    def get_computer_choice(self,userChoice1):
        computerChoice = random.choice(self.choiceList)
        print(f"You picked: {userChoice1}. The computed picked {computerChoice}")
        self.get_winner(userChoice1, computerChoice)

        

    def get_user_choice(self):
        while True:
            userChoice = str(input('please select Rock, Paper or Scissors or type "End Game" to end the game. Your choice: '))
            userChoice = userChoice.lower()
            if userChoice == 'end game':
                break
            elif userChoice not in self.choiceList:
                print('error, please try again: ')
            else:
                self.get_computer_choice(userChoice)



    def get_winner(self, userChoice2, computerChoice2):
        if computerChoice2 == userChoice2:
            print("It's a draw!")
        elif computerChoice2 == 'rock' and userChoice2 == 'scissors':
            print('You lost')
        elif computerChoice2 == 'rock' and userChoice2 == 'paper':
            print('You Won')
        elif computerChoice2 == 'paper' and userChoice2 == 'rock':
            print('You lost')
        elif computerChoice2 == 'paper' and userChoice2 == 'scissors':
            print('You won')
        elif computerChoice2 == 'scissors' and userChoice2 == 'rock':
            print('You won')
        elif computerChoice2 == 'scissors' and userChoice2 == 'paper':
            print('You lost')
        else:
            print('No Result: Seems to be an error somewhere')

def play_rps(choiceList):
    game = Rps(choiceList)
    game.get_user_choice()



