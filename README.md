# Game Theory & Life Test
This creates a program that tests various solutions to the Prisoner's Dilemma as well as Conway's Game of Life with a graphical user interface in python.
The GT script defines the basic framework for simulating the Prisoner's Dilemma game with various strategies. It runs each strategy pairing for a specified number of rounds and prints the results.
![image](https://github.com/pixelpump/gametheory/assets/405196/17aeab92-8dd6-42da-8764-1f3435bda201)


The GOL script sets up a simple GUI using tkinter. You can interact with the grid by clicking cells to toggle their state between alive and dead. Press the spacebar to start and stop the simulation, and press Enter to advance the simulation by one step.

Key Features of GOL
Canvas Drawing: Uses tkinter.Canvas to draw the grid and cells.
Event Binding: Binds mouse clicks to toggle cell states and keyboard events to control the simulation.
Game Logic: Implements the rules of Conway's Game of Life.
![Screenshot 2024-06-21 150530](https://github.com/pixelpump/gametheory/assets/405196/f4229410-f0b0-44d9-b8d2-464a0e2a310c)
