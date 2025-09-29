Rock Paper Scissors – Python CLI Game
=====================================

A simple command-line Rock Paper Scissors game built with Python! This interactive game lets you challenge your computer in a classic battle of wits and luck. Choose your move, see what Python picks, and find out who wins!

Features
--------
- Enum-based game logic for clean and readable code
- Randomized computer choices using Python's `random` module
- Personalized welcome message using command-line arguments
- Replay option to keep the fun going
- Input validation to ensure smooth gameplay

How to Run
----------
python rps_game.py -n YourName

How It Works
------------
- You choose Rock (1), Paper (2), or Scissors (3)
- The computer randomly picks its move
- The winner is determined based on classic RPS rules
- You can play again or exit the game

Requirements
------------
- Python 3.x

Example
-------
$ python rps_game.py -n Alex

Welcome Alex

Choose 
1. Rock 
2. Paper 
3. Scissor 

Enter your try: 2

AlexYou choose PAPER
Computer choose ROCK

You Won Alex!
