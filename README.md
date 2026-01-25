# Tic-Tac-Toe-playing-agent-using-reinforcement-learning
It is a normal reinforcement learning model which trains itself to play tic tac toe. It shows all the games it played in real time, and also plots the learning curve per few hundered episodes. This is just like my first step in Reinforcement learning. This has two codes, one with no UI and other with UI, they both follow same logic



# Tic Tac Toe AI with Real-Time Learning Visualization

The project provides:

- **Visual AI Training** – Watch the AI make moves on a Pygame board while learning.
- **Real-Time Learning Curves** – TD error (Q-update magnitude) is plotted live using Matplotlib to show the agent’s learning progress.
- **AI Self-Play Visualization** – After training, the AI can play against itself to demonstrate its learned strategy.
- **Human vs AI Gameplay** – After AI training, the user can play against the trained AI.

### Key Concepts

- **Q-Learning**: The agent maintains a Q-table that maps board states and actions to expected rewards.
- **TD Error**: Measures how much the Q-value changes with each update; used for plotting the learning curve.
- **Exploration vs Exploitation**: During training, the AI sometimes makes random moves (exploration) to discover better strategies.
- **Epsilon Decay**: Exploration probability decreases over time, making the AI rely more on learned strategies.

