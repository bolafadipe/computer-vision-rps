from email.utils import parseaddr
import random


# take the computer choice
# take the user guess



class Rps:

    def __init__(self, choiceList):
        self.choiceList = choiceList
        self.computerChoice = random.choice(choiceList)

    def get_computer_choice(self,userChoice1):
        # print(f'get_computer_choice prints as {self.computerChoice}')
        # print(f'inhereted get_user_choice prints as  {userChoice1}')
        print(f"You picked: {userChoice1}. The computed picked {self.computerChoice}")

        if self.computerChoice == userChoice1:
            print("It's a draw!")
        elif self.computerChoice == 'rock' and userChoice1 == 'scissors':
            print('You lost')
        elif self.computerChoice == 'rock' and userChoice1 == 'paper':
            print('You Won')
        elif self.computerChoice == 'paper' and userChoice1 == 'rock':
            print('You lost')
        elif self.computerChoice == 'paper' and userChoice1 == 'scissors':
            print('You won')
        elif self.computerChoice == 'scissors' and userChoice1 == 'rock':
            print('You won')
        elif self.computerChoice == 'scissors' and userChoice1 == 'paper':
            print('You lost')
        else:
            print('No Result: Seems to be an error somewhere')

        

    def get_user_choice(self):
        while True:
            userChoice = str(input('please select Rock, Paper or Scissors'))
            userChoice = userChoice.lower()
            if userChoice not in self.choiceList:
                print('error, please try again: ')
            else:
            # print(f'get_user_choice prints as {userChoice}')
                self.get_computer_choice(userChoice)

    def get_winner(self):
        self.get_user_choice()



     
# choiceList = ['rock', 'paper', 'scissors']

# game = Rps(choiceList)

# game.get_winner()



def play_rps(choiceList):
    game = Rps(choiceList)
    game.get_winner()


if __name__ == '__main__':
    choiceList = ['rock', 'paper', 'scissors']
    play_rps(choiceList)
