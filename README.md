# Game Theory & Life Test
To create a program that tests various solutions to the Prisoner's Dilemma as well as Conway's Game of Life with a graphical user interface in python.

The GT script defines the basic framework for simulating the Prisoner's Dilemma game with various strategies. It runs each strategy pairing for a specified number of rounds and prints the results.

The GOL script sets up a simple GUI using tkinter. You can interact with the grid by clicking cells to toggle their state between alive and dead. Press the spacebar to start and stop the simulation, and press Enter to advance the simulation by one step.

Key Features of GOL
Canvas Drawing: Uses tkinter.Canvas to draw the grid and cells.
Event Binding: Binds mouse clicks to toggle cell states and keyboard events to control the simulation.
Game Logic: Implements the rules of Conway's Game of Life.
