Updated 2017/09/24 by Jacob Stringer

Created 2017/09/21 by Jacob Stringer

# Execution
Please refer to README.md for instructions of how to set up the project. All the files in the controllers folder
get called by the API endpoints found in application/app.py. 



# Structure of controllers files:

file | import
---  | ---
app | card_logic, state_printer
state_printer | database_functions
card_logic | ai, game_state_functions
ai | database_functions
game_state_functions | trade
trade | database_functions
database_functions | All Models

This is the importing hierarchy. Files import only the files directly underneath them. The models are imported by
database_functions which is then imported by all the other files above it in the hierarchy.

## app.py
This is the API gateway. It accepts all calls from the front end. It uses game_state to set up the game, then card_logic
to change the state of the game. It calls state_printer to get the dictionary giving the game's state information.

## state_printer.py
This set of functions assists app.py in cleaning incoming data and getting output data ready. They do not change the
state of the game.

## card_logic.py
This set of functions deals with playing cards. The main function here is process_card, which maps moves to many other
functions. Understanding this function is enough to understand the entire card playing sequence.

## ai.py
This file contains AI logic to make their card choices smarter. Currently it is only a stub awaiting further development.

## game_state_functions.py
This file contains functions to set up the game and the functions that update the game object (round and age increments),
player object, and the associated calculations needed for both (like research and military calculations).

## trade.py
This file contains all the trading and check move logic. It imports from database_functions.

## database_functions.py
This file contains the db_committing_function that each of the other files use. It also imports all the models, which
are then used by others higher up the hierarchy. Increasingly, I am moving and standardising all the database calls to
getters in this file to clean up the back end code base. Others will be needed as the refactoring process happens.
