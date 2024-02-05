# Simple Turn-Based Battle Game

## Overview
This codebase contains the implementation of a simple turn-based game using Python and Pygame. The game features a player-controlled knight character and an enemy bandit characters which is controlled by an AI. The player and enemies take turns to perform actions such as attacking and defending.

## File Structure
- `main.py`: Contains the main game logic and event handling code.

## Gameplay
The game starts with a main menu where you can start the game by pressing the spacebar. In the start menu, you can enter the name of your character. The game then proceeds to the gameplay screen where you can see your character and the bandits. You can use the arrow keys to navigate the menu and select options.

The game is turn-based, meaning that each character takes a turn to attack. The knight can attack the bandits by pressing the 'E' key and selecting the bandit to attack. The bandits will also attack the knight automatically. The health of each character is displayed on the screen.

The game ends when either all the bandits are defeated or the knight's health reaches zero. In either case, a game over screen is displayed with options to replay the game or quit.

## Features
- Turn-based gameplay with player and enemy actions.
- GUI elements for player interaction, including different attack options and selecting target
- Sound effects.
- Attack effects
- Victory and defeat conditions based on the game state.

## How to Run
To run the game, ensure that Python and Pygame are installed on your system. Then, execute the `main.py` file using a Python interpreter.
