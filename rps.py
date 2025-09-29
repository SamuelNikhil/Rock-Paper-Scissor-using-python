import argparse
import sys
import random
from enum import Enum

def rps():

    ## Game Logics
    def rps_play():
        
        ## Enum for easy acces
        class RPS(Enum):

            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        # Gets input from the user (as numbers) then gets the value from enum (as RPS.Value) RPS=className
        playerChoice = input("Choose \n1. Rock \n2. Paper \n3. Scissor \n\nEnter your try: ")
        player = RPS(int(playerChoice))

        if playerChoice not in ['1','2','3']:

            print("Error data entry! ")
            return  rps_play()

        # Using Math Random module Randomizing the computer/pythons choice
        computerChoice = random.choice("123")
        computer = RPS(int(computerChoice))

        ## Function to handle the game winner
        def winner(player, computer):

            # Handling the winning moves in a dict for clean code
            winningMoves = {
                    # Declared the Enum values
                    RPS.ROCK: RPS.SCISSOR,
                    RPS.SCISSOR: RPS.PAPER,
                    RPS.PAPER: RPS.ROCK
            }

            # Comparing the choices
            if player == computer:
                return 'Tie game...\n'
            elif winningMoves[player] == computer:
                return f'You Won {args.name}!\n'
            else:
                return 'Python Wins!\n'

        print(f'\n{args.name}You choose {player.name}')
        print(f'Computer choose {computer.name}\n')
        
        result = winner(player,computer)
        print(result)

        ## Checks if player wanted to play again
        def play_again():

            playAgain = input("You to play again ?\nY for Yes \nN for No \nReady to play? :")
            while(playAgain):
                if playAgain not in ['y','Y','N','n']:
                    print("\nChoose Y or N")
                    play_again()

                elif playAgain in ['y','Y']:
                    rps_play()
 
                else:
                    print("Hope we see you again!....")
                    sys.exit()
        
        return play_again()

    return rps_play
            
game = rps()

## Wlc msg using argument *compile with -n (user name)*
parser = argparse.ArgumentParser(

    description="get the name of the user"

)

parser.add_argument(

    '-n','--name',metavar='name',
    required=True, help="To welcome greet the user"
)

args = parser.parse_args()

msg = f"\nWelcome {args.name}\n"
print(msg)

## This module only runs if its __main__ file 
if __name__ == '__main__':
    game()