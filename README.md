# Tic-Tac-Toe-playing-agent-using-reinforcement-learning
It is a normal reinforcement learning model which trains itself to play tic tac toe. It shows all the games it played in real time, and also plots the learning curve per few hundered episodes. This is just like my first step in Reinforcement learning. This has two codes, one with no UI and other with UI, they both follow same logic



# Requirements
Python 3.x
Libraries:
 - pygame
 - matplotlib

Install dependencies using:

# bash pip install pygame matplotlib

# How to Run
1. Run the Python script:
# bash python tic_tac_toe_ai.py
2. Training Phase:
  - The AI will play games against itself.
  - pygame window shows board moves.
  - Matplotlib window shows the TD error (loss) decreasing over episodes.
3. AI Self-Play Phase:
  - After training, the AI plays against itself.
  - Pygame window shows moves and announces winner.
4. Human Play Phase:
  - Click on the Pygame board to place your move (O).

# Features
 - Real-time AI training visualization.
 - Real-time learning curve plotting with Matplotlib.
 - Self-play mode for AI.
 - Human vs AI gameplay after training.

Adjustable parameters: learning rate (ALPHA), discount factor (GAMMA), epsilon decay.
AI (X) responds automatically.

Game ends with winner announcement.
